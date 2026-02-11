from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.song import Song

router = APIRouter(
    prefix="/songs",
    tags=["Songs"]
)

@router.get("/")
def get_all_songs(db: Session = Depends(get_db)):
    return db.query(Song).all()
