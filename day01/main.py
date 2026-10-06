
from fastapi import FastAPI
import platform
import os

app = FastAPI(title="DevOps Monitoring API")


@app.get("/")
def home():
    return {
        "message": "Welcome to my DevOps API",
        "engineer": "Sayyam Jain"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "devops-monitor"
    }


@app.get("/system")
def system_info():
    return {
        "os": platform.system(),
        "os_version": platform.release(),
        "architecture": platform.machine(),
        "current_directory": os.getcwd()
    }
