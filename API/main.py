# api/main.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from src.logic import ConnectionManager
from src import db

app = FastAPI()
manager = ConnectionManager()

@app.get("/")
async def home():
    return {"message": "Chat server is running 🚀"}

@app.get("/messages")
async def get_messages():
    return db.get_messages()

@app.get("/users")
async def get_users():
    return db.get_users()

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket, username)
    await manager.broadcast(f"📢 {username} joined the chat", "System")

    try:
        while True:
            data = await websocket.receive_text()
            db.save_message(username, data)
            await manager.broadcast(data, username)
    except WebSocketDisconnect:
        manager.disconnect(websocket, username)
        await manager.broadcast(f"❌ {username} left the chat", "System")
