import os
from fastapi import FastAPI

app = FastAPI(title="TFG Backend")

DATABASE_URL = os.getenv("DATABASE_URL")


@app.get("/")
def read_root():
    return {"status": "ok", "service": "backend"}


@app.get("/health")
def health():
    return {"status": "healthy", "database": DATABASE_URL is not None}
