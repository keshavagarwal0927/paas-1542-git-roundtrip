"""
MightyBot validation Rule
---
Description: Fail when the vendor field is empty or only whitespace.
Position: 1
Input Schemas: invoice
Output Schema: invoice_check
---
"""
def validate_vendor_not_empty(instance):
    """Fail when the vendor field is empty or only whitespace."""
    invoice = instance.data.select("invoice").first()
    if invoice is None:
        return {"passed": False, "reason": "Invoice data not found"}
    vendor = invoice.get("vendor") if isinstance(invoice, dict) else None
    if vendor is None or not str(vendor).strip():
        return {"passed": False, "reason": "Vendor is empty or only whitespace"}
    return {"passed": True}

result = validate_vendor_not_empty(instance)
