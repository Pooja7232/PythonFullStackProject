import streamlit as st
import asyncio
import websockets
import nest_asyncio

nest_asyncio.apply()

st.title("Chat Application")

username = st.text_input("Enter your username", key="username_input")
if "messages" not in st.session_state:
    st.session_state.messages = []

async def ws_send_receive(uri, msg):
    async with websockets.connect(uri) as ws:
        await ws.send(msg)
        resp = await ws.recv()
        return resp

if username:
    user_msg = st.text_input("Your message:", key="msg_input")
    if st.button("Send") and user_msg:
        uri = f"wss://my-deployed-backend-url/ws/{username}"  # <- Update this
        try:
            resp = asyncio.run(ws_send_receive(uri, user_msg))
            st.session_state.messages.append(f"{username}: {user_msg}")
            st.session_state.messages.append(f"Server: {resp}")
        except Exception as e:
            st.error("Connection failed: " + str(e))

st.write("### Chat History:")
for m in st.session_state.messages:
    st.write(m)