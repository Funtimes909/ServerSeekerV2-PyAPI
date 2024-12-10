import utils.database as database

def random():
    conn = database.pool.getconn()
    cur = conn.cursor()
    random = cur.execute("SELECT * FROM servers ORDER BY RANDOM() LIMIT 1").fetchone()
    database.pool.putconn(conn = conn)