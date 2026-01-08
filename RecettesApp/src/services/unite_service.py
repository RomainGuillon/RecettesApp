from sqlalchemy.orm import Session
from database.models import Unite

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
def get_all_unites(db: Session):
    return db.query(Unite).all()

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
def get_unite_by_id(db: Session, unite_id: int):
    return db.query(Unite).filter(Unite.IDUnite == unite_id).first()

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
def create_unite(db: Session, data: dict):
    unite = Unite(
        Nom=data.get("Nom"),
        Description=data.get("Description")
    )
    db.add(unite)
    db.commit()
    db.refresh(unite)
    return unite

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
def update_unite(db: Session, unite_id: int, data: dict):
    unite = get_unite_by_id(db, unite_id)
    if not unite:
        return None

    for key, value in data.items():
        if hasattr(unite, key):
            setattr(unite, key, value)

    db.commit()
    db.refresh(unite)
    return unite

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
def delete_unite(db: Session, unite_id: int):
    unite = get_unite_by_id(db, unite_id)
    if not unite:
        return False

    db.delete(unite)
    db.commit()
    return True