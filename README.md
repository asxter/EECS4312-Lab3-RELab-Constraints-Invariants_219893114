EECS4312 Winter26: Lab3

# Title: FROM ELICITATION TO CONSTRAINTS, INVARIANTS, AND TESTS

## Student Information
**Name:** Anirudh Sundar  
**Student ID:** 219893114

---

# Medication Dispensing System Documentation

## System Description

The system is a **medication dispensing system** for a pharmacy. Its primary function is to **record each dispensing event**, capturing:

- `patient_id` (who receives the medication)
- `medication` (what is dispensed)
- `dose_mg` (dose per dispensing event, in milligrams)
- `quantity` (number of units dispensed)
- `date` (day on which the medication is dispensed)

The system operates under **safety, consistency, and policy requirements**, ensuring that invalid dispensing events are rejected and that duplicate dispensing does not occur within a single day.

---

## Identified Constraints and Invariants

### Constraints 

1. `dose_mg` must be a **positive value** in mg.
2. `quantity` must be a **positive integer**.
3. Each medication has a **maximum daily dose**, and a dispensing event may not exceed that limit.

---

### Invariants 

1. A patient may **not receive the same medication more than once per day**, regardless of dose or quantity.

---

### Functional Requirements

- Record individual medication dispensing events.
- Associate each event with a patient and medication.
- Enforce safety and policy rules through constraints and invariants.
- Prevent inconsistent or unsafe dispensing records.

---

## Mapping Tests to Requirements

| Test Case | Requirement Validated | Description |
|----------|----------------------|-------------|
| `test_rule1_rejects_non_positive_dose` | Constraint: dose must be positive | Creating a dispensing event with zero or negative dose is rejected. |
| `test_rule2_rejects_invalid_quantity` | Constraint: quantity must be a positive integer | Creating a dispensing event with zero, negative, or non-integer quantity is rejected. |
| `test_rule3_enforces_max_daily_dose` | Constraint: maximum daily dose | Dispensing a dose above the medication’s allowed maximum is rejected. |
| `test_rule4_prevents_duplicate_dispense_same_day` | Invariant: no duplicate dispensing per day | A second dispensing of the same medication to the same patient on the same day is rejected. |
| `test_rule4_edge_case_duplicate_even_if_dose_or_quantity_differs` | Invariant: no duplicate dispensing per day | Duplicate dispensing is rejected even when dose or quantity differs, as long as patient, medication, and date match. |

---
