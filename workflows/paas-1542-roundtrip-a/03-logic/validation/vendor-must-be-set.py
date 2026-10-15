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
    """Fail when the vendor field is empty."""
    invoice = instance.data.select('invoice').first()
    if invoice is None:
        return {"passed": False, "reason": "No invoice data found"}

    vendor = invoice.get('vendor')
    if not vendor or not isinstance(vendor, str) or len(vendor.strip()) == 0:
        return {"passed": False, "reason": "Vendor field is empty"}

    return {"passed": True}

result = validate_vendor_not_empty(instance)
