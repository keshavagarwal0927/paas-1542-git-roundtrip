"""
MightyBot validation Rule
---
Description: Fail when the vendor name is shorter than three characters.
Position: 1
Input Schemas: invoice
Output Schema: invoice_check
---
"""
def validate_vendor_name_length(instance):
    """Fail when the vendor name is shorter than three characters."""
    invoice_record = instance.data.select("invoice").first()
    if not invoice_record:
        return {"passed": False, "reason": "Missing invoice data"}

    vendor = invoice_record.get("vendor") if isinstance(invoice_record, dict) else None
    if vendor is None or len(str(vendor).strip()) < 3:
        return {"passed": False, "reason": "Vendor name is shorter than three characters"}

    return {"passed": True}

result = validate_vendor_name_length(instance)
