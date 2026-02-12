# app/schemas/favorite_schema.py
from pydantic import BaseModel

class FavoriteCreate(BaseModel):
    user_id: int
    song_id: int
    
class FavoriteOut(BaseModel):
    id: int
    user_id: int
    song_id: int

    class Config:
        orm_mode = True

class SongInfo(BaseModel):
    id: int
    title: str
    artist: str
    category: str
    audio_url: str


class FavoriteResponse(BaseModel):
    id: int
    user_id: int
    song: SongInfo

    class Config:
        from_attributes = True  # Pydantic v2 (IMPORTANT)
