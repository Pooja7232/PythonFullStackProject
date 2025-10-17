from fastapi import FastAPI, Form
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.post("/chat/")
async def chat(username: str = Form(...), message: str = Form(...)):
    # Insert username and message into 'chatapp' table
    response = supabase.table("chatapp").insert(
        {"username": username, "message": message}
    ).execute()

    if response.status_code != 201:
        return {"status": "error", "message": "Failed to save message"}

    # Respond to the user (could be extended to AI response)
    return {"status": "success", "response": f"Received message from {username}"}