from pydantic import BaseModel
from typing import Optional

# ------------------------------------------------------------
# Base
# ------------------------------------------------------------
class EtapeBase(BaseModel):
    NomEtape: Optional[str] = None
    DescriptionEtape: Optional[str] = None
    NumeroEtape: int
    IDRecette: int

# ------------------------------------------------------------
# Create
# ------------------------------------------------------------
class EtapeCreate(EtapeBase):
    pass

# ------------------------------------------------------------
# Update
# ------------------------------------------------------------
class EtapeUpdate(BaseModel):
    NomEtape: Optional[str] = None
    DescriptionEtape: Optional[str] = None
    NumeroEtape: Optional[int] = None
    IDRecette: Optional[int] = None

# ------------------------------------------------------------
# Output
# ------------------------------------------------------------
class EtapeOut(EtapeBase):
    IDEtape: int

    class Config:
        from_attributes = True