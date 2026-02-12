from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.song import Song
import shutil, os
from fastapi.responses import JSONResponse
from fastapi import Query

router = APIRouter()

# Get all songs
@router.get("/")
def get_songs(category: str = Query(None), db: Session = Depends(get_db)):
    query = db.query(Song)
    if category:
        query = query.filter(Song.category == category)
    return query.all()

# Upload a new song
@router.post("/upload")
def upload_song(
    title: str = Form(...),
    artist: str = Form(...),
    category: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Validate file type
    if not file.filename.endswith(".mp3"):
        raise HTTPException(status_code=400, detail="Only mp3 files allowed")

    # Save file
    upload_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "songs")
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Save to DB
    song = Song(title=title, artist=artist, category=category, file_path=file.filename)
    db.add(song)
    db.commit()
    db.refresh(song)

    # Return JSON response
    audio_url = f"http://127.0.0.1:8000/media/{file.filename}"
    return JSONResponse(content={
        "id": song.id,
        "title": song.title,
        "artist": song.artist,
        "category": song.category,
        "audio_url": audio_url
    })
