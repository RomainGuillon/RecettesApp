from pydantic import BaseModel
from typing import Optional

# ------------------------------------------------------------
# Base
# ------------------------------------------------------------
class IngredientRecetteBase(BaseModel):
    IDRecette: int
    IDIngredient: int
    Quantite: float
    IDUnite: int

# ------------------------------------------------------------
# Create
# ------------------------------------------------------------
class IngredientRecetteCreate(IngredientRecetteBase):
    pass

# ------------------------------------------------------------
# Update
# ------------------------------------------------------------
class IngredientRecetteUpdate(BaseModel):
    IDRecette: Optional[int] = None
    IDIngredient: Optional[int] = None
    Quantite: Optional[float] = None
    IDUnite: Optional[int] = None

# ------------------------------------------------------------
# Output
# ------------------------------------------------------------
class IngredientRecetteOut(IngredientRecetteBase):
    IDIngredientRecette: int

    class Config:
        from_attributes = True