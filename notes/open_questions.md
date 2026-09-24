# Remaining follow-up items

The series runs September 28 and October 12, 2026, 3:30–5:15 PM in McCourtney
Hall B01. Alex approved 35 minutes presentation, 10 Q&A, 45 hands-on, and 15
regroup per meeting. See [seminar notes](seminar_notes.md) for verification and
[the session guide](../resources/workshops/cstr/activities/session_guide.md) for
the current in-room activity scope.

**As of 2026-09-24, Part 1 is four days away and the announcement has not been
sent** (item 9). Items 9, 10, and 2 are the time-critical ones; the rest improve
a series that would already run.

Resuming on another machine: read [machine_setup.md](machine_setup.md) first.

1. **Rehearse both session decks.** The split is built and visually reviewed:
   Part 1 has 27 frames and Part 2 has 31. Verify each fits its 35-minute
   presentation slot while preserving the activity and regroup time.
2. **Recheck time-sensitive claims before each session.** Model availability,
   product limits, Notre Dame approvals, and sponsor restrictions can change.
   Use [references](references.md). This overnight edit preserves the existing
   slides' claims; it is not a fresh product or policy audit.
3. **Remove DRAFT when Alex requests it.** Retained on both session titles.
4. **Handout built.** The two-page standalone reference is in `handout/`. Review
   the final wording and print double-sided for participants if desired.
5. **Capture the desktop app screenshot for Part 1 frame 12.** The placeholder
   remains. Use the Code tab with several sessions and one conversation visible.
   Hide private project names and keep the visible text to roughly 8–15 lines.
6. **Pilot the activities with learners.** The novice/median/power-user completion
   targets are design estimates. Observe the 45-minute block with public-only
   copies and verify that participants can explain their checks. Adjust scope
   from those observations without removing the human evidence review.
7. **Session split complete.** Original slides 1–26 / 27–54 are preserved in two
   builds with titles, closings, and a Part 2 reconnect. No slides were cut.
8. **Starter recovery and runtime verification complete.** All five release
   checks and public docs passed after the merge; see seminar notes. The tools
   now support this machine's separate checkout locations.
9. **Send the announcement and prerequisites. Time-critical.** It has not been
   sent.
   Participants need accounts, installed tools, a private working copy, and a
   working environment before Part 1. Say that both meetings use one project,
   extraction resumes in Part 2, and the fortnight is for experimenting on
   their own research. Additional literature searching is optional.
10. **Act on the September 24 PDF review.** All eight documents were rebuilt and
    handed to Alex for review in transit: both session decks, the combined
    58-frame build, the handout, the report template, the fallback report, and
    the two instructor-only answer documents. **No changes have been made from
    that review**; anything Alex marked up is still outstanding.
11. **Give `report/` a `Makefile`.** `audit_fallback.tex` needs an explicit
    BibTeX pass and fails quietly without one — `woolf2009cstr` renders as `[?]`
    and the section references resolve to `??`. Participants will hit this, and
    so will anyone building it live. See [machine_setup.md](machine_setup.md).
12. **Decide the instructor-only questions** recorded in the private repository:
    which regroup reveals to show, and whether the worked solutions are
    distributed after the series. Neither blocks Part 1.

No repository may be pushed without Alex's approval.
