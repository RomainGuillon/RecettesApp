from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from services.ingredient_recette_service import (
    get_all_ingredient_recettes,
    get_ingredient_recette_by_id,
    get_ingredients_by_recette,
    create_ingredient_recette,
    update_ingredient_recette,
    delete_ingredient_recette
)
from schemas.ingredient_recette_schema import (
    IngredientRecetteCreate,
    IngredientRecetteUpdate,
    IngredientRecetteOut
)

router = APIRouter(
    prefix="/ingredient-recette",
    tags=["IngredientRecette"]
)

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
@router.get("/", response_model=list[IngredientRecetteOut])
def read_ingredient_recettes(db: Session = Depends(get_db)):
    return get_all_ingredient_recettes(db)

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
@router.get("/{ir_id}", response_model=IngredientRecetteOut)
def read_ingredient_recette(ir_id: int, db: Session = Depends(get_db)):
    ir = get_ingredient_recette_by_id(db, ir_id)
    if not ir:
        raise HTTPException(status_code=404, detail="Relation ingrédient-recette non trouvée")
    return ir

# ------------------------------------------------------------
# GET INGREDIENTS FOR A RECIPE
# ------------------------------------------------------------
@router.get("/recette/{recette_id}", response_model=list[IngredientRecetteOut])
def read_ingredients_for_recette(recette_id: int, db: Session = Depends(get_db)):
    return get_ingredients_by_recette(db, recette_id)

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
@router.post("/", response_model=IngredientRecetteOut)
def create_new_ingredient_recette(data: IngredientRecetteCreate, db: Session = Depends(get_db)):
    return create_ingredient_recette(db, data.dict())

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
@router.put("/{ir_id}", response_model=IngredientRecetteOut)
def update_existing_ingredient_recette(ir_id: int, data: IngredientRecetteUpdate, db: Session = Depends(get_db)):
    ir = update_ingredient_recette(db, ir_id, data.dict(exclude_unset=True))
    if not ir:
        raise HTTPException(status_code=404, detail="Relation ingrédient-recette non trouvée")
    return ir

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
@router.delete("/{ir_id}")
def delete_existing_ingredient_recette(ir_id: int, db: Session = Depends(get_db)):
    success = delete_ingredient_recette(db, ir_id)
    if not success:
        raise HTTPException(status_code=404, detail="Relation ingrédient-recette non trouvée")
    return {"message": "Relation ingrédient-recette supprimée"}