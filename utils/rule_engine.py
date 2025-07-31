import re
import json

def load_rules(rule_file_path="C:\\Users\\Admine\\OneDrive\\Desktop\\PolicyPulse\\rules.json"):
    """Load policy rules from a JSON file."""
    with open(rule_file_path, "r") as f:
        rules = json.load(f)
    return rules

def apply_rules(text, rules):
    """
    Apply forbidden terms and PII patterns to the given text.
    Returns a list of flagged items with sentence, rule type, and matched term/pattern.
    """
    flagged = []
    sentences = text.split(".")  # Simple sentence splitter

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        # Check forbidden terms
        for term in rules.get("forbidden_terms", []):
            if term.lower() in sentence.lower():
                flagged.append({
                    "sentence": sentence,
                    "rule": "forbidden_term",
                    "term": term
                })

        # Check PII patterns
        for pattern_name, pattern in rules.get("pii_patterns", {}).items():
            matches = re.findall(pattern, sentence)
            for match in matches:
                flagged.append({
                    "sentence": sentence,
                    "rule": "pii_pattern",
                    "pattern": pattern_name,
                    "match": match
                })

    return flagged