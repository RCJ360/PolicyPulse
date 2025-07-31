import json

def load_emails(inbox="C:\\Users\\Admine\\OneDrive\\Desktop\\PolicyPulse\\sample_emails.json"):
    """Load mock emails from a local JSON file."""
    with open(inbox, "r") as f:
        emails = json.load(f)
    return emails

def get_email_by_id(email_id, emails):
    """Fetch a single email by its ID."""
    for email in emails:
        if email["id"] == email_id:
            return email
    return None