from psycopg_pool import ConnectionPool

import const

pool = ConnectionPool(
    conninfo=f"dbname={const.DATABASE_NAME} user={const.DATABASE_USER} password={const.DATABASE_PASSWORD} host={const.DATABASE_HOST} port={const.DATABASE_PORT}",
    min_size=1,
    max_size=50,
    open=True
)