from typing import Union
from fastapi import FastAPI
import psycopg

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}