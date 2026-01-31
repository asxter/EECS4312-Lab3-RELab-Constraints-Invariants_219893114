# Task 2 – Requirement Classification


<What uniquely identifies a patient?, functional requirement>
Justification: The system must record and use a defined identifier to associate events with the right patient.

<How is the date of a dispensing event recorded (is time relevant or is date enough)?, functional requirement>
Justification: The system must capture event time/date information; to “record each dispensing event.”

<Do medication names include strength/formulation (e.g., Aspirin 81 mg vs 325 mg)?, constraint>
Justification: This constrains the valid representation of the “medication” field and how the system interprets it.

<Are fractional doses permitted (e.g., 12.5 mg) and how many decimals are allowed?, constraint>
Justification: This restricts the valid input domain for dose_mg.

<Can multiple medications be dispensed in a single transaction (separate events or one record)?, functional requirement>
Justification: This affects the behavior for recording events.

<How is each medication’s maximum daily dose defined and managed, and can it vary by patient?, constraint>
Justification: Maximum-dose limits directly restrict whether an input event is valid..

<What should the system do when a dispensing attempt violates a constraint or invariant (error, discard, log, override)?, functional requirement>
Justification: This defines required system behavior in response to invalid operations.

<Are there medications/circumstances requiring special handling (e.g., controlled substances, exceptions)?, invariant>
Justification: Special handling often becomes a system-wide rule that must always hold across events, not just a single-field validity check.
