# app.py

import streamlit as st
import re
from chatbot_engine import generate_questions, filter_to_only_selected_techs

st.set_page_config(page_title="TalentScout AI Hiring Assistant", layout="centered")

# ---------------------
# Header and Greeting
# ---------------------
st.title("👩‍💻 TalentScout AI Hiring Assistant")
st.markdown("Welcome! I'm here to help with your initial screening process. Please fill out your details below to begin.")

# ---------------------
# Candidate Form
# ---------------------
with st.form("candidate_form"):
    full_name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.slider("Years of Experience", 0, 30, 1)
    position = st.text_input("Desired Position(s)")
    location = st.text_input("Current Location")
    tech_stack = st.text_area("Tech Stack (comma-separated)", placeholder="e.g., Python, Django, MySQL, React")

    # Two buttons instead of one
    col1, col2 = st.columns(2)
    with col1:
        submitted = st.form_submit_button("Submit")
    with col2:
        exited = st.form_submit_button("Exit")

# ---------------------
# After Form Submission
# ---------------------

# ---------------------
# After Form Submission
# ---------------------
# ✅ Exit button behavior
if exited:
    st.warning("👋 Thanks for visiting TalentScout! Wishing you the best in your journey.")
    st.stop()

# ✅ Submit button behavior
if submitted:
    # Validate required fields
    if not full_name.strip() or not email.strip() or not tech_stack.strip():
        st.error("❌ Please fill in your Full Name, Email, and Tech Stack before submitting.")
    else:
        st.success("✅ Form submitted successfully!")
        st.write("Here’s what you entered:")
        st.write(f"**Full Name:** {full_name}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone:** {phone}")
        st.write(f"**Experience:** {experience} years")
        st.write(f"**Position:** {position}")
        st.write(f"**Location:** {location}")
        st.write(f"**Tech Stack:** {tech_stack}")

        st.subheader("📌 Technical Questions Based on Your Tech Stack")

        # Clean up tech stack
        tech_stack_clean = re.sub(r"[.;]+", ",", tech_stack)

        # Generate + filter
        with st.spinner("Generating questions..."):
            raw_questions = generate_questions(tech_stack_clean)
            questions = filter_to_only_selected_techs(raw_questions, tech_stack_clean)

        if questions:
            st.markdown(questions)
        else:
            st.error("No questions generated.")

        # Save to CSV
        import csv
        from datetime import datetime
        import os

        log_file = "data/logs.csv"
        os.makedirs("data", exist_ok=True)

        candidate_data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "experience": experience,
            "position": position,
            "location": location,
            "tech_stack": tech_stack_clean
        }

        file_exists = os.path.isfile(log_file)
        with open(log_file, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=candidate_data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(candidate_data)

        st.success("📝 Candidate information saved to logs.csv!")
