from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/config")
def config():
    return {
        "db_host": os.getenv("DB_HOST"),
        "db_name": os.getenv("POSTGRES_DB"),
    }
