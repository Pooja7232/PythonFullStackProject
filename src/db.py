from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def add_user(username: str, email: str):
    response = supabase.table("users").insert(
        {"username": username, "email": email}
    ).execute()
    return response.data

def get_users():
    response = supabase.table("users").select("*").execute()
    return response.data
