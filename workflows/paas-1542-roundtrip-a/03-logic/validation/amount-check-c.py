"""
MightyBot validation Rule
---
Description: Fail when amount is negative.
Position: 2
Input Schemas: temp_c
Output Schema: invoice_check
---
"""
def validate_amount_not_negative(instance):
    """Fail when amount is negative."""
    temp_c = instance.data.select("temp_c").first()
    amount = temp_c.get("amount") if temp_c else None

    if amount is None:
        return {
            "passed": False,
            "reason": "Amount is missing"
        }

    if amount < 0:
        return {
            "passed": False,
            "reason": "Amount is negative"
        }

    return {
        "passed": True
    }

result = validate_amount_not_negative(instance)
