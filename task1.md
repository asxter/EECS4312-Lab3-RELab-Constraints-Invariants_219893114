# Title: Task 1 - Elicitation Questions

The initial problem statement for the medication dispensing system leaves many
details vague.  Before any implementation can begin, any assumptions
must be found and resolved.  Below is a set of eight elicitation
questions to do the same.  

1. **What uniquely identifies a patient?**  (e.g. health card number,
   internal patient ID, full name and date of birth).  This determines how
   dispensing events are connected to the correct individual.

2. **How is the date of a dispensing event recorded?**  Is the time
   relevant, or is a daily date check sufficient for enforcing the
   “no duplicate dispensing per day” rule?

3. **Do medication names include strength or formulation?**  For example,
   is Aspirin 81 mg distinct from Aspirin 325 mg or are they treated as
   the same medication with different doses?  This affects how 
   dispensing works and how maximum doses are applied.

4. **Are fractional doses permitted?**  Can a dose be a non‑integer value
   such as 12.5 mg, and if so, how many decimal places are acceptable?

5. **Can multiple medications be dispensed in a single transaction?**  If
   so, are they recorded as separate events or single?

6. **How is each medication’s maximum daily dose defined and managed?**
   Where does this limit come from (e.g. manufacturer guidelines, clinical
   policies, prescription), and can it vary by patient (e.g. weight‑based dosing)?

7. **What should the system do when an attempted dispensing violates a
   constraint or invariant?**  Should it stop, refuse and display an error,
   discard it, log it for review, or prompt the user for an override?

8. **Are there medications or circumstances that require special
   handling?**  For example, controlled substances may require additional
   verification, or certain drugs may permit multiple dispenses in a day
   under specific conditions.
