from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import models
from os import getenv
from pydantic import BaseModel
from psycopg.rows import class_row
import psycopg
load_dotenv()

app = FastAPI()

try:
    conn = psycopg.connect(f"dbname={getenv("DBNAME")} user={getenv("USERNAME")} password={getenv("PASSWORD")} host={getenv("HOST")} port={getenv("PORT")}")
except:
    raise ConnectionRefusedError("Database can't be reached!")
    
@app.get("/stats")
def stats():
    cur = conn.cursor(row_factory=class_row(models.Stats))
    stats = cur.execute("SELECT COUNT(*) FROM servers").fetchone()
    return {"servers":f"{stats.count}"}

# @app.get("/random")
# def random():
#     cur = conn.cursor()
#     random = cur.execute("SELECT * FROM servers LEFT JOIN playerhistory ON servers.address = playerhistory.address AND servers.port = playerhistory.port LEFT JOIN mods ON servers.address = mods.address AND servers.port = mods.port ORDER BY RANDOM() LIMIT 1").fetchone()

@app.get("/history")
def PlayerHistory(player: str = None, address: str = None):
    cur = conn.cursor(row_factory=class_row(models.History))
    if player != None and address != None:
        raise HTTPException(status_code=400, detail="You can't use both player and address!")
    elif player == None and address == None:
        raise HTTPException(status_code=400, detail="You have to provide either an address or a player!")
    elif player != None and address == None:
        history = cur.execute(f"SELECT address, playername, playeruuid, lastseen FROM playerhistory WHERE playername = '{player}' ORDER BY lastseen DESC", prepare=True).fetchall()
    elif player == None and address != None:
        history = cur.execute(f"SELECT address, playername, playeruuid, lastseen FROM playerhistory WHERE playerhistory.address = '{address}' ORDER BY lastseen DESC", prepare=True).fetchall()
        return {
                "address":f"{history[0].address}",
                "playername":f"{history[0].playername}",
                "playeruuid":f"{history[0].playeruuid}",
                "lastseen":f"{history[0].lastseen}"
            }
    