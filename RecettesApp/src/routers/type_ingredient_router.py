from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from services.type_ingredient_service import (
    get_all_type_ingredients,
    get_type_ingredient_by_id,
    create_type_ingredient,
    update_type_ingredient,
    delete_type_ingredient
)
from schemas.type_ingredient_schema import (
    TypeIngredientCreate,
    TypeIngredientUpdate,
    TypeIngredientOut
)

router = APIRouter(
    prefix="/type-ingredients",
    tags=["TypeIngredient"]
)

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
@router.get("/", response_model=list[TypeIngredientOut])
def read_type_ingredients(db: Session = Depends(get_db)):
    return get_all_type_ingredients(db)

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
@router.get("/{type_id}", response_model=TypeIngredientOut)
def read_type_ingredient(type_id: int, db: Session = Depends(get_db)):
    type_ing = get_type_ingredient_by_id(db, type_id)
    if not type_ing:
        raise HTTPException(status_code=404, detail="Type d'ingrédient non trouvé")
    return type_ing

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
@router.post("/", response_model=TypeIngredientOut)
def create_new_type_ingredient(data: TypeIngredientCreate, db: Session = Depends(get_db)):
    return create_type_ingredient(db, data.dict())

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
@router.put("/{type_id}", response_model=TypeIngredientOut)
def update_existing_type_ingredient(type_id: int, data: TypeIngredientUpdate, db: Session = Depends(get_db)):
    type_ing = update_type_ingredient(db, type_id, data.dict(exclude_unset=True))
    if not type_ing:
        raise HTTPException(status_code=404, detail="Type d'ingrédient non trouvé")
    return type_ing

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
@router.delete("/{type_id}")
def delete_existing_type_ingredient(type_id: int, db: Session = Depends(get_db)):
    success = delete_type_ingredient(db, type_id)
    if not success:
        raise HTTPException(status_code=404, detail="Type d'ingrédient non trouvé")
    return {"message": "Type d'ingrédient supprimé"}