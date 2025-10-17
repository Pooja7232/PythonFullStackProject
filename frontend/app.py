import streamlit as st
import requests

st.title("Chat Application")

username = st.text_input("Enter username")
message = st.text_area("Enter message")

if st.button("Send"):
    if not username or not message:
        st.warning("Please enter both username and message")
    else:
        with st.spinner("Sending message..."):
            res = requests.post("http://127.0.0.1:8000/chat/", data={"username": username, "message": message})
            if res.status_code == 200:
                data = res.json()
                if data["status"] == "success":
                    st.success(data["response"])
                else:
                    st.error(data["message"])
            else:
                st.error("Error communicating with backend")
