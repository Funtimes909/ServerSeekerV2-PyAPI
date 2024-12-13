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
    version: str
    protocol: int
    icon: str
    software: str
    motd: str
    country: str
    asn: str
    org: str
    firstseen: int
    lastseen: int
    hostname: str
    whitelist: bool
    cracked: bool
    enforces_secure_chat: bool
    prevents_reports: bool

