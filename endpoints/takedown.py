import utils.database as database

def run(address: str):
    with database.pool.acquire() as connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM servers WHERE address = %s", (address,), prepare=True)
            connection.commit()