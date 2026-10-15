"""
MightyBot validation Rule
---
Description: Fail when the invoice total is zero or negative. Pass otherwise and explain the reason.
Position: 0
Input Schemas: invoice
Output Schema: invoice_check
---
"""
def validate_invoice_total(instance):
    """Fail when invoice total is zero or negative; pass otherwise with reason."""
    invoice = instance.data.select('invoice').first()
    if not invoice:
        return {"passed": False, "reason": "Invoice data missing"}
    total = invoice.get('total')
    if total is None:
        return {"passed": False, "reason": "Invoice total missing"}
    if total <= 0:
        return {"passed": False, "reason": "Invoice total is zero or negative"}
    return {"passed": True, "reason": "Invoice total is positive"}

result = validate_invoice_total(instance)
