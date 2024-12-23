from fastapi import HTTPException
from psycopg.rows import class_row

import utils.database as database
import utils.models as models

def run(
        address: str = None,
        port: int = None,
        version: str = None,
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
        minimal: bool = None,
        seenafter: int = None,
        seenbefore: int = None,
        onlineplayers: int = None,
        maxplayers: int = None,
        limit: int = None,
        offset: int = None
):
    conn = database.pool.getconn()
    
    if minimal:
        query = "SELECT address, port, version, country, lastseen FROM servers WHERE "
    else:
        query = "SELECT * FROM servers WHERE "

    values = []

    if address:
        query += "address = %s AND "
        values.append(address)

    if port:
        query += "port = %s AND "
        values.append(port)

    if version:
        query += "version = %s AND "
        values.append(version)

    if protocol:
        query += "protocol = %s AND "
        values.append(protocol)

    if software:
        query += "type = %s AND "
        values.append(software)

    if motd:
        search_pattern = f"%{motd}%"
        query += "motd LIKE %s AND "
        values.append(search_pattern)

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
        query += "onlineplayers = 0 AND "

    if full:
        query += "onlineplayers >= maxplayers AND "

    if seenafter:
        query += "lastseen >= %s AND "
        values.append(seenafter)

    if seenbefore:
        query += "lastseen <= %s AND "
        values.append(seenbefore)

    if onlineplayers:
        query += "onlineplayers = %s AND "
        values.append(onlineplayers)

    if maxplayers:
        query += "maxplayers = %s AND "
        values.append(maxplayers)

    # If query hasn't been modified, error
    if len(query) <= 28:
        raise HTTPException(status_code=400, detail="You have to provide some search queries!")
    if empty and full:
        raise HTTPException(status_code=422, detail="You can't use both empty and full!")

    query = query.removesuffix(' AND ')
    query += " ORDER BY lastseen DESC"

    if offset:
        query += " OFFSET %s "
        values.append(offset)

    if limit:
        query += " LIMIT %s"
        values.append(limit)

    # Execute query
    cur = conn.cursor(row_factory=class_row(models.Server))
    results = cur.execute(query, values).fetchall()

    database.pool.putconn(conn)

    def output(serverid):
        server = results[serverid]
        if minimal:
            return {
                "address": server.address,
                "port": server.port,
                "version": server.version,
                "country": server.country,
                "lastseen": server.lastseen
            }

        return {
            "address": server.address,
            "port": server.port,
            "version": server.version,
            "protocol": server.protocol,
            "software": server.software,
            "motd": server.motd,
            "country": server.country,
            "asn": server.asn,
            "org": server.org,
            "hostname": server.reversedns,
            "firstseen": server.firstseen,
            "lastseen": server.lastseen,
            "whitelist": server.whitelist,
            "cracked": server.cracked,
            "enforces_secure_chat": server.enforces_secure_chat,
            "prevents_reports": server.prevents_reports,
            "maxplayers": server.maxplayers,
            "onlineplayers": server.onlineplayers,
            "icon": server.icon
        }

    json_output = []

    for i in range(len(results)):
        if not json_output:
            json_output = [output(i)]
        elif json_output:
            json_output.append(output(i))
    return json_output