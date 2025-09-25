import os
from supabase import create_client
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)
# USER OPERATIONS
def create_user(username,email):
    data = {"username":username,"email":email}
    response=supabase.table("users").insert(data).execute()
    return response
def get_user(user_id):
    response=supabase.table("users").select("*").eq("id",user_id).single().execute()
    return response
def update_user(user_id,username=None,email=None,status=None):
    updates={}
    if username:
        updates["username"]=username
    if email:
        updates["email"]=email
    if status:
        updates["status"]=status
    response=supabase.table("users").update(updates).eq("id",user_id).execute()
    return response
def delete_user(user_id):
    response=supabase.table("users").delete().eq("id",user_id).execute()
    return response
# FRIEND OPERATIONS
def add_friend(user_id, friend_id):
    data={"user_id":user_id,"friend_id":friend_id}
    response=supabase.table("friends").insert(data).execute()
    return response
def get_friends(user_id):
    response=supabase.table("friends").select("*").eq("user_id",user_id).execute()
    return response
def remove_friend(friend_relation_id):
    response=supabase.table("friends").delete().eq("id",friend_relation_id).execute()
    return response
# MESSAGE OPERATIONS
def send_message(from_uid,to_uid,message_text):
    data={"from_uid":from_uid,"to_uid":to_uid,"message_text":message_text}
    response=supabase.table("messages").insert(data).execute()
    return response
def get_messages(from_uid,to_uid):
    response=supabase.table("messages").select("*").or_(f"and(from_uid.eq.{from_uid},to_uid.eq.{to_uid}),and(from_uid.eq.{to_uid},to_uid.eq.{from_uid})").order("sent_dt",desc=True).execute()
    return response
def update_message(message_id,message_text):
    response=supabase.table("messages").update({"message_text": message_text}).eq("id",message_id).execute()
    return response
def delete_message(message_id):
    response=supabase.table("messages").delete().eq("id",message_id).execute()
    return response