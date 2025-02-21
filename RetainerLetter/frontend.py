import streamlit as st
import requests

API_URL = "http://localhost:8000/generate_retainer"

st.title("Retainer Letter Generator")

firm_name = st.text_input("Firm Name")
firm_address = st.text_input("Firm Address")
firm_phone = st.text_input("Firm Phone Number")
firm_email = st.text_input("Firm Email")
firm_website = st.text_input("Firm Website")
firm_lead = st.text_input("Firm Lead Partner")

client_name = st.text_input("Client Name")
client_address = st.text_input("Client Address")
contact_name = st.text_input("Contact Name")
contact_phone = st.text_input("Contact Phone Number")
contact_email = st.text_input("Contact Email")

existing_relationship = st.radio("Existing Relationship?", options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
initial_meeting_notes = st.text_area("Initial Meeting Notes")
scope = st.text_area("Scope")
billing_type = st.selectbox("Billing Type", ["Hourly", "Fixed", "Retainer"])
partner_rate = st.text_input("Partner Rate")
associate_rate = st.text_input("Associate Rate")
student_rate = st.text_input("Student Rate")
frequency = st.selectbox("Billing Frequency", ["Monthly", "Quarterly", "Annually"])
retainer_amount = st.text_input("Retainer Amount")
late_fee = st.text_input("Late Fee (%)")
jurisdiction = st.text_input("Jurisdiction")

dispute_clause = st.checkbox("Include Dispute Resolution Clause")
confidentiality_clause = st.checkbox("Include Confidentiality Clause")

if st.button("Generate Retainer Letter"):
    payload = {
        "FirmName": firm_name,
        "FirmAddress": firm_address,
        "FirmPhoneNumber": firm_phone,
        "FirmEmail": firm_email,
        "FirmWebsite": firm_website,
        "FirmLeadPartner": firm_lead,
        "ClientName": client_name,
        "ClientAddress": client_address,
        "ContactName": contact_name,
        "ContactPhoneNumber": contact_phone,
        "ContactEmail": contact_email,
        "ExistingRelationship": existing_relationship,
        "InitialMeetingNotes": initial_meeting_notes,
        "Scope": scope,
        "BillingType": billing_type,
        "PartnerRate": partner_rate,
        "AssociateRate": associate_rate,
        "StudentRate": student_rate,
        "Frequency": frequency,
        "RetainerAmount": retainer_amount,
        "LateFeePercent": late_fee,
        "Jurisdiction": jurisdiction,
        "DisputeResolutionClause": int(dispute_clause),
        "ConfidentialityClause": int(confidentiality_clause)
    }

    with st.spinner("Processing..."):
        response = requests.post(API_URL, json=payload, stream=True)
        
        status_box = st.empty()
        for line in response.iter_lines(decode_unicode=True):
            status_box.markdown(f"**Status:** {line}")

        st.success("Retainer Letter Generated.")
