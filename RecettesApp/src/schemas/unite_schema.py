from pydantic import BaseModel
from typing import Optional

# ------------------------------------------------------------
# Base
# ------------------------------------------------------------
class UniteBase(BaseModel):
    Nom: str
    Description: Optional[str] = None

# ------------------------------------------------------------
# Create
# ------------------------------------------------------------
class UniteCreate(UniteBase):
    pass

# ------------------------------------------------------------
# Update
# ------------------------------------------------------------
class UniteUpdate(BaseModel):
    Nom: Optional[str] = None
    Description: Optional[str] = None

# ------------------------------------------------------------
# Output
# ------------------------------------------------------------
class UniteOut(UniteBase):
    IDUnite: int

    class Config:
        from_attributes = True