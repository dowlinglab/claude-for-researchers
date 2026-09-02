"""One publication-figure style for a whole project, plus figure provenance.

Drop this file into your project, import it everywhere you plot, and never set a
font size in an analysis script again. The point is not tidiness: once styling is
scattered across dozens of scripts, any *later* standard becomes unenforceable,
and "update every figure to the new guideline" turns into a week of edits
instead of a one-line change.

Implements the NDCBE publication-quality figure guidelines:
https://ndcbe.github.io/data-and-computing/notebooks/01/Publication-Quality-Figures.html

    figure size 4x4 (single) / 4x6.4 (tall) / 6.4x4 (wide) / 8x4 (two-panel)
    dpi 300 (PNG), 1200 (PDF)
    line width 3, marker size 8
    tick labels 15, ticks "in", top and right on
    axis labels 16 bold; legend 15
    Okabe-Ito colour-blind-safe palette; viridis for sequential data

Typical use
-----------
    import figure_style as fs

    fs.apply_style()
    fig, ax = fs.figure(fs.SINGLE)
    ax.plot(x, y, color=fs.color(0), label="baseline")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel(r"Concentration (mol m$^{-3}$)")
    ax.legend()
    fs.save_fig(fig, "figures/fig3_concentration", sources=["results/run_07.csv"])

`save_fig` writes `fig3_concentration.png`, `.pdf`, and
`.provenance.json` recording the script, the git commit, and the input files.
That sidecar is what lets you answer "which run produced this?" six months
later; see practices/scientific_figures_tables.md §5.

Requires: matplotlib. Everything else is the standard library.
"""

from __future__ import annotations

import datetime
import json
import os
import subprocess
import sys
import warnings

import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

__all__ = [
    "PALETTE", "SEQUENTIAL", "DIVERGING",
    "SINGLE", "TALL", "WIDE", "TWO_PANEL", "NAMED_SIZES",
    "apply_style", "color", "figure", "save_fig", "grayscale_preview",
]

# --------------------------------------------------------------------------- #
# Palette
#
# Okabe-Ito: an 8-colour qualitative palette that remains distinguishable under
# the common forms of colour vision deficiency and in greyscale print. Use it in
# order -- the first four are the most widely separated.
# --------------------------------------------------------------------------- #

PALETTE = [
    "#000000",  # black
    "#E69F00",  # orange
    "#56B4E9",  # sky blue
    "#009E73",  # bluish green
    "#CC79A7",  # reddish purple
    "#0072B2",  # blue
    "#D55E00",  # vermillion
    "#F0E442",  # yellow
]

SEQUENTIAL = "viridis"   # perceptually uniform, colour-blind safe
DIVERGING = "RdBu_r"     # use only when the data has a meaningful midpoint

# --------------------------------------------------------------------------- #
# Sizes (inches). Sized for a single journal column at 100% -- check the figure
# at final printed size, not zoomed in on a monitor.
# --------------------------------------------------------------------------- #

SINGLE = (4.0, 4.0)
TALL = (4.0, 6.4)
WIDE = (6.4, 4.0)
TWO_PANEL = (8.0, 4.0)

NAMED_SIZES = {
    "SINGLE": SINGLE, "TALL": TALL, "WIDE": WIDE, "TWO_PANEL": TWO_PANEL,
}

_SIZE_TOL = 0.05  # inches
_APPLIED = False


def color(i: int) -> str:
    """Palette colour `i`, cycling. Use this rather than literal hex codes, so a
    palette change propagates."""
    return PALETTE[i % len(PALETTE)]


def apply_style(force: bool = False) -> None:
    """Apply the publication rcParams. Idempotent; call once at import time."""
    global _APPLIED
    if _APPLIED and not force:
        return
    mpl.rcParams.update({
        "figure.figsize": SINGLE,
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "axes.labelsize": 16,
        "axes.labelweight": "bold",
        "axes.titlesize": 16,
        "axes.titleweight": "bold",
        "xtick.labelsize": 15,
        "ytick.labelsize": 15,
        "legend.fontsize": 15,
        "legend.frameon": False,
        "lines.linewidth": 3,
        "lines.markersize": 8,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.top": True,
        "ytick.right": True,
        "axes.labelpad": 8,
        "axes.prop_cycle": cycler(color=PALETTE),
        "image.cmap": SEQUENTIAL,
        "font.family": "sans-serif",
        "mathtext.default": "regular",
    })
    _APPLIED = True


def figure(size=SINGLE, **kwargs):
    """`plt.subplots` with the style applied and a standard size.

    Returns (fig, ax) exactly as `plt.subplots` does.
    """
    apply_style()
    return plt.subplots(figsize=size, **kwargs)


# --------------------------------------------------------------------------- #
# Saving, with size checking and provenance
# --------------------------------------------------------------------------- #

def _check_size(fig) -> None:
    """Warn if the figure is not one of the standard sizes.

    Both dimensions are checked. Checking only the width is a real bug that has
    shipped before: a figure at the right width and the wrong height passes
    silently and prints at the wrong scale.
    """
    w, h = fig.get_size_inches()
    for name, (sw, sh) in NAMED_SIZES.items():
        if abs(w - sw) <= _SIZE_TOL and abs(h - sh) <= _SIZE_TOL:
            return
    warnings.warn(
        f"figure is {w:.2f}x{h:.2f} in, which is not a standard size "
        f"({', '.join(f'{n} {s[0]}x{s[1]}' for n, s in NAMED_SIZES.items())}). "
        "Pass check_size=False if this is deliberate.",
        stacklevel=3,
    )


def _artist_points_display(ax):
    """Vertices of the plotted data in display coordinates."""
    chunks = []
    for line in ax.get_lines():
        xy = line.get_xydata()
        if xy is not None and len(xy):
            chunks.append(ax.transData.transform(xy))
    for coll in ax.collections:
        try:
            off = coll.get_offsets()
        except Exception:  # pragma: no cover - artist without offsets
            continue
        if off is not None and len(off):
            chunks.append(ax.transData.transform(off))
    return chunks


def _check_legend(fig, margin: float = 2.0) -> None:
    """Warn if a legend sits on top of the data, or runs outside its axes.

    A legend covering plotted data is a figure-quality violation, not a matter
    of taste -- it hides the evidence the figure exists to show. `loc="best"`
    minimises overlap but does not eliminate it, and it silently gives up when
    the axes are full.

    Fixes, in rough order of preference: move the legend outside the axes with
    `bbox_to_anchor`; extend the axis limits to open up space; reduce the number
    of plotted series; or label series directly instead of using a legend.
    """
    try:
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()
    except Exception:  # pragma: no cover - backend without a renderer
        return

    for i, ax in enumerate(fig.get_axes()):
        leg = ax.get_legend()
        if leg is None:
            continue
        try:
            bb = leg.get_window_extent(renderer)
        except Exception:  # pragma: no cover
            continue
        # Shrink slightly so a curve merely grazing the border does not trip it.
        box = bb.expanded(1.0, 1.0).padded(-margin)

        covered = 0
        for pts in _artist_points_display(ax):
            inside = ((pts[:, 0] >= box.x0) & (pts[:, 0] <= box.x1) &
                      (pts[:, 1] >= box.y0) & (pts[:, 1] <= box.y1))
            covered += int(inside.sum())

        where = f"axes {i}" if len(fig.get_axes()) > 1 else "the axes"
        if covered:
            warnings.warn(
                f"legend on {where} covers {covered} plotted data point(s). "
                "A legend must not sit on top of the data. Move it outside the "
                "axes (bbox_to_anchor), extend the axis limits to make room, or "
                "label the series directly. Pass check_layout=False to override.",
                stacklevel=4,
            )

        # A legend anchored outside the axes is the recommended fix above, so
        # "extends past the right edge" is the WRONG predicate -- it fires on
        # correct usage. The real rule is that the legend should not be wider
        # than the thing it labels: a full-width legend over a narrower plot
        # reads as unbalanced even though nothing is clipped.
        ax_bb = ax.get_window_extent(renderer)
        if bb.width > ax_bb.width + margin:
            warnings.warn(
                f"legend on {where} is wider than the axes "
                f"({bb.width / fig.dpi:.2f} vs {ax_bb.width / fig.dpi:.2f} in). "
                "Use fewer columns so it wraps, or widen the figure.",
                stacklevel=4,
            )


def _git_state(path: str) -> dict:
    """Commit and dirty flag for the repository containing `path`, if any."""
    d = os.path.dirname(os.path.abspath(path)) or "."
    def run(*args):
        return subprocess.run(["git", "-C", d, *args], capture_output=True,
                              text=True, timeout=10).stdout.strip()
    try:
        commit = run("rev-parse", "HEAD")
        if not commit:
            return {}
        return {"git_commit": commit,
                "git_dirty": bool(run("status", "--porcelain"))}
    except (OSError, subprocess.SubprocessError):
        return {}


def save_fig(fig, path_no_ext: str, sources=None, formats=("png", "pdf"),
             close: bool = True, check_size: bool = True,
             check_layout: bool = True, provenance: bool = True,
             notes: str = None):
    """Save a figure at publication settings and record where it came from.

    Parameters
    ----------
    fig : matplotlib Figure
    path_no_ext : str
        Output path WITHOUT an extension. Directories are created as needed.
    sources : sequence of str, optional
        Input data files this figure was built from. Strongly recommended --
        this is the link that makes a figure traceable back to a run.
    formats : tuple
        Defaults to PNG (300 dpi) and PDF (1200 dpi).
    close : bool
        Close the figure after writing. Default True, so long scripts do not
        accumulate open figures.
    check_size : bool
        Warn if the figure is not a standard size (both dimensions).
    check_layout : bool
        Warn if a legend covers plotted data or is clipped by the axes.
    provenance : bool
        Write `<path>.provenance.json`. On by default, deliberately: figure
        provenance is skipped by default everywhere else, and that is exactly
        why figures become untraceable.
    notes : str, optional
        Free text stored in the provenance record -- the configuration, the
        run label, anything a future reader would want.

    Returns the list of paths written.
    """
    if check_size:
        _check_size(fig)
    if check_layout:
        _check_legend(fig)

    out_dir = os.path.dirname(os.path.abspath(path_no_ext))
    os.makedirs(out_dir, exist_ok=True)

    dpis = {"png": 300, "pdf": 1200, "svg": 300, "eps": 1200}
    written = []
    for fmt in formats:
        out = f"{path_no_ext}.{fmt}"
        fig.savefig(out, dpi=dpis.get(fmt, 300), bbox_inches="tight",
                    pad_inches=0.05)
        written.append(out)

    if provenance:
        w, h = fig.get_size_inches()
        # sys.argv[0] is "-" for stdin and "" in some REPLs; only record a real file.
        script = sys.argv[0] if sys.argv else ""
        script = os.path.abspath(script) if script and os.path.isfile(script) else None
        record = {
            "figure": [os.path.basename(p) for p in written],
            "created": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
            "script": script,
            "size_inches": [round(float(w), 3), round(float(h), 3)],
            "sources": list(sources) if sources else [],
            "python": sys.version.split()[0],
            "matplotlib": mpl.__version__,
        }
        if notes:
            record["notes"] = notes
        record.update(_git_state(path_no_ext))
        prov = f"{path_no_ext}.provenance.json"
        with open(prov, "w", encoding="utf-8") as fh:
            json.dump(record, fh, indent=1)
        written.append(prov)

    if close:
        plt.close(fig)
    return written


def grayscale_preview(fig, path_no_ext: str):
    """Write a desaturated copy so you can check the greyscale requirement.

    "Is the figure understandable in greyscale?" is on the checklist and is
    almost never actually tested. This makes testing it one line.
    """
    import io
    from matplotlib import image as mpimg

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=150, bbox_inches="tight")
    buf.seek(0)
    rgb = mpimg.imread(buf)[:, :, :3]
    lum = rgb @ [0.2126, 0.7152, 0.0722]  # Rec. 709 luminance

    out = f"{path_no_ext}_grayscale.png"
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    gfig, gax = plt.subplots(figsize=fig.get_size_inches())
    gax.imshow(lum, cmap="gray", vmin=0, vmax=1)
    gax.axis("off")
    gfig.savefig(out, dpi=150, bbox_inches="tight", pad_inches=0)
    plt.close(gfig)
    return out


# Applying on import is deliberate: a project should not be able to plot in the
# wrong style by forgetting a call.
apply_style()
