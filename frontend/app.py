# frontend/app.py
import tkinter as tk
import threading
import asyncio
import websockets

SERVER_URL = "ws://localhost:8000/ws"

class ChatClient:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title(f"Chat - {username}")

        # Chat display area
        self.text_area = tk.Text(root, state="disabled", width=60, height=20)
        self.text_area.pack(padx=10, pady=10)

        # Input box
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(side="left", padx=(10, 0), pady=(0, 10))
        self.entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(side="right", padx=(0, 10), pady=(0, 10))

        # WebSocket connection
        self.loop = asyncio.new_event_loop()
        threading.Thread(target=self.start_async_loop, daemon=True).start()

    def start_async_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.connect())

    async def connect(self):
        uri = f"{SERVER_URL}/{self.username}"
        async with websockets.connect(uri) as ws:
            self.ws = ws
            while True:
                try:
                    msg = await ws.recv()
                    self.display_message(msg)
                except:
                    break

    def send_message(self, event=None):
        message = self.entry.get().strip()
        if message and hasattr(self, "ws"):
            asyncio.run_coroutine_threadsafe(self.ws.send(message), self.loop)
            self.entry.delete(0, tk.END)

    def display_message(self, message):
        self.text_area.config(state="normal")
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.config(state="disabled")
        self.text_area.see(tk.END)

if __name__ == "__main__":
    username = input("Enter your username: ")
    root = tk.Tk()
    client = ChatClient(root, username)
    root.mainloop()
