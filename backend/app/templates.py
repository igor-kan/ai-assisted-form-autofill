TEMPLATES = {
    "contact_intake": {
        "label": "Contact Intake",
        "required_fields": ["full_name", "email", "phone"],
    },
    "vendor_registration": {
        "label": "Vendor Registration",
        "required_fields": ["full_name", "email", "phone", "company"],
    },
}


def get_template(template_id: str) -> dict:
    return TEMPLATES.get(template_id, TEMPLATES["contact_intake"])
