# Complaint / Issue Tracking System
A Complaint / Issue Tracking System is a software application that allows users to raise complaints or issues and track their resolution status. It helps organizations efficiently manage, monitor, and resolve issues reported by users, ensuring transparency and accountability. The system supports registering complaints, updating statuses, and viewing complaint history through a centralized platform.
## Key Features
1. **Complaint Registration:** Users can submit complaints with title and description.

2. **Status Tracking:** Track complaint status such as Open, In Progress, and Resolved.

3. **User Identification:** Complaints are linked to registered users.

4. **Admin Management:** Admin can view and update all complaints.

5. **Real-time Updates:** Status changes are reflected instantly.

6. **Complaint History:** View previously raised complaints.

7. **Search and Filtering:** Find complaints based on status or user.

8. **Secure Data Storage:** Data stored securely using Supabase.

9. **Simple UI:** User-friendly interface built with Streamlit.

10. **Scalable Backend:** FastAPI-based RESTful backend.

11. **Cross-Platform Access:** Accessible via web on any device.

## Project Structure
ComplaintTrackingSystem/
|
|---src/        #core application logic
| |---logic.py  #business logic for complaints
| |__db.py      #database operations
|
|----api/       #backend API
| |__main.py    #FastAPI endpoints
|
|----frontend/  #frontend application
| |__app.py     #Streamlit web interface
|
|____requirements.txt # Python dependencies
|
|____README.md  #Project documentation
|
|____.env       #Environment variables
## Quick Start
### Prerequisites
-Python 3.8 or higher
-A Supabase account
-GIT (for push and cloning)
### 1.Clone or Download the Project
# Option 1: Clone with Git
git clone https://github.com/Pooja7232/PythonFullStackProject.git
# Option 2: Download and extract the ZIP file
### 2.Install Dependencies
# Install all required Python packages
pip install -r requirements.txt
### 3.Set Up Supabase Database
1.Create a Supabase project
2.Create the Complaints Table
- Go to the SQL Editor in your Supabase dashboard
-Run this SQL command
``` sql
CREATE TABLE complaints (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    title VARCHAR(100),
    description TEXT,
    status VARCHAR(20) DEFAULT 'Open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
3. **Get Your Credentials**
### 4. Configure Environment Variables
1. Create a .env file in the project root
2. Add your Supabase credentials to .env
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here
**Example:**
SUPABASE_URL="https://ddfyosxkgjjdddzsdswp.supabase.co"
SUPABASE_KEY="your_supabase_anon_key_here"
### 5. Run the Application
## Streamlit Frontend
streamlit run frontend/app.py
## FastAPI Backend
cd api
python main.py
The API will be available at http://127.0.0.1:8000
## How to Use
- Register or enter your username in the frontend.
- Submit a new complaint with title and description.
- View the submitted complaint and its status.
- Admin can update the complaint status.
- Users can track complaint resolution progress.
- View complaint history anytime.
## Technical Details
### Technologies Used
- **Frontend:** Streamlit (Python web framework for UI)
- **Backend:** FastAPI (Python REST API framework)
- **Database:** Supabase (PostgreSQL-based Backend-as-a-Service)
- **Programming Language:** Python 3.8+
- **Environment:** `.env` file to securely store Supabase credentials
### Key Components
- **`src/db.py`:** Handles database CRUD operations
- **`src/logic.py`:** Contains complaint business logic
- **`api/main.py`:** Defines FastAPI routes and endpoints
- **`frontend/app.py`:** Streamlit interface for user interaction
## Common Issues & Troubleshooting
- Backend not running: Ensure FastAPI server is started before frontend.
- Connection refused error: Check API URL and port number.
- Supabase errors: Verify Supabase URL and key in .env.
- Streamlit UI issues: Use session state correctly.
## Future Enhancements
- User authentication and login system
- Admin dashboard with role-based access
- Complaint categories and priority levels
- File uploads for complaint evidence
- Email and SMS notifications
- Analytics and reports
- Mobile application support
## Support
If you encounter any issues or have questions:
- phone no: 70........
- email: 23..................