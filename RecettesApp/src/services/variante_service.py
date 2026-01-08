from sqlalchemy.orm import Session
from database.models import Variante

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
def get_all_variantes(db: Session):
    return db.query(Variante).all()

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
def get_variante_by_id(db: Session, variante_id: int):
    return db.query(Variante).filter(Variante.IDVariante == variante_id).first()

# ------------------------------------------------------------
# GET VARIANTES FOR A BASE RECIPE
# ------------------------------------------------------------
def get_variantes_by_recette_base(db: Session, recette_id: int):
    return db.query(Variante).filter(
        Variante.IDRecetteBase == recette_id
    ).all()

# ------------------------------------------------------------
# GET VARIANTES FOR A DERIVED RECIPE
# ------------------------------------------------------------
def get_variantes_by_recette_variante(db: Session, recette_id: int):
    return db.query(Variante).filter(
        Variante.IDRecetteVariante == recette_id
    ).all()

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
def create_variante(db: Session, data: dict):
    variante = Variante(
        IDRecetteBase=data.get("IDRecetteBase"),
        IDRecetteVariante=data.get("IDRecetteVariante"),
        Difference=data.get("Difference")
    )
    db.add(variante)
    db.commit()
    db.refresh(variante)
    return variante

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
def update_variante(db: Session, variante_id: int, data: dict):
    variante = get_variante_by_id(db, variante_id)
    if not variante:
        return None

    for key, value in data.items():
        if hasattr(variante, key):
            setattr(variante, key, value)

    db.commit()
    db.refresh(variante)
    return variante

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
def delete_variante(db: Session, variante_id: int):
    variante = get_variante_by_id(db, variante_id)
    if not variante:
        return False

    db.delete(variante)
    db.commit()
    return True