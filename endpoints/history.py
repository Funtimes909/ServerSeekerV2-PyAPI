from fastapi import HTTPException
from psycopg.rows import class_row

import utils.database as database
import utils.models as models

def run(
        player: str = None,
        address: str = None,
        offset: int = None,
        limit: int = None
):
    if player and address:
        raise HTTPException(status_code=422, detail="You can't use both player and address!")
    elif not player and not address:
        raise HTTPException(status_code=400, detail="You have to provide either an address or a player!")

    conn = database.pool.getconn()
    cur = conn.cursor(row_factory=class_row(models.History))

    if player:
        option = player
        query = f"SELECT * FROM playerhistory WHERE playername = %s ORDER BY lastseen DESC LIMIT %s OFFSET %s"
    elif address:
        option = address
        query = f"SELECT * FROM playerhistory WHERE address = %s ORDER BY lastseen DESC LIMIT %s OFFSET %s"

    playerhistory = cur.execute(query, (option,limit,offset), prepare=True).fetchall()

    database.pool.putconn(conn = conn)

    def output(serverid):
        server = playerhistory[serverid]
        return {"address": server.address, "playername": server.playername, "playeruuid": server.playeruuid,
                "lastseen": server.lastseen}

    length = len(playerhistory)
    json_output = []

    for i in range(length):
        if not json_output:
            json_output = [output(i)]
        elif json_output:
            json_output.append(output(i))
    return json_output