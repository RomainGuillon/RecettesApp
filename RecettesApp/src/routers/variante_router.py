from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from services.variante_service import (
    get_all_variantes,
    get_variante_by_id,
    get_variantes_by_recette_base,
    get_variantes_by_recette_variante,
    create_variante,
    update_variante,
    delete_variante
)
from schemas.variante_schema import (
    VarianteCreate,
    VarianteUpdate,
    VarianteOut
)

router = APIRouter(
    prefix="/variantes",
    tags=["Variantes"]
)

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
@router.get("/", response_model=list[VarianteOut])
def read_variantes(db: Session = Depends(get_db)):
    return get_all_variantes(db)

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
@router.get("/{variante_id}", response_model=VarianteOut)
def read_variante(variante_id: int, db: Session = Depends(get_db)):
    variante = get_variante_by_id(db, variante_id)
    if not variante:
        raise HTTPException(status_code=404, detail="Variante non trouvée")
    return variante

# ------------------------------------------------------------
# GET VARIANTES FOR A BASE RECIPE
# ------------------------------------------------------------
@router.get("/base/{recette_id}", response_model=list[VarianteOut])
def read_variantes_base(recette_id: int, db: Session = Depends(get_db)):
    return get_variantes_by_recette_base(db, recette_id)

# ------------------------------------------------------------
# GET VARIANTES FOR A VARIANT RECIPE
# ------------------------------------------------------------
@router.get("/variante/{recette_id}", response_model=list[VarianteOut])
def read_variantes_variante(recette_id: int, db: Session = Depends(get_db)):
    return get_variantes_by_recette_variante(db, recette_id)

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
@router.post("/", response_model=VarianteOut)
def create_new_variante(data: VarianteCreate, db: Session = Depends(get_db)):
    return create_variante(db, data.dict())

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
@router.put("/{variante_id}", response_model=VarianteOut)
def update_existing_variante(variante_id: int, data: VarianteUpdate, db: Session = Depends(get_db)):
    variante = update_variante(db, variante_id, data.dict(exclude_unset=True))
    if not variante:
        raise HTTPException(status_code=404, detail="Variante non trouvée")
    return variante

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
@router.delete("/{variante_id}")
def delete_existing_variante(variante_id: int, db: Session = Depends(get_db)):
    success = delete_variante(db, variante_id)
    if not success:
        raise HTTPException(status_code=404, detail="Variante non trouvée")
    return {"message": "Variante supprimée"}
