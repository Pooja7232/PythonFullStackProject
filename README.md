# Chat Application
A chat application is a simple software that enables users to send and receive instant messages in real time. It allows people to communicate quickly and easily through text, supporting one-on-one or group conversations. The app manages users, messages, and connections, providing a platform for seamless communication over the internet.
## Key Features
1. **Real-time Messaging:** Instant sending and receiving of text messages with minimal delay.
2. **User Authentication:** Secure login/signup to manage user identities.
3. **Online Presence and Status:** Show if users are online, offline, or typing.
4. **Group Chats:** Support for multiple users to communicate in one space.
5. **Rich Media Sharing:** Ability to send images, videos, files, and voice notes.
6. **Notifications:** Alerts for incoming messages or mentions, even when app is closed.
7. **Message History and Search:** Store and retrieve past conversations with search capability.
8. **Read Receipts and Typing Indicators:** Show when messages are read or if someone is typing.
9. **Encryption and Security:** Protect user privacy through end-to-end encryption.
10. **Customization:** Themes, emojis, stickers, and profile personalization.
11. **Cross-Platform Support:** Sync chats across devices like mobile, web, and desktop.
## Project Structure
ChatApplication/
|
|---src/          #core application logic
|    |---logic.py #Business logic and task
operations
|    |__db.py     #Database operations
|
|----api/         #Backend API
|    |__main.py   #FastAPI endpoints
|
|----frontend/    #Frontend application
|     |__app.py   #Streamlit web interface
|
|____requirements.txt #Python Dependencies
|
|____README.md    #Project documentation
|
|____.env         #Python Variables
## Quick Start
### Prerequisites
-Python 3.8 or higher
-A Supabase account
-GIT(Push,cloning)
### 1.Clone or Download the Project
# Option 1: Clone with Git
git clone [<repository-url>](https://github.com/Pooja7232/PythonFullStackProject.git)
# Option 2: Download and extract the ZIP file
### 2.Install Dependencies
# Install all required Python Packages
pip install -r requirements.txt
### 3. Set Up Supabase Database
1.Create a Supabse Projects:
2.Create the Users Table:
- Go to the SQL Editor in your Supabse dashboard
-Run this SQL command
``` sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    status VARCHAR(10) DEFAULT 'Active',
    authentication_time DATETIME DEFAULT CURRENT_TIMESTAMP
);
```
3. **Get Your Credentials:
### 4. Configure Environment Variables
1. Create a `.env` file in the project root
2. Add your Supabase credentials to `.env`:
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here
**Example:**
SUPABASE_URL="https://ddfyosxkgjjdddzsdswp.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRkZnlvc3hrZ2pqZGRkenNkc3dwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODIzMTgsImV4cCI6MjA3MzY1ODMxOH0.LXAQWqEUDekJYNoI_jlFDnmUIVs_jrTcmNlFzC9tETQ"
### 5. Run the Application
## Streamlit Frontend
streamlit run frontend/app.py
## FastAPI Backend
cd api
python main.py
The API will be available at 
Here is the README.md text including sections for "How to Use" and "Technical Details" based on earlier content and good documentation practices:text
## How to Use
- Register a new user through the frontend interface.
- Add friends using their usernames or emails.
- Select a friend or group to initiate a chat.
- Send and receive messages in real-time via the chat interface.
- View message history and status indicators such as read/unread and typing.
- Receive notifications for new messages even when the app is minimized.
## Technical Details
### Technologies Used
- **Frontend:** Streamlit (Python web framework for UI)
- **Backend:** FastAPI (Python REST API framework)
- **Database:** Supabase (PostgreSQL-based Backend-as-a-Service)
- **Programming Language:** Python 3.8+
- **Environment:** `.env` file to securely store Supabase credentials and other configuration
### Key Components
- **`src/db.py`:** Handles database CRUD operations.  
- **`src/logic.py`:** Contains business logic and chat functionalities.  
- **`api/main.py`:** Defines FastAPI routes and endpoints.  
- **`frontend/app.py`:** Streamlit interface for user interaction.
## Common Issues & Troubleshooting
- Streamlit UI state issues—use session state properly.  
- Resource limits on deployment—cache heavy operations if needed.  
- Deployment inconsistencies—use logging for diagnosis.  
- Backend concurrency—handle race conditions carefully.
## Future Enhancements
- Group chats  
- Media sharing (images, videos, voice notes, files)  
- Message reactions  
- Read receipts and typing indicators  
- Voice and video calling  
- Chatbots and AI integration  
- Search functionality  
- Message editing and deletion  
- Push notifications  
- User profiles with avatars and privacy settings  
- End-to-end encryption  
- Admin panel for moderation and analytics  
- Cross-platform support for mobile and desktop  
- Cloud sync for multiple devices  
## Support
If you encounter any issues or have questions:
- phone no:7032512204
- email:23b81a7232@cvr.ac.in