import datetime
import pytest

from src.dispense import DispenseEvent, invariant_holds


# Rule 1: The dose must be a positive value.
def test_rule1_rejects_non_positive_dose():
    day = datetime.date(2026, 1, 31)

    with pytest.raises(ValueError):
        DispenseEvent("p1", "Aspirin", 0, 1, event_date=day)

    with pytest.raises(ValueError):
        DispenseEvent("p1", "Aspirin", -5, 1, event_date=day)


# Rule 2: The quantity dispensed must be a positive integer.
def test_rule2_rejects_invalid_quantity():
    day = datetime.date(2026, 1, 31)

    with pytest.raises(ValueError):
        DispenseEvent("p2", "Aspirin", 100, 0, event_date=day)

    with pytest.raises(ValueError):
        DispenseEvent("p2", "Aspirin", 100, -2, event_date=day)

    with pytest.raises(ValueError):
        DispenseEvent("p2", "Aspirin", 100, 1.5, event_date=day)


# Rule 3: Each medication has a maximum daily dose.
def test_rule3_enforces_max_daily_dose():
    day = datetime.date(2026, 1, 31)

    max_allowed = DispenseEvent.MAX_DAILY_DOSE_MG["Aspirin"]

    # Exactly at max should be allowed
    ok = DispenseEvent("p3", "Aspirin", max_allowed, 1, event_date=day)
    assert ok.dose_mg == float(max_allowed)

    # Above max should be rejected
    with pytest.raises(ValueError):
        DispenseEvent("p3", "Aspirin", max_allowed + 1, 1, event_date=day)


# Rule 4 (Invariant): A patient may not receive the same medication more than once per day.
def test_rule4_prevents_duplicate_dispense_same_day():
    day = datetime.date(2026, 1, 31)

    first = DispenseEvent("p4", "Ibuprofen", 200, 1, event_date=day)
    duplicate = DispenseEvent("p4", "Ibuprofen", 200, 1, event_date=day)

    assert invariant_holds([first], duplicate) is False


# Edge case for Rule 4:
# Duplicate should be rejected even if dose/quantity are different, as long as patient+med+day match.
def test_rule4_edge_case_duplicate_even_if_dose_or_quantity_differs():
    day = datetime.date(2026, 1, 31)

    first = DispenseEvent("p5", "Ibuprofen", 200, 1, event_date=day)

    # Same patient + same med + same day, but different dose/quantity
    second = DispenseEvent("p5", "Ibuprofen", 400, 2, event_date=day)

    assert invariant_holds([first], second) is False
