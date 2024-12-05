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