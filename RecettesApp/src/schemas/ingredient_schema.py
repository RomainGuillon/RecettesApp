from pydantic import BaseModel
from typing import Optional

# ------------------------------------------------------------
# Base
# ------------------------------------------------------------
class IngredientBase(BaseModel):
    Nom: str
    IDTypeIngredient: int

# ------------------------------------------------------------
# Create
# ------------------------------------------------------------
class IngredientCreate(IngredientBase):
    pass

# ------------------------------------------------------------
# Update
# ------------------------------------------------------------
class IngredientUpdate(BaseModel):
    Nom: Optional[str] = None
    IDTypeIngredient: Optional[int] = None

# ------------------------------------------------------------
# Output
# ------------------------------------------------------------
class IngredientOut(IngredientBase):
    IDIngredient: int

    class Config:
        from_attributes = True