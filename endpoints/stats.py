from psycopg.rows import class_row

import utils.database as database
import utils.models as models

def run():
    with database.pool.getconn() as connection:
        with connection.cursor(row_factory=class_row(models.Stats)) as cursor:
            stats = cursor.execute("SELECT COUNT(*) FROM servers").fetchone()
            return {"servers":f"{stats.count}"}