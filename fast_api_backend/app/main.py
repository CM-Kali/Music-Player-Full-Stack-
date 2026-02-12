from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.database import Base, engine
from app.routes import songs, favorites
from app.models.song import Song
from app.models.favorite import Favorite
import os

app = FastAPI(title="Music Backend API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Songs directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SONGS_DIR = os.path.join(BASE_DIR, "songs")
os.makedirs(SONGS_DIR, exist_ok=True)

app.mount("/media", StaticFiles(directory=SONGS_DIR), name="media")

# Create tables
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(songs.router, prefix="/songs", tags=["Songs"])
app.include_router(favorites.router, prefix="/favorites", tags=["Favorites"])

@app.get("/")
def root():
    return {"status": "running"}
