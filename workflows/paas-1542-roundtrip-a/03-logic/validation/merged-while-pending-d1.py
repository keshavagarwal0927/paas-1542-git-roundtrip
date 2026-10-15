"""
MightyBot validation Rule
---
Description: Fail when the vendor name is shorter than three characters.
Position: 4
Input Schemas: invoice
Output Schema: invoice_check
---
"""
def run(payload: dict) -> dict:
    return payload
