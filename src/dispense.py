import datetime

class DispenseEvent:
    # Example max daily dose table (mg/day).
    # You can edit/extend these values as needed for your tests.
    MAX_DAILY_DOSE_MG = {
        "Aspirin": 4000,
        "Ibuprofen": 3200,
        "Acetaminophen": 3000,
    }

    def __init__(self, patient_id, medication, dose_mg, quantity, event_date=None):
        """
        Initialize a new DispenseEvent.

        Constraints enforced (Task 3):
        1) dose_mg must be positive
        2) quantity must be a positive integer
        3) dose_mg must not exceed the medication's maximum daily dose (if known)
        5) doses are in milligrams (mg) by definition of dose_mg

        Note:
        Rule 4 (no duplicate same medication same day) is NOT a constructor constraint
        because it requires checking existing history; it is enforced in invariant_holds().
        """

        # store date for per-day invariant checking
        if event_date is None:
            event_date = datetime.date.today()
        if not isinstance(event_date, datetime.date):
            raise ValueError("event_date must be a datetime.date")
        self.date = event_date

        # prevent empty events
        if patient_id is None or str(patient_id).strip() == "":
            raise ValueError("patient_id must be provided")

        if medication is None or str(medication).strip() == "":
            raise ValueError("medication must be provided")

        # Rule 1: dose must be positive (and numeric)
        if not isinstance(dose_mg, (int, float)):
            raise ValueError("dose_mg must be a number (mg)")
        if dose_mg <= 0:
            raise ValueError("dose_mg must be a positive value (mg)")

        # Rule 2: quantity must be a positive integer
        if not isinstance(quantity, int):
            raise ValueError("quantity must be a positive integer")
        if quantity <= 0:
            raise ValueError("quantity must be a positive integer")

        # Rule 3: max daily dose (if known)
        max_allowed = DispenseEvent.MAX_DAILY_DOSE_MG.get(str(medication))
        if max_allowed is not None and dose_mg > max_allowed:
            raise ValueError(
                f"dose_mg {dose_mg} exceeds maximum daily dose {max_allowed} for {medication}"
            )

        # Save fields only after all constraints pass
        self.patient_id = str(patient_id)
        self.medication = str(medication)
        self.dose_mg = float(dose_mg)
        self.quantity = quantity


# Task 4: Define and check system invariants
def invariant_holds(existing_events, new_event):
    """
    Invariant (Rule 4):
    A patient may not receive the same medication more than once per day.

    Returns:
        True  -> invariant holds (safe to add)
        False -> invariant violated (do NOT add)
    """
    for evt in existing_events:
        same_patient = evt.patient_id == new_event.patient_id
        same_med = evt.medication == new_event.medication
        same_day = evt.date == new_event.date

        if same_patient and same_med and same_day:
            return False

    return True
