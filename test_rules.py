import unittest
from utils.rule_engine import apply_rules

class TestRuleEngine(unittest.TestCase):

    def setUp(self):
        self.rules = {
            "forbidden_terms": ["confidential", "salary"],
            "pii_patterns": {
                "email": "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}",
                "phone": "\\b\\d{10}\\b"
            }
        }

    def test_forbidden_term_detection(self):
        text = "This document is confidential and includes salary information."
        flagged = apply_rules(text, self.rules)
        terms = [f['term'] for f in flagged if f['rule'] == 'forbidden_term']
        self.assertIn("confidential", terms)
        self.assertIn("salary", terms)

    def test_pii_email_detection(self):
        text = "Send it to john.doe@example.com for review."
        flagged = apply_rules(text, self.rules)
        emails = [f['match'] for f in flagged if f['rule'] == 'pii_pattern']
        self.assertIn("john.doe@example.com", emails)

    def test_pii_phone_detection(self):
        text = "Contact me at 9876543210."
        flagged = apply_rules(text, self.rules)
        phones = [f['match'] for f in flagged if f['rule'] == 'pii_pattern']
        self.assertIn("9876543210", phones)

    def test_no_violation(self):
        text = "This report contains only general information."
        flagged = apply_rules(text, self.rules)
        self.assertEqual(len(flagged), 0)

if __name__ == '__main__':
    unittest.main()