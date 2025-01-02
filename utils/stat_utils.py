from psycopg.rows import class_row
import utils.database as database
import utils.models as models

conn = database.pool.getconn()
cur = conn.cursor(row_factory=class_row(models.Stats))

class stats():
    total = cur.execute("SELECT COUNT(*) FROM servers").fetchone()
    java = cur.execute("SELECT COUNT(*) FROM servers WHERE type = 'JAVA'").fetchone()
    class modded():
        lexforge = cur.execute("SELECT COUNT(*) FROM servers WHERE type = 'LEXFORGE'").fetchone()
        neoforge = cur.execute("SELECT COUNT(*) FROM servers WHERE type = 'NEOFORGE'").fetchone()
    class plugin():
        bukkit = cur.execute("SELECT COUNT(*) FROM servers WHERE type = 'BUKKIT'").fetchone()
        spigot = cur.execute("SELECT COUNT(*) FROM servers WHERE type = 'SPIGOT'").fetchone()
        paper = cur.execute("SELECT COUNT(*) FROM servers WHERE type = 'PAPER'").fetchone()
        purpur = cur.execute("SELECT COUNT(*) FROM servers WHERE type = 'PURPUR'").fetchone()
        pufferfish = cur.execute("SELECT COUNT(*) FROM servers WHERE type = 'PUFFERFISH'").fetchone()
    class multi_threaded():
        folia = cur.execute("SELECT COUNT(*) FROM servers WHERE type = 'FOLIA'").fetchone()
        lumina = cur.execute("SELECT COUNT(*) FROM servers WHERE type = 'LUMINA'").fetchone()
    class proxies():
        velocity = cur.execute("SELECT COUNT(*) FROM servers WHERE type = 'VELOCITY'").fetchone()
        waterfall = cur.execute("SELECT COUNT(*) FROM servers WHERE type = 'WATERFALL'").fetchone()
        bungeecord = cur.execute("SELECT COUNT(*) FROM servers WHERE type = 'BUNGEECORD'").fetchone()

database.pool.putconn(conn = conn)
