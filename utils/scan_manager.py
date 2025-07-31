import json
import uuid
import os

SCAN_RESULTS_FILE = "data/scan_results.json"

def load_scan_results():
    """Load all scan results from the local JSON file."""
    if not os.path.exists(SCAN_RESULTS_FILE):
        return []

    with open(SCAN_RESULTS_FILE, "r") as f:
        return json.load(f)

def save_scan_result(email_id, subject, flagged_items):
    """Save a new scan result with a unique scan ID."""
    scan_id = str(uuid.uuid4())
    scan_entry = {
        "scanId": scan_id,
        "emailId": email_id,
        "subject": subject,
        "flags": flagged_items
    }

    scans = load_scan_results()
    scans.append(scan_entry)

    with open(SCAN_RESULTS_FILE, "w") as f:
        json.dump(scans, f, indent=4)

    return scan_id

def get_scan_by_id(scan_id):
    """Retrieve a scan result by its scanId."""
    scans = load_scan_results()
    for scan in scans:
        if scan["scanId"] == scan_id:
            return scan
    return None