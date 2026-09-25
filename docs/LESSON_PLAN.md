# 📖 Lesson Plan — Electronics-Circuits-Bench

> **Chain K — Hardware & Systems Foundations** | Electronics fundamentals at a real bench: voltage, current, resistance, components, breadboarding, soldering, and reading a multimeter.

## What This Project Is

Learn electronics at a real bench — Ohm's law, components, breadboarding, soldering, and diagnosing a circuit with a multimeter.

## Learning Objectives

By the end I can:

1. Apply Ohm's law to size a resistor correctly.
2. Identify common components and explain what each does.
3. Prototype a working circuit on a breadboard.
4. Solder a joint that is mechanically and electrically sound.
5. Measure voltage, continuity, and resistance with a multimeter.
6. Diagnose a non-working circuit systematically.

## Software You Will Use

- Breadboard, jumper wires, component assortment.
- A digital multimeter.
- A soldering iron.
- Falstad or similar for simulation.

## Build Order

1. Work through Ohm's law calculations on paper.
2. Build an LED circuit and size the resistor yourself.
   - 🎥 [Breadboard Jumpering — Collin's Lab Notes (Adafruit)](https://www.youtube.com/shorts/ZQFdzvKB0yw) — a quick look at clean jumper routing before you start placing components.
3. Add a transistor as a switch.
4. Measure every node and compare against prediction.
   - 🎥 [Collin's Lab: Multimeters (Adafruit)](https://www.youtube.com/watch?v=rPGoMbVSUu8) — watch this before your first real measurement if you've never held a meter before; covers voltage/resistance/current/continuity, the same four modes Lesson 2 walks through.
5. Solder the circuit onto perfboard.
   - 🎥 [Collin's Lab: Soldering (Adafruit)](https://www.youtube.com/watch?v=QKbJxytERvg) — watch the joint being made in real time before you pick up the iron; this is the same video linked from Lesson 3 of the interactive tour, worth watching here too if you're jumping straight to the hardware appendix.
6. Introduce a fault deliberately and find it with the meter.

## Common Mistakes to Avoid

- Omitting a current-limiting resistor and destroying the LED.
- Reversing polarity on a polarised component.
- Cold solder joints that look fine and fail intermittently.
- Measuring current in parallel and blowing the meter fuse.
- Working on a live circuit.

## Check Your Understanding

The quiz covers Ohm's law, component identification, multimeter use, and fault-finding order.

## Why This Matters (Industry Application)

Hardware skills complement software ones and are increasingly relevant with IoT and edge devices. Being
able to diagnose whether a problem is electrical or logical — and to repair rather than replace — is a
genuinely useful, uncommon combination.

## Reflection Questions

- What did measuring actually teach you that the calculation did not?
- How does systematic fault-finding here compare to debugging software?
