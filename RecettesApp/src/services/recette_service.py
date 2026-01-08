from sqlalchemy.orm import Session
from database.models import Recette

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
def get_all_recettes(db: Session):
    return db.query(Recette).all()

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
def get_recette_by_id(db: Session, recette_id: int):
    return db.query(Recette).filter(Recette.IDRecette == recette_id).first()

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
def create_recette(db: Session, data: dict):
    recette = Recette(
        Nom=data.get("Nom"),
        Description=data.get("Description"),
        Origine=data.get("Origine"),
        Type=data.get("Type"),
        TempsPreparation=data.get("TempsPreparation"),
        TempsCuisson=data.get("TempsCuisson"),
        PartsParDefaut=data.get("PartsParDefaut")
    )
    db.add(recette)
    db.commit()
    db.refresh(recette)
    return recette

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
def update_recette(db: Session, recette_id: int, data: dict):
    recette = get_recette_by_id(db, recette_id)
    if not recette:
        return None

    for key, value in data.items():
        if hasattr(recette, key):
            setattr(recette, key, value)

    db.commit()
    db.refresh(recette)
    return recette

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
def delete_recette(db: Session, recette_id: int):
    recette = get_recette_by_id(db, recette_id)
    if not recette:
        return False

    db.delete(recette)
    db.commit()
    return True