"""
MightyBot validation Rule
---
Description: Fail when the invoice total is zero or negative. Pass otherwise and explain the reason.
Position: 0
Input Schemas: invoice
Output Schema: invoice_check
---
"""
def run(payload: dict) -> dict:
    return payload
