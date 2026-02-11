from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/media", StaticFiles(directory="songs"), name="media")

@app.get("/songs")
def get_songs():
    return [
        {
            "id": 1,
            "title": "Relax Beats",
            "artist": "CM Studio",
            "audio_url": "http://127.0.0.1:8000/media/song1.mp3"
        },
        {
            "id": 2,
            "title": "Night Vibes",
            "artist": "CM Studio",
            "audio_url": "http://127.0.0.1:8000/media/song2.mp3"
        }
    ]
