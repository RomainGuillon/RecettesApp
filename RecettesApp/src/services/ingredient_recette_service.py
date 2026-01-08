from sqlalchemy.orm import Session
from database.models import IngredientRecette

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
def get_all_ingredient_recettes(db: Session):
    return db.query(IngredientRecette).all()

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
def get_ingredient_recette_by_id(db: Session, ingredient_recette_id: int):
    return db.query(IngredientRecette).filter(
        IngredientRecette.IDIngredientRecette == ingredient_recette_id
    ).first()

# ------------------------------------------------------------
# GET BY RECETTE
# ------------------------------------------------------------
def get_ingredients_by_recette(db: Session, recette_id: int):
    return db.query(IngredientRecette).filter(
        IngredientRecette.IDRecette == recette_id
    ).all()

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
def create_ingredient_recette(db: Session, data: dict):
    ing_rec = IngredientRecette(
        IDRecette=data.get("IDRecette"),
        IDIngredient=data.get("IDIngredient"),
        Quantite=data.get("Quantite"),
        IDUnite=data.get("IDUnite")
    )
    db.add(ing_rec)
    db.commit()
    db.refresh(ing_rec)
    return ing_rec

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
def update_ingredient_recette(db: Session, ingredient_recette_id: int, data: dict):
    ing_rec = get_ingredient_recette_by_id(db, ingredient_recette_id)
    if not ing_rec:
        return None

    for key, value in data.items():
        if hasattr(ing_rec, key):
            setattr(ing_rec, key, value)

    db.commit()
    db.refresh(ing_rec)
    return ing_rec

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
def delete_ingredient_recette(db: Session, ingredient_recette_id: int):
    ing_rec = get_ingredient_recette_by_id(db, ingredient_recette_id)
    if not ing_rec:
        return False

    db.delete(ing_rec)
    db.commit()
    return True