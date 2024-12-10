from psycopg.rows import class_row

import database
import models

def run():
    conn = database.pool.getconn()
    cur = conn.cursor(row_factory=class_row(models.Stats))
    stats = cur.execute("SELECT COUNT(*) FROM servers").fetchone()
    database.pool.putconn(conn = conn)
    return {"servers":f"{stats.count}"}