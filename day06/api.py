from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="Day 6 DevOps API",
    version="1.0.0",
)


class ServerRequest(BaseModel):
    hostname: str
    cpu: float
    memory: float
    disk: float


@app.get("/")
def home():
    return {
        "message": "Day 6 API running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/server/check")
def check_server(server: ServerRequest):
    metrics = {
        "cpu": server.cpu,
        "memory": server.memory,
        "disk": server.disk,
    }

    alerts = []

    for metric, value in metrics.items():
        if value < 0 or value > 100:
            raise HTTPException(
                status_code=400,
                detail=f"{metric} must be between 0 and 100",
            )

        if value >= 80:
            alerts.append(metric)

    return {
        "hostname": server.hostname,
        "status": "alert" if alerts else "healthy",
        "alerts": alerts,
        "metrics": metrics,
    }