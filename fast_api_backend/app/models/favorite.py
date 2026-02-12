from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from app.database import Base

class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)  # For now, you can use dummy user_id
    song_id = Column(Integer, ForeignKey("songs.id"), nullable=False)

    __table_args__ = (UniqueConstraint("user_id", "song_id", name="_user_song_uc"),)
