from psycopg.rows import class_row

import utils.database as database
import utils.models as models

def run(
        version: str = None,
        port: int = None,
        software: str = None,
        protocol: int = None,
        motd: str = None,
        country: str = None,
        asn: str = None,
        org: str = None,
        hostname: str = None,
        icon: bool = None,
        prevents_reports: bool = None,
        whitelist: bool = None,
        cracked: bool = None,
        enforces_secure_chat: bool = None,
        empty: bool = None,
        full: bool = None,
        seenafter: int = None,
        seenbefore: int = None,
        onlineplayers: int = None,
        maxplayers: int = None,
        player: str = None,
):
    conn = database.pool.getconn()

    query = "SELECT * FROM servers WHERE "
    values = []

    if version:
        query += "version = %s AND "
        values.append(version)

    if port:
        query += "port = %s AND "
        values.append(port)

    if protocol:
        query += "protocol = %s AND "
        values.append(protocol)

    if software:
        query += "type = %s AND "
        values.append(software)

    if motd:
        query += "motd LIKE %s AND "
        values.append(motd)

    if country:
        query += "country = %s AND "
        values.append(country)

    if asn:
        query += "asn = %s AND "
        values.append(asn)

    if org:
        query += "org = %s AND "
        values.append(org)

    if hostname:
        query += "reversedns = %s AND "
        values.append(hostname)

    if icon:
        query += "icon IS NOT NULL AND "
        values.append(icon)

    if prevents_reports:
        query += "preventsReports = %s AND "
        values.append(prevents_reports)

    if whitelist:
        query += "whitelist = %s AND "
        values.append(whitelist)

    if cracked:
        query += "cracked = %s AND "
        values.append(cracked)

    if enforces_secure_chat:
        query += "enforcesSecureChat = %s AND "
        values.append(enforces_secure_chat)

    if empty:
        query += "onlineplayers == 0 AND "

    if full:
        query += "onlineplayers >= maxplayers AND "

    if seenafter:
        query += "lastseen < = %s AND "
        values.append(seenafter)

    if seenbefore:
        query += "seenbefore = %s AND "
        values.append(seenbefore)

    if onlineplayers:
        query += "onlineplayers = %s AND "
        values.append(onlineplayers)

    if maxplayers:
        query += "maxplayers = %s AND "
        values.append(maxplayers)


    query = query[:-5]

    print(query)
    print(values)

    cur = conn.cursor()
    # results = cur.execute(query, (values[0],)).fetchall()

    # print(len(results))