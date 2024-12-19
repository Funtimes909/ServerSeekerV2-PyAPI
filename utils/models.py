from pydantic import BaseModel

class Stats(BaseModel):
    count: int

class History(BaseModel):
    address: str
    playername: str
    playeruuid: str
    lastseen: int

class Key(BaseModel):
    apikey: str

class Server(BaseModel):
    address: str
    port: int
    version: str | None = None
    protocol: int | None = None
    software: str | None = None
    motd: str | None = None
    country: str | None = None
    asn: str | None = None
    org: str | None = None
    reversedns: str | None = None
    firstseen: int | None = None
    lastseen: int | None = None
    whitelist: bool | None = None
    cracked: bool | None = None
    enforces_secure_chat: bool | None = None
    prevents_reports: bool | None = None
    maxplayers: int | None = None
    onlineplayers: int | None = None
    icon: str | None = None
