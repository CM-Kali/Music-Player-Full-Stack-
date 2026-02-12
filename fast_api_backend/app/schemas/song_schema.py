from pydantic import BaseModel

class SongCreate(BaseModel):
    title: str
    artist: str
    category: str
    audio_url: str

class SongResponse(BaseModel):
    id: int
    title: str
    artist: str
    category: str
    audio_url: str

    class Config:
        from_attributes = True

 