from pydantic import BaseModel
from typing import Optional

# ------------------------------------------------------------
# Base
# ------------------------------------------------------------
class TypeIngredientBase(BaseModel):
    Nom: str

# ------------------------------------------------------------
# Create
# ------------------------------------------------------------
class TypeIngredientCreate(TypeIngredientBase):
    pass

# ------------------------------------------------------------
# Update
# ------------------------------------------------------------
class TypeIngredientUpdate(BaseModel):
    Nom: Optional[str] = None

# ------------------------------------------------------------
# Output
# ------------------------------------------------------------
class TypeIngredientOut(TypeIngredientBase):
    IDTypeIngredient: int

    class Config:
        from_attributes = True