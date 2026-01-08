from pydantic import BaseModel
from typing import Optional

# ------------------------------------------------------------
# Base
# ------------------------------------------------------------
class RecetteBase(BaseModel):
    Nom: str
    Description: Optional[str] = None
    Origine: Optional[str] = None
    Type: Optional[str] = None
    TempsPreparation: Optional[int] = None
    TempsCuisson: Optional[int] = None
    PartsParDefaut: Optional[int] = None

# ------------------------------------------------------------
# Create
# ------------------------------------------------------------
class RecetteCreate(RecetteBase):
    pass

# ------------------------------------------------------------
# Update
# ------------------------------------------------------------
class RecetteUpdate(BaseModel):
    Nom: Optional[str] = None
    Description: Optional[str] = None
    Origine: Optional[str] = None
    Type: Optional[str] = None
    TempsPreparation: Optional[int] = None
    TempsCuisson: Optional[int] = None
    PartsParDefaut: Optional[int] = None

# ------------------------------------------------------------
# Output
# ------------------------------------------------------------
class RecetteOut(RecetteBase):
    IDRecette: int

    class Config:
        from_attributes = True