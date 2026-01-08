from pydantic import BaseModel
from typing import Optional

# ------------------------------------------------------------
# Base
# ------------------------------------------------------------
class VarianteBase(BaseModel):
    IDRecetteBase: int
    IDRecetteVariante: int
    Difference: Optional[str] = None

# ------------------------------------------------------------
# Create
# ------------------------------------------------------------
class VarianteCreate(VarianteBase):
    pass

# ------------------------------------------------------------
# Update
# ------------------------------------------------------------
class VarianteUpdate(BaseModel):
    IDRecetteBase: Optional[int] = None
    IDRecetteVariante: Optional[int] = None
    Difference: Optional[str] = None

# ------------------------------------------------------------
# Output
# ------------------------------------------------------------
class VarianteOut(VarianteBase):
    IDVariante: int

    class Config:
        from_attributes = True