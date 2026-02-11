from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Allow Flutter Web to access backend
origins = [
    "http://localhost:5000",  # Flutter Web default port
    "http://127.0.0.1:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve audio files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SONGS_DIR = os.path.join(BASE_DIR, "songs")
app.mount("/media", StaticFiles(directory=SONGS_DIR), name="media")

# Return list of songs
@app.get("/songs")
def get_songs():
    return [
        {
            "id": 1, 
            "title": "Relax Beats",
            "artist": "CM Studio",
            "audio_url": "http://192.168.10.8:8000/media/song1.mp3"
        },
        {
            "id": 2,
            "title": "Night Vibes",
            "artist": "CM Studio",
            "audio_url": "http://192.168.10.8:8000/media/song2.mp3"
        }
    ]
