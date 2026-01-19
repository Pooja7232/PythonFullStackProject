from fastapi import FastAPI
from pydantic import BaseModel
from src.logic import raise_complaint, view_complaints, change_status

app = FastAPI()


class Complaint(BaseModel):
    username: str
    title: str
    description: str


class StatusUpdate(BaseModel):
    complaint_id: int
    status: str


@app.get("/")
def root():
    return {"message": "Complaint Tracking API is running"}


@app.post("/complaint")
def create(complaint: Complaint):
    return raise_complaint(
        complaint.username,
        complaint.title,
        complaint.description
    )


@app.get("/complaints")
def read_all():
    return view_complaints()


@app.put("/complaint/status")
def update(status: StatusUpdate):
    return change_status(status.complaint_id, status.status)
