from sqlalchemy.orm import Session
from database.models import RecetteRecette

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
def get_all_recette_recettes(db: Session):
    return db.query(RecetteRecette).all()

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
def get_recette_recette_by_id(db: Session, rr_id: int):
    return db.query(RecetteRecette).filter(
        RecetteRecette.IDRecetteRecette == rr_id
    ).first()

# ------------------------------------------------------------
# GET CHILDREN OF A PARENT RECIPE
# ------------------------------------------------------------
def get_enfants_by_parent(db: Session, parent_id: int):
    return db.query(RecetteRecette).filter(
        RecetteRecette.IDRecetteParent == parent_id
    ).all()

# ------------------------------------------------------------
# GET PARENTS OF A CHILD RECIPE
# ------------------------------------------------------------
def get_parents_by_enfant(db: Session, enfant_id: int):
    return db.query(RecetteRecette).filter(
        RecetteRecette.IDRecetteEnfant == enfant_id
    ).all()

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
def create_recette_recette(db: Session, data: dict):
    rr = RecetteRecette(
        IDRecetteParent=data.get("IDRecetteParent"),
        IDRecetteEnfant=data.get("IDRecetteEnfant")
    )
    db.add(rr)
    db.commit()
    db.refresh(rr)
    return rr

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
def update_recette_recette(db: Session, rr_id: int, data: dict):
    rr = get_recette_recette_by_id(db, rr_id)
    if not rr:
        return None

    for key, value in data.items():
        if hasattr(rr, key):
            setattr(rr, key, value)

    db.commit()
    db.refresh(rr)
    return rr

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
def delete_recette_recette(db: Session, rr_id: int):
    rr = get_recette_recette_by_id(db, rr_id)
    if not rr:
        return False

    db.delete(rr)
    db.commit()
    return True