from src.db import create_complaint, get_all_complaints, update_complaint_status


def raise_complaint(username, title, description):
    create_complaint(username, title, description)
    return {"message": "Complaint raised successfully"}


def view_complaints():
    return get_all_complaints().data


def change_status(complaint_id, status):
    update_complaint_status(complaint_id, status)
    return {"message": "Status updated"}
