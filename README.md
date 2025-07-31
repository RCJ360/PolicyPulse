# PolicyPulse – Internal Policy Compliance Checker

> A Streamlit-based rule engine to scan emails or documents for internal policy violations and PII data exposure.

---

## Overview

**PolicyPulse** helps teams automatically flag potential internal compliance violations in text content such as emails or uploaded documents.

It uses a **rule-based engine** to detect:
- Forbidden terms (like "confidential", "salary", "internal use only")
- Personally Identifiable Information (PII) such as phone numbers, email addresses, and SSNs

Built using:
- Python
- Streamlit (for UI)
- spaCy + Regex (for NLP and pattern matching)
- Free & open-source tools only (as required)

---

## Features

- View and scan sample email inbox
- Highlight policy violations with detailed flags
- Save and view previous scans
- Detect both keyword-based and regex-based patterns
- Unit test support for rule logic
- Fully documented and prompt-logged

---

## Project Structure

PolicyPulse/
├── app.py
├── rules/
│   └── rules.json
├── data/
│   └── scan_results.json
├── sample_emails.json    
├── utils/
│   ├── rule_engine.py
│   ├── email_loader.py
│   └── scan_manager.py
├── test_rules.py
│   
├── README.md
└── prompt_log.md

---

## How to Run:

1. Install dependencies:
   pip install -r requirements.txt

2. Start the app:
   streamlit run app.py

3. Run tests:
   python -m unittest discover tests

---

## Rule Format:

rules.json:
{
  "forbidden_terms": ["confidential", "salary"],
  "pii_patterns": {
    "email": "[EMAIL_REGEX]",
    "phone": "[PHONE_REGEX]"
  }
}

---

## Sample Email Format:

{
  "id": "email_001",
  "subject": "Monthly Report",
  "body": "Please send your salary details to hr@example.com."
}

---

## Prompt Log (AI Help Used):

- "Create a rule engine that applies regex and forbidden terms to text"
- "Generate Streamlit UI that scans text and shows flagged terms"
- "Write unit tests for rule-based scanning logic in Python"

---

## Screenshots:

Screenshots of app for your refernce Added (Screenshots Folder).

---

## Author:

Rupak C. Jogi – Applied for AI/ML Intern