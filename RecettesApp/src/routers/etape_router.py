from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from services.etape_service import (
    get_all_etapes,
    get_etape_by_id,
    get_etapes_by_recette,
    create_etape,
    update_etape,
    delete_etape
)
from schemas.etape_schema import (
    EtapeCreate,
    EtapeUpdate,
    EtapeOut
)

router = APIRouter(
    prefix="/etapes",
    tags=["Etapes"]
)

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
@router.get("/", response_model=list[EtapeOut])
def read_etapes(db: Session = Depends(get_db)):
    return get_all_etapes(db)

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
@router.get("/{etape_id}", response_model=EtapeOut)
def read_etape(etape_id: int, db: Session = Depends(get_db)):
    etape = get_etape_by_id(db, etape_id)
    if not etape:
        raise HTTPException(status_code=404, detail="Étape non trouvée")
    return etape

# ------------------------------------------------------------
# GET ETAPES FOR A RECIPE
# ------------------------------------------------------------
@router.get("/recette/{recette_id}", response_model=list[EtapeOut])
def read_etapes_for_recette(recette_id: int, db: Session = Depends(get_db)):
    return get_etapes_by_recette(db, recette_id)

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
@router.post("/", response_model=EtapeOut)
def create_new_etape(data: EtapeCreate, db: Session = Depends(get_db)):
    return create_etape(db, data.dict())

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
@router.put("/{etape_id}", response_model=EtapeOut)
def update_existing_etape(etape_id: int, data: EtapeUpdate, db: Session = Depends(get_db)):
    etape = update_etape(db, etape_id, data.dict(exclude_unset=True))
    if not etape:
        raise HTTPException(status_code=404, detail="Étape non trouvée")
    return etape

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
@router.delete("/{etape_id}")
def delete_existing_etape(etape_id: int, db: Session = Depends(get_db)):
    success = delete_etape(db, etape_id)
    if not success:
        raise HTTPException(status_code=404, detail="Étape non trouvée")
    return {"message": "Étape supprimée"}