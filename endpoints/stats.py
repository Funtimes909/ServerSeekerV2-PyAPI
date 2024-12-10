from psycopg.rows import class_row

import database
import models

def run():
    conn = database.pool.getconn()
    cur = conn.cursor(row_factory=class_row(models.Stats))
    stats = cur.execute("SELECT COUNT(*) FROM servers").fetchone()
    return {"servers":f"{stats.count}"}