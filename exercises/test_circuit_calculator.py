"""
Tests for circuit_calculator.py — every value here matches a worked example
from docs/interactive/index.html (Lesson 1's divider, or the Cheat Sheet's
LED row). If a test fails with NotImplementedError, that function still needs
writing. If it fails with a wrong-value assertion, check your formula against
the docstring and the tour's worked example side by side.
"""
import pytest

from circuit_calculator import (
    series_resistance,
    current_series,
    power_dissipated,
    divider_output,
    led_series_resistor,
)


def test_series_resistance_adds_two_resistors():
    assert series_resistance(1000, 2000) == 3000


def test_series_resistance_adds_three_resistors():
    assert series_resistance(100, 200, 300) == 600


def test_current_series_matches_lesson_1_worked_example():
    # 9 V across 1 kOhm + 2 kOhm in series -> 3 mA, per the tour's worked example.
    assert current_series(9, 1000, 2000) == pytest.approx(0.003)


def test_power_dissipated_matches_lesson_1_trap_example():
    # A 1/4 W resistor passing 30 mA at 9 V dissipates 0.27 W and cooks.
    assert power_dissipated(9, 0.03) == pytest.approx(0.27)


def test_divider_output_matches_lesson_1_diagram():
    # The SVG divider diagram: 9 V, R1 = 1 kOhm, R2 = 2 kOhm -> Vout = 6 V.
    assert divider_output(9, 1000, 2000) == pytest.approx(6.0)


def test_divider_output_equal_resistors_halves_voltage():
    assert divider_output(10, 1000, 1000) == pytest.approx(5.0)


def test_led_series_resistor_matches_cheat_sheet():
    # 9 V supply, ~2 V LED forward voltage, 20 mA target -> 350 ohm.
    assert led_series_resistor(9, 2, 0.02) == pytest.approx(350.0)
