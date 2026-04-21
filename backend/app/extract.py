import re


EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
PHONE_REGEX = re.compile(r"(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
COMPANY_REGEX = re.compile(r".*(inc|corp|corporation|ltd|llc).*", re.IGNORECASE)


def extract_fields(text: str) -> dict:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    email = EMAIL_REGEX.search(text)
    phone = PHONE_REGEX.search(text)
    company = next((line for line in lines if COMPANY_REGEX.match(line)), "")
    address = lines[-1] if len(lines) > 1 else ""

    candidate_name = ""
    if lines:
        candidate_name = lines[0]

    return {
        "full_name": {
            "value": candidate_name,
            "confidence": 0.65 if candidate_name else 0.0,
        },
        "email": {
            "value": email.group(0) if email else "",
            "confidence": 0.95 if email else 0.0,
        },
        "phone": {
            "value": phone.group(0) if phone else "",
            "confidence": 0.9 if phone else 0.0,
        },
        "company": {
            "value": company,
            "confidence": 0.78 if company else 0.0,
        },
        "address": {
            "value": address,
            "confidence": 0.58 if address else 0.0,
        },
    }
