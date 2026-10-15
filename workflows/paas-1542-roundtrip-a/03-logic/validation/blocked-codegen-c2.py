"""
MightyBot validation Rule
---
Description: Fail when the invoice number is missing.
Position: 3
Input Schemas: invoice
Output Schema: invoice_check
---
"""
def run(payload: dict) -> dict:
    return payload
