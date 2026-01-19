from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def create_complaint(username, title, description):
    return supabase.table("complaints").insert({
        "username": username,
        "title": title,
        "description": description
    }).execute()


def get_all_complaints():
    return supabase.table("complaints").select("*").order("created_at", desc=True).execute()


def update_complaint_status(complaint_id, status):
    return supabase.table("complaints").update({
        "status": status
    }).eq("id", complaint_id).execute()
