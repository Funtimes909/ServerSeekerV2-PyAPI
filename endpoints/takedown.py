import utils.database as database

def run(address: str):
    conn = database.pool.getconn()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM servers WHERE address = %s", (address,), prepare=True)
    conn.commit()
    database.pool.putconn(conn)
    return {"success": True}