# Four bounded extensions to the reactor notebook

Use the preserved baseline as the control. The starter model solves algebraic steady-state balances. It does not include reactor dynamics, measured uncertainty, or stability analysis. Each extension should produce a command, a CSV or figure, a test, and a two-sentence interpretation. Keep the original notebook and baseline unchanged.

## A. Resolve the coolant transition more closely

Start with the original 0.5 K sweep. Find adjacent sampled coolant values where the number of accepted states changes. Resweep those two intervals at 0.1 K, then optionally 0.02 K. Preserve solver tolerances, then repeat near apparent transitions with a denser initial-guess grid and check residual norms. If an intermediate state count appears, investigate whether a root was missed. Report the last grid value with one state and first with three as a bracket at each edge. Plot all states without connecting ranks across a change in multiplicity. A grid narrows a bracket; it does not locate a mathematical fold exactly.

## B. Change heat removal

At the original coolant condition, sweep `UA` from 0.8 to 1.2 times its baseline value in 0.05 increments. Keep feed, reaction, volume, and solver settings fixed. For every `UA`, report the count of distinct accepted states and the temperatures and conversions of each. Verify the baseline `UA` row reproduces the saved nominal result and every accepted residual is small. This is a parameter sensitivity study, not a prediction for a measured reactor.

## C. Change feed temperature

At the original coolant condition, sweep `Tf` from 310 to 330 K in 2 K increments. Keep other parameters fixed. Plot reactor temperature and conversion for *all* distinct states; include a state-count column. Check that the baseline `Tf` row matches saved nominal states and that conversion stays between zero and one. Do not infer dynamics or safety from the steady-state plot.

## D. Test dependence on initial guesses

Repeat the nominal solve and coolant sweep with at least two temperature guess grids: the notebook's original grid and a wider, denser grid (for example, 280–460 K every 2 K). Compare sorted root temperatures, concentrations, residual norms, and the number of states at every condition. Flag any disagreement and investigate convergence rather than hiding extra roots. Agreement is a useful robustness check, but finite guesses cannot prove completeness.

For any route, record what you varied, what stayed fixed, units, software versions, the exact command, the baseline commit, and a limitation. Add a regression test that would fail if the extension silently changed the nominal result.
