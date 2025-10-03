# src/logic.py
from typing import List
from fastapi import WebSocket
from src import db

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections.append(websocket)
        db.add_user(username)

    def disconnect(self, websocket: WebSocket, username: str):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        db.remove_user(username)

    async def broadcast(self, message: str, username: str = "System"):
        db.save_message(username, message)
        for connection in self.active_connections:
            await connection.send_text(f"{username}: {message}")

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(f"You: {message}")
