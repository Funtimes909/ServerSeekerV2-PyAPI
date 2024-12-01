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
    if player and address:
        raise HTTPException(status_code=400, detail="You can't use both player and address!")
    elif not player and not address:
        raise HTTPException(status_code=400, detail="You have to provide either an address or a player!")
    elif player and not address:
        history = cur.execute(f"SELECT address, playername, playeruuid, lastseen FROM playerhistory WHERE playername = '{player}' ORDER BY lastseen DESC", prepare=True).fetchall()
        def output(serverId):
            server = history[serverId]
            return {"address": server.address, "playername": server.playername, "playeruuid": server.playeruuid, "lastseen": server.lastseen}
        length = len(history)
        JsonOutput = []
        for i in range(length):
            if not JsonOutput:
                JsonOutput = [output(i)]
            elif JsonOutput:
                JsonOutput.append(output(i))
        return JsonOutput
    elif not player and address:
        history = cur.execute(f"SELECT address, playername, playeruuid, lastseen FROM playerhistory WHERE playerhistory.address = '{address}' ORDER BY lastseen DESC", prepare=True).fetchall()
        def output(serverId):
            server = history[serverId]
            return {"address": server.address, "playername": server.playername, "playeruuid": server.playeruuid, "lastseen": server.lastseen}
        length = len(history)
        JsonOutput = []
        for i in range(length):
            if not JsonOutput:
                JsonOutput = [output(i)]
            elif JsonOutput:
                JsonOutput.append(output(i))
        return JsonOutput
    
