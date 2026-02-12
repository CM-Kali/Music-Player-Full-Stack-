from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.favorite import Favorite
from app.schemas.favorite_schema import FavoriteCreate, FavoriteOut
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/favorites", tags=["Favorites"])

# Add favorite
@router.post("/add", response_model=FavoriteOut)
def add_favorite(fav: FavoriteCreate, db: Session = Depends(get_db)):
    # Check if already favorited
    exists = db.query(Favorite).filter(
        Favorite.user_id == fav.user_id,
        Favorite.song_id == fav.song_id
    ).first()
    if exists:
        raise HTTPException(status_code=400, detail="Already favorited")

    favorite = Favorite(user_id=fav.user_id, song_id=fav.song_id)
    db.add(favorite)
    db.commit()
    db.refresh(favorite)
    return favorite

# Remove favorite
@router.delete("/remove")
def remove_favorite(user_id: int, song_id: int, db: Session = Depends(get_db)):
    fav = db.query(Favorite).filter(
        Favorite.user_id == user_id,
        Favorite.song_id == song_id
    ).first()
    if not fav:
        raise HTTPException(status_code=404, detail="Favorite not found")
    db.delete(fav)
    db.commit()
    return JSONResponse(content={"detail": "Removed from favorites"})

# Get all favorites for a user
@router.get("/{user_id}")
def get_favorites(user_id: int, db: Session = Depends(get_db)):
    favs = db.query(Favorite).filter(Favorite.user_id == user_id).all()
    return favs
