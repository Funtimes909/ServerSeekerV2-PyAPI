from dotenv import load_dotenv
from fastapi import FastAPI
from os import getenv
from pydantic import BaseModel
from psycopg.rows import class_row
import psycopg
load_dotenv()

app = FastAPI()

try:
    conn = psycopg.connect(f"dbname={getenv("DBNAME")} user={getenv("USERNAME")} password={getenv("PASSWORD")} host={getenv("HOST")} port={getenv("PORT")}")
except:
    raise ConnectionError("Database can't be reached!")
    
@app.get("/stats")
def stats():
    class Stats(BaseModel):
        count: int
    cur = conn.cursor(row_factory=class_row(Stats))
    stats = cur.execute("SELECT COUNT(*) FROM servers").fetchone()
    return {"servers":f"{stats.count}"}