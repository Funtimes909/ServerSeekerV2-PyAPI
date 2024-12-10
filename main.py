from typing import Annotated
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Header

import endpoints.history
from key_check import check
from psycopg.rows import class_row
import models
import responses
import subprocess
import database
load_dotenv()

def commit_short() -> str:
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()

def branch() -> str:
    return subprocess.check_output(['git', 'branch', '--show-current']).decode('ascii').strip()

description = "ServerSeekerV2 API implemented in Python <br> Maintained by [Nucceteere](https://github.com/EngurRuzgar)"

app = FastAPI(
    title="ServerSeekerV2 API",
    description=description,
    version=f"{commit_short()} @ {branch()}",
    contact={
        "name": "Nucceteere",
        "email": "ruzgar@nucceteere.xyz",
    },
    license_info={
        "name": "GPLv3",
        "url": "https://www.gnu.org/licenses/gpl-3.0.txt",
    },
    docs_url="/docs",
    redoc_url=None
)

conn = database.pool.getconn()
gcur = conn.cursor(row_factory=class_row(models.Key))
keyTable = ("CREATE TABLE IF NOT EXISTS api_keys ("
            "ID int,"
            "APIKey varchar(255) NOT NULL UNIQUE,"
            "PRIMARY KEY (ID))")

gcur.execute(keyTable)
conn.commit()

keyQuery = gcur.execute("SELECT APIKey FROM api_keys").fetchall()
keys = check(keyQuery)

@app.get("/stats", responses=responses.stats, operation_id="stats")
def stats():
    """
    Get the stats for ServerSeekerV2
    """
    cur = conn.cursor(row_factory=class_row(models.Stats))
    stats = cur.execute("SELECT COUNT(*) FROM servers").fetchone()
    return {"servers":f"{stats.count}"}

@app.get("/history", responses=responses.history, operation_id="history")
def history(player: str = None, address: str = None, offset: int = None, x_auth_key: Annotated[str | None, Header()] = None):
    if not x_auth_key or x_auth_key not in keys:
        raise HTTPException(status_code=401)
    if player and address:
        raise HTTPException(status_code=422, detail="You can't use both player and address!")
    elif not player and not address:
        raise HTTPException(status_code=400, detail="You have to provide either an address or a player!")

    return endpoints.history.history(player=player, address=address, offset=offset)

# @app.get("/random")
# def random():
#     cur = conn.cursor()
#     random = cur.execute("SELECT * FROM servers LEFT JOIN playerhistory ON servers.address = playerhistory.address AND servers.port = playerhistory.port LEFT JOIN mods ON servers.address = mods.address AND servers.port = mods.port ORDER BY RANDOM() LIMIT 1").fetchone()
