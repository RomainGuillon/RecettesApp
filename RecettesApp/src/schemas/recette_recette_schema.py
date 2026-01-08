from pydantic import BaseModel
from typing import Optional

# ------------------------------------------------------------
# Base
# ------------------------------------------------------------
class RecetteRecetteBase(BaseModel):
    IDRecetteParent: int
    IDRecetteEnfant: int

# ------------------------------------------------------------
# Create
# ------------------------------------------------------------
class RecetteRecetteCreate(RecetteRecetteBase):
    pass

# ------------------------------------------------------------
# Update
# ------------------------------------------------------------
class RecetteRecetteUpdate(BaseModel):
    IDRecetteParent: Optional[int] = None
    IDRecetteEnfant: Optional[int] = None

# ------------------------------------------------------------
# Output
# ------------------------------------------------------------
class RecetteRecetteOut(RecetteRecetteBase):
    IDRecetteRecette: int

    class Config:
        from_attributes = True