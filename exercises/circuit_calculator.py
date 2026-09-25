"""
Circuit Calculator — fill in the five functions below.

Every formula here is one you already saw worked out by hand in the interactive
tour (docs/interactive/index.html, Lesson 1 and the Cheat Sheet tab). This file
turns "I can follow the math on the page" into "I can write the math myself" —
the same gap MuseumsNotebook/PhoneBook ask you to close, just for circuits
instead of data or abstraction.

Run the tests as you go:  pytest exercises/test_circuit_calculator.py -v
All five start failing. Implement one function, re-run, watch it turn green,
move to the next — don't write all five before running the tests once.
"""


def series_resistance(*resistances_ohms):
    """Total resistance of resistors wired in series.

    Series resistances simply add. See docs/interactive/index.html, Lesson 1:
    "Series resistances add: R_total = R1 + R2 + ..."

    >>> series_resistance(1000, 2000)
    3000
    """
    # TODO: return the sum of resistances_ohms
    raise NotImplementedError


def current_series(voltage, *resistances_ohms):
    """Current (in amps) flowing through a series circuit.

    Ohm's law: I = V / R_total. Reuse series_resistance() above rather than
    re-summing — that's the whole point of having written it.

    >>> current_series(9, 1000, 2000)
    0.003
    """
    # TODO: compute total resistance, then return voltage / total
    raise NotImplementedError


def power_dissipated(voltage, current):
    """Power in watts. P = V x I.

    The lesson's warning applies here too: a resistor can be sized right for
    current and still be under-rated for power. This function is what you'd
    use to check that before ordering a 1/4 W resistor.

    >>> power_dissipated(9, 0.003)
    0.027
    """
    # TODO: return voltage * current
    raise NotImplementedError


def divider_output(v_in, r1_ohms, r2_ohms):
    """Output voltage of a voltage divider, taken across r2.

    Vout = Vin x R2 / (R1 + R2). Matches the worked example and the SVG
    diagram in Lesson 1: 9 V across a 1 kOhm + 2 kOhm divider outputs 6 V.

    >>> divider_output(9, 1000, 2000)
    6.0
    """
    # TODO: return v_in * r2_ohms / (r1_ohms + r2_ohms)
    raise NotImplementedError


def led_series_resistor(supply_v, led_forward_v, desired_ma):
    """Minimum series resistor (ohms) to safely drive an LED.

    This is the fix for the Lesson 1 trap: an LED held at 9 V with no series
    resistor draws runaway current because an LED isn't a resistor — it holds
    a roughly fixed forward voltage. The series resistor has to absorb the
    *difference* between supply and forward voltage, at your target current.

    R = (V_supply - V_forward) / I_desired

    >>> led_series_resistor(9, 2, 0.02)
    350.0
    """
    # TODO: return (supply_v - led_forward_v) / desired_ma
    raise NotImplementedError
