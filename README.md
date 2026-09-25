# Electronics-Circuits-Bench

### Electronics fundamentals at a real bench: voltage, current, resistance, components, breadboarding, soldering, and reading a multimeter.

![Chain K](https://img.shields.io/badge/Chain%20K-64748B?style=for-the-badge) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](LICENSE-GPL) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue?style=for-the-badge)](LICENSE-AGPL)

[🎮 Interactive Tour](docs/interactive/index.html) · [📋 Cheat Sheet](docs/CHEATSHEET.pdf) · [📖 Full Lesson](docs/LESSON.pdf) · [🔗 Resources](docs/RESOURCES.pdf)

<!-- SCREENSHOT PLACEHOLDER: docs/screenshots/overview.png -->

Part of **Chain K — Hardware & Systems Foundations**.

## What this is

This is the bottom of the hardware stack — everything else in Chain K, and every physical thing you'll
ever build, ultimately comes down to voltage, current, and resistance actually doing what you predicted.
We're building working knowledge of four things in order: **Ohm's law** (the math that predicts a
circuit's behavior before you touch it), **the bench** (a multimeter and a breadboard, and the specific
ways each one lies to you if you don't know its failure modes), **soldering** (making a joint that's
mechanically and electrically sound — flux is the actual lesson here, not the iron), and **debugging**
(finding a fault in a dead circuit with three measurements instead of guessing and swapping parts).

Every circuit in this project runs in your browser first, in a real circuit simulator — this is
emulation-first, with real-hardware notes throughout for what changes once you're actually at a bench
with an iron in hand.

## Prerequisites

| Requirement | Notes |
|---|---|
| A modern browser | Chrome, Firefox, Safari, or Edge — the interactive tour is a single HTML file, no install |
| Python 3.8+ (for the exercises) | Check with `python3 --version` |
| Nothing else required to start | Real breadboard/multimeter/soldering iron only needed once you move to the hardware appendix — see the [Hardware Buying Guide](#hardware-buying-guide-what-to-look-for--red-flags) below before buying anything |

## Quick Start

1. **Open the interactive tour.** Double-click `docs/interactive/index.html`, or open it from your
   browser with `File → Open`. It works straight from disk — no server, no build step.
2. **Work Lesson 1 first.** Read the lesson body on the left, then the practice panel on the right.
   Each lesson ends with a **Quick Check** — you can't move to the next lesson until you answer it
   (right or wrong doesn't matter, answering does — the explanation shown after is the point).
3. **Open the Simulation tab** when a lesson tells you to. It embeds Falstad CircuitJS directly, with
   that lesson's guided exercise listed underneath so you're not hunting for what to build.
   > ⚠️ **You may get stuck here:** if the simulator doesn't load in the embedded frame, some
   > browsers block third-party iframes by default. Use the "open it in a new tab" link right above
   > the frame instead — the exercises work identically in a separate tab.
4. **Work through all 4 lessons**, then take the **Quiz** tab (5–8 questions, immediate feedback).
5. **Try the Flashcards, Match, and Pop Quiz tabs** once you've done the lessons — these pull from the
   same key terms and question bank, just in a different format, for spaced review.
6. **Do the skeleton-code exercise.** Open a terminal in this project's folder and run:
   ```bash
   cd exercises
   python3 -m venv .venv && source .venv/bin/activate
   pip install pytest
   pytest -v
   ```
   You'll see 7 failing tests. Open `exercises/circuit_calculator.py` and implement the five functions
   — each has a docstring pointing back at the exact lesson concept it matches. Full instructions in
   [`exercises/README.md`](exercises/README.md).
   > ⚠️ **You may get stuck here:** if `pytest` isn't found after `pip install pytest`, confirm the
   > virtual environment is actually active — your terminal prompt should show `(.venv)`. If it
   > doesn't, re-run the `source .venv/bin/activate` line (Windows: `.venv\Scripts\activate`).
7. **Check the Report Card tab** any time to see your progress — quick checks, quiz score, pop quiz
   results, flashcards known, and your best Match-game round, all in one place. Click **Print / Save
   as PDF** and choose "Save as PDF" in the print dialog to keep a dated copy in `docs/`.

## Exercise Overview

| # | Lesson | Concept | Simulator exercise |
|---|---|---|---|
| 1 | Ohm's law | `V = I × R`, series resistance, why an LED needs a series resistor | Build a voltage divider, predict Vout before measuring it |
| 2 | The bench | Voltage in parallel, current in series, continuity, breadboard rails | Measure the divider's Vout and current, then check both rails for a split |
| 3 | Soldering & flux | What flux actually does, reading a joint, temperature/safety | (real-hardware) practice joints — good, cold, bridge, insufficient |
| 4 | Debugging | Fault-finding order: power → ground → orientation → joints | Introduce one fault on purpose, debug it in order, note which measurement found it |

**Learning path:**
```
Lesson 1 (Ohm's law)  →  Lesson 2 (the bench)  →  Lesson 3 (soldering)  →  Lesson 4 (debugging)
        ↓                                                                          ↓
  exercises/ (circuit_calculator.py)                                    Quiz → Flashcards/Match/Pop Quiz
```

## Hardware Buying Guide (what to look for & red flags)

**Parts list:** a breadboard + jumper wire + component kit (resistors, capacitors, diodes, transistors,
LEDs), a digital multimeter, a soldering iron, wire strippers, and a heat-shrink assortment. All shared
across most of Chain K — see [`../HARDWARE_SHOPPING_LIST.md`](../HARDWARE_SHOPPING_LIST.md#shared-starter-kit--buy-once-reuse-everywhere)
for Budget/Mid/Premium picks with current links.

**What to look for:** a True-RMS auto-ranging multimeter (cheap ones are genuinely fine here — see the
shopping list), a portable USB-C/DC soldering iron (TS100-style) over a cheap fixed-temp iron, and a
component kit that includes an assortment of resistor values, not just a handful.

**Red flags:** multimeters with no fuse rating listed, soldering irons with no adjustable temperature,
and breadboards sold with no rail continuity guarantee (see Lesson 2's "split rail" trap).

## Why This Matters (Industry Application)

Hardware skills complement software ones and are increasingly relevant with IoT and edge devices. Being
able to diagnose whether a problem is electrical or logical — and to repair rather than replace — is a
genuinely useful, uncommon combination.

## How This Connects

Chain K (Hardware & Systems Foundations). Underpins the GPIO work in **Raspberry-Pi-Tinkering** and the
wiring in **Cyberdeck-Build**.

## Project Layout

```
Electronics-Circuits-Bench/
├── docs/
│   ├── interactive/index.html   # the tour: lessons, quiz, flashcards, match, pop quiz, sim, report card
│   ├── LESSON_PLAN.md           # short build-plan reference
│   ├── LESSON.pdf               # the full written lesson, printable
│   ├── CHEATSHEET.pdf           # one-page formula/rule recap, printable
│   └── RESOURCES.pdf            # further-reading links, printable
├── exercises/
│   ├── circuit_calculator.py    # skeleton — implement the 5 functions
│   ├── test_circuit_calculator.py
│   └── README.md                # exercise-specific setup/instructions
└── README.md                    # this file
```

---
Dual licensed — [GPL v3](LICENSE-GPL) and [AGPL v3](LICENSE-AGPL).
