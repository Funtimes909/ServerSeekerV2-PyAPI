from psycopg.rows import class_row

import database
import models


def history(player: str = None, address: str = None, offset: int = None, limit: int = None):
    """
    Get the history of a player or server.
    - **player**: The player name you want to see history for. Incompatible with address.
    - **address**: The address you want to see history for. Incompatible with player.
    - **offset**: Offset from where to start the sear
    \f
    :param player: Player name to search history for.
    :param address: Address to search history for.
    :param offset: Offset from where to start the search.
    :param X-Auth-Key: The api token to identify yourself or your application.
    """

    conn = database.pool.getconn()
    cur = conn.cursor(row_factory=class_row(models.History))

    if player:
        option = player
        query = f"SELECT * FROM playerhistory WHERE playername = %s ORDER BY lastseen DESC LIMIT %s OFFSET %s"
    elif address:
        option = address
        query = f"SELECT * FROM playerhistory WHERE address = %s ORDER BY lastseen DESC LIMIT %s OFFSET %s"

    playerhistory = cur.execute(query, (option,limit,offset), prepare=True).fetchall()

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