from typing import Annotated
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Header
from utils.key_check import check
from psycopg.rows import class_row
from endpoints import stats, history, servers

import endpoints
import utils.models as models
import utils.responses as responses
import subprocess
import utils.database as database
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
    return endpoints.stats.run()


@app.get("/servers", responses=responses.servers, operation_id="servers")
def servers(
        version: str = None,
        software: str = None,
        motd: str = None,
        player: str = None,
        country: str = None,
        asn: str = None,
        org: str = None,
        hostname: str = None,
        icon: bool = None,
        prevents_reports: bool = None,
        whitelist: bool = None,
        cracked: bool = None,
        enforces_secure_chat: bool = None,
        empty: bool = None,
        full: bool = None,
        seenafter: int = None,
        seenbefore: int = None,
        onlineplayers: int = None,
        maxplayers: int = None,
        port: int = None,
        protocol: int = None,
):
    return endpoints.servers.run(
        version=version,
        software=software,
        motd=motd,
        player=player,
        country=country,
        asn=asn,
        org=org,
        hostname=hostname,
        icon=icon,
        prevents_reports=prevents_reports,
        whitelist=whitelist,
        cracked=cracked,
        enforces_secure_chat=enforces_secure_chat,
        empty=empty,
        full=full,
        seenafter=seenafter,
        seenbefore=seenbefore,
        onlineplayers=onlineplayers,
        maxplayers=maxplayers,
        port=port,
        protocol=protocol,
    )
@app.get("/history", responses=responses.history, operation_id="history")
def history(player: str = None, address: str = None, offset: int = None, limit: int = None, x_auth_key: Annotated[str | None, Header()] = None):
    """
    Get the history of a player or server.
    - **player**: The player name you want to see history for. Incompatible with address.
    - **address**: The address you want to see history for. Incompatible with player.
    - **offset**: Offset from where to start the sear
    - **limit**: Limit the amount of results returned
    \f
    :param player: Player name to search history for.
    :param address: Address to search history for.
    :param offset: Offset from where to start the search.
    :param limit: Number of results to return.
    :param X-Auth-Key: The api token to identify yourself or your application.
    """
    key_check(x_auth_key)
    return endpoints.history.run(player=player, address=address, offset=offset, limit=limit)

def key_check(x_auth_key: Annotated[str | None, Header()] = None):
    if not x_auth_key or x_auth_key not in keys:
        raise HTTPException(status_code=401, headers={"WWW-Authenticate": "X-Auth-Key"})
