import streamlit as st
import asyncio
import websockets

# Set page config
st.set_page_config(page_title="Chat App", page_icon="💬", layout="wide")

st.title("💬 Python Full-Stack Chat App")

# Input for username
username = st.text_input("Enter your username:")

# Message input
message = st.text_input("Type your message:")

# Button to send message
send_button = st.button("Send")

# Display area for chat messages
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

chat_container = st.container()

async def send_message(msg):
    uri = "ws://localhost:8000/ws"  # Your FastAPI WebSocket endpoint
    async with websockets.connect(uri) as websocket:
        await websocket.send(msg)
        response = await websocket.recv()
        return response

if send_button and username and message:
    # Add message locally first
    st.session_state.chat_history.append(f"{username}: {message}")
    
    # Send message to WebSocket server
    try:
        response = asyncio.run(send_message(f"{username}: {message}"))
        st.session_state.chat_history.append(f"Server: {response}")
    except Exception as e:
        st.error(f"Error sending message: {e}")

# Display chat history
with chat_container:
    for msg in st.session_state.chat_history:
        st.write(msg)
