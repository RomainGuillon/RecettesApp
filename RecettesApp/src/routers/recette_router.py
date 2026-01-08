from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from services.recette_service import (
    get_all_recettes,
    get_recette_by_id,
    create_recette,
    update_recette,
    delete_recette
)
from schemas.recette_schema import RecetteCreate, RecetteUpdate, RecetteOut

router = APIRouter(
    prefix="/recettes",
    tags=["Recettes"]
)

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
@router.get("/", response_model=list[RecetteOut])
def read_recettes(db: Session = Depends(get_db)):
    return get_all_recettes(db)

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
@router.get("/{recette_id}", response_model=RecetteOut)
def read_recette(recette_id: int, db: Session = Depends(get_db)):
    recette = get_recette_by_id(db, recette_id)
    if not recette:
        raise HTTPException(status_code=404, detail="Recette non trouvée")
    return recette

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
@router.post("/", response_model=RecetteOut)
def create_new_recette(data: RecetteCreate, db: Session = Depends(get_db)):
    return create_recette(db, data.dict())

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
@router.put("/{recette_id}", response_model=RecetteOut)
def update_existing_recette(recette_id: int, data: RecetteUpdate, db: Session = Depends(get_db)):
    recette = update_recette(db, recette_id, data.dict(exclude_unset=True))
    if not recette:
        raise HTTPException(status_code=404, detail="Recette non trouvée")
    return recette

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
@router.delete("/{recette_id}")
def delete_existing_recette(recette_id: int, db: Session = Depends(get_db)):
    success = delete_recette(db, recette_id)
    if not success:
        raise HTTPException(status_code=404, detail="Recette non trouvée")
    return {"message": "Recette supprimée"}