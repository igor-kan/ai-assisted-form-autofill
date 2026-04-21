import re


EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
PHONE_REGEX = re.compile(r"(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")


def extract_fields(text: str) -> dict:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    email = EMAIL_REGEX.search(text)
    phone = PHONE_REGEX.search(text)

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
    }
