import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from utils.rule_engine import load_rules, apply_rules
from utils.email_loader import load_emails, get_email_by_id
from utils.scan_manager import save_scan_result, load_scan_results, get_scan_by_id

# Load data
emails = load_emails()
rules = load_rules()

st.set_page_config(page_title="PolicyPulse – Compliance Checker", layout="wide")
st.title("PolicyPulse – Internal Policy Compliance Checker")

# Sidebar for email selection
st.sidebar.header("Select Email to Scan")
email_ids = [email["id"] for email in emails]
selected_id = st.sidebar.selectbox("Choose email ID", email_ids)

# Get selected email
selected_email = get_email_by_id(selected_id, emails)
if selected_email:
    st.subheader(f" Subject: {selected_email['subject']}")
    st.write(selected_email["body"])

    if st.button("Run Policy Scan"):
        flagged = apply_rules(selected_email["body"], rules)
        scan_id = save_scan_result(selected_id, selected_email["subject"], flagged)

        if flagged:
            st.warning(" Policy Violations Detected:")
            for flag in flagged:
                if flag["rule"] == "forbidden_term":
                    st.markdown(f"- **Forbidden Term** `{flag['term']}` in: _{flag['sentence']}_")
                elif flag["rule"] == "pii_pattern":
                    st.markdown(f"- **PII Match** `{flag['pattern']}` (`{flag['match']}`) in: _{flag['sentence']}_")
        else:
            st.success("No policy violations found.")

        st.info(f"Scan ID: `{scan_id}` stored successfully.")

# Divider
st.markdown("---")
st.header(" Previous Scans")

scans = load_scan_results()
if scans:
    for scan in scans[::-1]:  # Show latest first
        with st.expander(f" {scan['subject']} – Scan ID: {scan['scanId'][:8]}..."):
            for flag in scan["flags"]:
                if flag["rule"] == "forbidden_term":
                    st.markdown(f"- **Forbidden Term** `{flag['term']}` in: _{flag['sentence']}_")
                elif flag["rule"] == "pii_pattern":
                    st.markdown(f"- **PII Match** `{flag['pattern']}` (`{flag['match']}`) in: _{flag['sentence']}_")
else:
    st.info("No scans performed yet.")