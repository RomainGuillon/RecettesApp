from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from services.ingredient_service import (
    get_all_ingredients,
    get_ingredient_by_id,
    create_ingredient,
    update_ingredient,
    delete_ingredient
)
from schemas.ingredient_schema import (
    IngredientCreate,
    IngredientUpdate,
    IngredientOut
)

router = APIRouter(
    prefix="/ingredients",
    tags=["Ingredients"]
)

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
@router.get("/", response_model=list[IngredientOut])
def read_ingredients(db: Session = Depends(get_db)):
    return get_all_ingredients(db)

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
@router.get("/{ingredient_id}", response_model=IngredientOut)
def read_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    ingredient = get_ingredient_by_id(db, ingredient_id)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingrédient non trouvé")
    return ingredient

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
@router.post("/", response_model=IngredientOut)
def create_new_ingredient(data: IngredientCreate, db: Session = Depends(get_db)):
    return create_ingredient(db, data.dict())

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
@router.put("/{ingredient_id}", response_model=IngredientOut)
def update_existing_ingredient(ingredient_id: int, data: IngredientUpdate, db: Session = Depends(get_db)):
    ingredient = update_ingredient(db, ingredient_id, data.dict(exclude_unset=True))
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingrédient non trouvé")
    return ingredient

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
@router.delete("/{ingredient_id}")
def delete_existing_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    success = delete_ingredient(db, ingredient_id)
    if not success:
        raise HTTPException(status_code=404, detail="Ingrédient non trouvé")
    return {"message": "Ingrédient supprimé"}