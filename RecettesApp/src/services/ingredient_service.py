from sqlalchemy.orm import Session
from database.models import Ingredient

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
def get_all_ingredients(db: Session):
    return db.query(Ingredient).all()

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
def get_ingredient_by_id(db: Session, ingredient_id: int):
    return db.query(Ingredient).filter(Ingredient.IDIngredient == ingredient_id).first()

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
def create_ingredient(db: Session, data: dict):
    ingredient = Ingredient(
        Nom=data.get("Nom"),
        IDTypeIngredient=data.get("IDTypeIngredient")
    )
    db.add(ingredient)
    db.commit()
    db.refresh(ingredient)
    return ingredient

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
def update_ingredient(db: Session, ingredient_id: int, data: dict):
    ingredient = get_ingredient_by_id(db, ingredient_id)
    if not ingredient:
        return None

    for key, value in data.items():
        if hasattr(ingredient, key):
            setattr(ingredient, key, value)

    db.commit()
    db.refresh(ingredient)
    return ingredient

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
def delete_ingredient(db: Session, ingredient_id: int):
    ingredient = get_ingredient_by_id(db, ingredient_id)
    if not ingredient:
        return False

    db.delete(ingredient)
    db.commit()
    return True