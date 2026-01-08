from sqlalchemy.orm import Session
from database.models import TypeIngredient

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
def get_all_type_ingredients(db: Session):
    return db.query(TypeIngredient).all()

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
def get_type_ingredient_by_id(db: Session, type_id: int):
    return db.query(TypeIngredient).filter(TypeIngredient.IDTypeIngredient == type_id).first()

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
def create_type_ingredient(db: Session, data: dict):
    type_ing = TypeIngredient(
        Nom=data.get("Nom")
    )
    db.add(type_ing)
    db.commit()
    db.refresh(type_ing)
    return type_ing

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
def update_type_ingredient(db: Session, type_id: int, data: dict):
    type_ing = get_type_ingredient_by_id(db, type_id)
    if not type_ing:
        return None

    for key, value in data.items():
        if hasattr(type_ing, key):
            setattr(type_ing, key, value)

    db.commit()
    db.refresh(type_ing)
    return type_ing

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
def delete_type_ingredient(db: Session, type_id: int):
    type_ing = get_type_ingredient_by_id(db, type_id)
    if not type_ing:
        return False

    db.delete(type_ing)
    db.commit()
    return True