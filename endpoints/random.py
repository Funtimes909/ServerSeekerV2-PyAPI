from psycopg.rows import class_row

import utils.database as database
from utils import models


def run():
    with database.pool.getconn() as connection:
        with connection.cursor(row_factory=class_row(models.Server)) as cursor:
            random = cursor.execute("SELECT * FROM servers ORDER BY RANDOM() LIMIT 1").fetchone()

    return {
        "address": random.address,
        "port": random.port,
        "version": random.version,
        "protocol": random.protocol,
        "software": random.software,
        "motd": random.motd,
        "country": random.country,
        "asn": random.asn,
        "org": random.org,
        "hostname": random.reversedns,
        "firstseen": random.firstseen,
        "lastseen": random.lastseen,
        "whitelist": random.whitelist,
        "cracked": random.cracked,
        "enforces_secure_chat": random.enforces_secure_chat,
        "prevents_reports": random.prevents_reports,
        "maxplayers": random.maxplayers,
        "onlineplayers": random.onlineplayers,
        "icon": random.icon
    }