from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from services.unite_service import (
    get_all_unites,
    get_unite_by_id,
    create_unite,
    update_unite,
    delete_unite
)
from schemas.unite_schema import (
    UniteCreate,
    UniteUpdate,
    UniteOut
)

router = APIRouter(
    prefix="/unites",
    tags=["Unites"]
)

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
@router.get("/", response_model=list[UniteOut])
def read_unites(db: Session = Depends(get_db)):
    return get_all_unites(db)

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
@router.get("/{unite_id}", response_model=UniteOut)
def read_unite(unite_id: int, db: Session = Depends(get_db)):
    unite = get_unite_by_id(db, unite_id)
    if not unite:
        raise HTTPException(status_code=404, detail="Unité non trouvée")
    return unite

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
@router.post("/", response_model=UniteOut)
def create_new_unite(data: UniteCreate, db: Session = Depends(get_db)):
    return create_unite(db, data.dict())

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
@router.put("/{unite_id}", response_model=UniteOut)
def update_existing_unite(unite_id: int, data: UniteUpdate, db: Session = Depends(get_db)):
    unite = update_unite(db, unite_id, data.dict(exclude_unset=True))
    if not unite:
        raise HTTPException(status_code=404, detail="Unité non trouvée")
    return unite

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
@router.delete("/{unite_id}")
def delete_existing_unite(unite_id: int, db: Session = Depends(get_db)):
    success = delete_unite(db, unite_id)
    if not success:
        raise HTTPException(status_code=404, detail="Unité non trouvée")
    return {"message": "Unité supprimée"}