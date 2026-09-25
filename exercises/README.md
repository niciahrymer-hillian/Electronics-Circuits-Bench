# Exercises — Circuit Calculator

A hands-on companion to Lesson 1 (Ohm's law) in the interactive tour. The tour shows you the math
worked out; this makes you write it.

## Setup

```bash
# from this exercises/ folder
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pytest
```

## Run the tests

```bash
pytest -v
```

You'll see 7 failing tests — every function in `circuit_calculator.py` currently raises
`NotImplementedError`. That's the starting point, not a bug.

## What to do

Open `circuit_calculator.py`. Each of the five functions has a docstring explaining the formula, a
worked-example `>>>` line showing the expected input/output, and a `# TODO` marking exactly what to
write. Implement one function, re-run `pytest -v`, watch its tests go green, move to the next.

All five formulas already appear in docs/interactive/index.html's Lesson 1 and Cheat Sheet tab — if
you get stuck, that's the place to check your formula against, not a hint file (there isn't one; the
tour already has the explanation).

## Order

1. `series_resistance` — the simplest one, just addition.
2. `current_series` — reuses `series_resistance`.
3. `power_dissipated` — one multiplication.
4. `divider_output` — matches the tour's Lesson 1 diagram exactly.
5. `led_series_resistor` — the trickiest: it's solving for the *missing* piece (the resistor) rather
   than computing a known circuit's behavior, which is closer to what you'll actually do at the bench
   when picking a resistor before you've built anything.

## When you're done

All 7 tests passing means you can compute everything the interactive tour's Lesson 1 and Cheat Sheet
show without looking either one up — which is the actual goal, not just green checkmarks.
