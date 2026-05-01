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
