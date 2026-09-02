"""Minimal example: python example.py

Writes example.png, example.pdf, example.provenance.json, and
example_grayscale.png next to this file.
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figure_style as fs  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    x = np.linspace(0, 10, 200)

    fig, ax = fs.figure(fs.WIDE)
    for i in range(5):
        ax.plot(x, np.exp(-x / 6) * np.sin(x + i), color=fs.color(i),
                label=f"case {i + 1}")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel(r"Signal (mol m$^{-3}$)")

    # Anchored above the axes, not inside them. A legend placed inside would sit
    # on top of the curves -- save_fig warns about exactly that. `loc="best"` is
    # not a fix here: with five damped oscillations there is no empty corner.
    #
    # ncol=3 rather than 5: at five columns the legend is wider than the plot it
    # labels, which save_fig also warns about. Three columns wraps to two rows
    # and stays inside the axes width.
    ax.legend(ncol=3, loc="lower center", bbox_to_anchor=(0.5, 1.02),
              frameon=False, columnspacing=1.2, handlelength=1.6)

    out = os.path.join(HERE, "example")
    written = fs.save_fig(
        fig, out,
        sources=["results/demo.csv"],          # what this figure was built from
        notes="figure_style demo; synthetic data",
        close=False,
    )
    for path in written:
        print("wrote", os.path.relpath(path, HERE))

    # The greyscale check from the accessibility checklist, in one line.
    print("wrote", os.path.relpath(fs.grayscale_preview(fig, out), HERE))


if __name__ == "__main__":
    main()
