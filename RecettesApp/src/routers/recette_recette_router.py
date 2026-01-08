from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from services.recette_recette_service import (
    get_all_recette_recettes,
    get_recette_recette_by_id,
    get_enfants_by_parent,
    get_parents_by_enfant,
    create_recette_recette,
    update_recette_recette,
    delete_recette_recette
)
from schemas.recette_recette_schema import (
    RecetteRecetteCreate,
    RecetteRecetteUpdate,
    RecetteRecetteOut
)

router = APIRouter(
    prefix="/recette-recette",
    tags=["RecetteRecette"]
)

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
@router.get("/", response_model=list[RecetteRecetteOut])
def read_recette_recettes(db: Session = Depends(get_db)):
    return get_all_recette_recettes(db)

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
@router.get("/{rr_id}", response_model=RecetteRecetteOut)
def read_recette_recette(rr_id: int, db: Session = Depends(get_db)):
    rr = get_recette_recette_by_id(db, rr_id)
    if not rr:
        raise HTTPException(status_code=404, detail="Relation recette-recette non trouvée")
    return rr

# ------------------------------------------------------------
# GET CHILDREN OF A PARENT RECIPE
# ------------------------------------------------------------
@router.get("/parent/{recette_id}", response_model=list[RecetteRecetteOut])
def read_enfants(recette_id: int, db: Session = Depends(get_db)):
    return get_enfants_by_parent(db, recette_id)

# ------------------------------------------------------------
# GET PARENTS OF A CHILD RECIPE
# ------------------------------------------------------------
@router.get("/enfant/{recette_id}", response_model=list[RecetteRecetteOut])
def read_parents(recette_id: int, db: Session = Depends(get_db)):
    return get_parents_by_enfant(db, recette_id)

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
@router.post("/", response_model=RecetteRecetteOut)
def create_new_recette_recette(data: RecetteRecetteCreate, db: Session = Depends(get_db)):
    return create_recette_recette(db, data.dict())

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
@router.put("/{rr_id}", response_model=RecetteRecetteOut)
def update_existing_recette_recette(rr_id: int, data: RecetteRecetteUpdate, db: Session = Depends(get_db)):
    rr = update_recette_recette(db, rr_id, data.dict(exclude_unset=True))
    if not rr:
        raise HTTPException(status_code=404, detail="Relation recette-recette non trouvée")
    return rr

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
@router.delete("/{rr_id}")
def delete_existing_recette_recette(rr_id: int, db: Session = Depends(get_db)):
    success = delete_recette_recette(db, rr_id)
    if not success:
        raise HTTPException(status_code=404, detail="Relation recette-recette non trouvée")
    return {"message": "Relation recette-recette supprimée"}