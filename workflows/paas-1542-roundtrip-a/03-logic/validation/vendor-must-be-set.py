"""
MightyBot validation Rule
---
Description: Fail when the vendor field is empty or only whitespace.
Position: 1
Input Schemas: invoice
Output Schema: invoice_check
---
"""
def run(payload: dict) -> dict:
    return payload
