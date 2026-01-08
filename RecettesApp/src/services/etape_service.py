from sqlalchemy.orm import Session
from database.models import Etape

# ------------------------------------------------------------
# GET ALL
# ------------------------------------------------------------
def get_all_etapes(db: Session):
    return db.query(Etape).all()

# ------------------------------------------------------------
# GET BY ID
# ------------------------------------------------------------
def get_etape_by_id(db: Session, etape_id: int):
    return db.query(Etape).filter(Etape.IDEtape == etape_id).first()

# ------------------------------------------------------------
# GET BY RECETTE
# ------------------------------------------------------------
def get_etapes_by_recette(db: Session, recette_id: int):
    return db.query(Etape).filter(Etape.IDRecette == recette_id).order_by(Etape.NumeroEtape).all()

# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
def create_etape(db: Session, data: dict):
    etape = Etape(
        NomEtape=data.get("NomEtape"),
        DescriptionEtape=data.get("DescriptionEtape"),
        NumeroEtape=data.get("NumeroEtape"),
        IDRecette=data.get("IDRecette")
    )
    db.add(etape)
    db.commit()
    db.refresh(etape)
    return etape

# ------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------
def update_etape(db: Session, etape_id: int, data: dict):
    etape = get_etape_by_id(db, etape_id)
    if not etape:
        return None

    for key, value in data.items():
        if hasattr(etape, key):
            setattr(etape, key, value)

    db.commit()
    db.refresh(etape)
    return etape

# ------------------------------------------------------------
# DELETE
# ------------------------------------------------------------
def delete_etape(db: Session, etape_id: int):
    etape = get_etape_by_id(db, etape_id)
    if not etape:
        return False

    db.delete(etape)
    db.commit()
    return True