from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from psycopg.rows import class_row
import psycopg

app = FastAPI()

conn = psycopg.connect("dbname=test user=fastapi password=nucceteere host=localhost")

@app.get("/stats")
def stats():
    class Stats(BaseModel):
        count: int
    cur = conn.cursor(row_factory=class_row(Stats))
    stats = cur.execute("SELECT COUNT(*) FROM servers").fetchone()
    return {"servers":f"{stats.count}"}