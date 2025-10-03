# src/db.py

# In-memory storage for simplicity
messages = []   # Stores chat history
users = set()   # Active users

def save_message(username: str, message: str):
    entry = {"user": username, "message": message}
    messages.append(entry)
    return entry

def get_messages():
    return messages[-20:]  # Return last 20 messages

def add_user(username: str):
    users.add(username)

def remove_user(username: str):
    users.discard(username)

def get_users():
    return list(users)
