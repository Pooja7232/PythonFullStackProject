import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("🚨 Complaint Tracking System")

menu = ["Raise Complaint", "View Complaints (Admin)"]
choice = st.sidebar.selectbox("Menu", menu)


if choice == "Raise Complaint":
    st.subheader("Raise a Complaint")

    username = st.text_input("Username")
    title = st.text_input("Complaint Title")
    description = st.text_area("Complaint Description")

    if st.button("Submit"):
        res = requests.post(
            f"{API_URL}/complaint",
            json={
                "username": username,
                "title": title,
                "description": description
            }
        )
        st.success("Complaint submitted successfully")


elif choice == "View Complaints (Admin)":
    st.subheader("All Complaints")

    complaints = requests.get(f"{API_URL}/complaints").json()

    for c in complaints:
        st.write(f"🆔 {c['id']} | 👤 {c['username']}")
        st.write(f"📌 {c['title']}")
        st.write(f"📝 {c['description']}")
        st.write(f"📊 Status: {c['status']}")

        new_status = st.selectbox(
            "Update Status",
            ["Open", "In Progress", "Resolved"],
            key=c["id"]
        )

        if st.button("Update", key=f"btn{c['id']}"):
            requests.put(
                f"{API_URL}/complaint/status",
                json={
                    "complaint_id": c["id"],
                    "status": new_status
                }
            )
            st.success("Status updated")
            st.experimental_rerun()

        st.divider()
