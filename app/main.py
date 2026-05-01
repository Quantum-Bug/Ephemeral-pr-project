from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    pr_number = os.getenv("PR_NUMBER", "Local")
    return{
            "message": f"Welcome to Company XYZ",
            "environment": f"PR-{pr_number}"
            }
# app/main.py
@app.get("/")
def read_root():
    return {
        "status": "Success",
        "message": "This is running in a local ephemeral environment!",
        "pr_number": os.getenv("PR_NUMBER", "unknown")
    }