from sqlalchemy import (
    Column, Integer, String, Float, ForeignKey, Text, UniqueConstraint
)
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# ------------------------------------------------------------
# TABLE : TypeIngredient
# ------------------------------------------------------------
class TypeIngredient(Base):
    __tablename__ = "TypeIngredient"

    IDTypeIngredient = Column(Integer, primary_key=True, index=True)
    GuidTypeIngredient = Column(UNIQUEIDENTIFIER, nullable=False)
    Nom = Column(String(255), nullable=False)

    ingredients = relationship("Ingredient", back_populates="type_ingredient")


# ------------------------------------------------------------
# TABLE : Unite
# ------------------------------------------------------------
class Unite(Base):
    __tablename__ = "Unite"

    IDUnite = Column(Integer, primary_key=True, index=True)
    GuidUnite = Column(UNIQUEIDENTIFIER, nullable=False)
    Nom = Column(String(50), nullable=False)
    Description = Column(String(255))

    ingredients_recette = relationship("IngredientRecette", back_populates="unite")


# ------------------------------------------------------------
# TABLE : Ingredient
# ------------------------------------------------------------
class Ingredient(Base):
    __tablename__ = "Ingredient"

    IDIngredient = Column(Integer, primary_key=True, index=True)
    GuidIngredient = Column(UNIQUEIDENTIFIER, nullable=False)
    Nom = Column(String(255), nullable=False)
    IDTypeIngredient = Column(Integer, ForeignKey("TypeIngredient.IDTypeIngredient"), nullable=False)

    type_ingredient = relationship("TypeIngredient", back_populates="ingredients")
    ingredients_recette = relationship("IngredientRecette", back_populates="ingredient")


# ------------------------------------------------------------
# TABLE : Recette
# ------------------------------------------------------------
class Recette(Base):
    __tablename__ = "Recette"

    IDRecette = Column(Integer, primary_key=True, index=True)
    GuidRecette = Column(UNIQUEIDENTIFIER, nullable=False)
    Nom = Column(String(255), nullable=False)
    Description = Column(Text)
    Origine = Column(String(255))
    Type = Column(String(255))
    TempsPreparation = Column(Integer)
    TempsCuisson = Column(Integer)
    PartsParDefaut = Column(Integer)

    ingredients = relationship("IngredientRecette", back_populates="recette")
    etapes = relationship("Etape", back_populates="recette")
    variantes_base = relationship("Variante", foreign_keys="Variante.IDRecetteBase", back_populates="recette_base")
    variantes_derivees = relationship("Variante", foreign_keys="Variante.IDRecetteVariante", back_populates="recette_variante")
    recettes_parents = relationship("RecetteRecette", foreign_keys="RecetteRecette.IDRecetteEnfant", back_populates="recette_enfant")
    recettes_enfants = relationship("RecetteRecette", foreign_keys="RecetteRecette.IDRecetteParent", back_populates="recette_parent")


# ------------------------------------------------------------
# TABLE : IngredientRecette
# ------------------------------------------------------------
class IngredientRecette(Base):
    __tablename__ = "IngredientRecette"

    IDIngredientRecette = Column(Integer, primary_key=True, index=True)
    GuidIngredientRecette = Column(UNIQUEIDENTIFIER, nullable=False)
    IDRecette = Column(Integer, ForeignKey("Recette.IDRecette"), nullable=False)
    IDIngredient = Column(Integer, ForeignKey("Ingredient.IDIngredient"), nullable=False)
    Quantite = Column(Float, nullable=False)
    IDUnite = Column(Integer, ForeignKey("Unite.IDUnite"), nullable=False)

    recette = relationship("Recette", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="ingredients_recette")
    unite = relationship("Unite", back_populates="ingredients_recette")


# ------------------------------------------------------------
# TABLE : Etape
# ------------------------------------------------------------
class Etape(Base):
    __tablename__ = "Etape"

    IDEtape = Column(Integer, primary_key=True, index=True)
    GuidEtape = Column(UNIQUEIDENTIFIER, nullable=False)
    NomEtape = Column(String(255))
    DescriptionEtape = Column(Text)
    NumeroEtape = Column(Integer, nullable=False)
    IDRecette = Column(Integer, ForeignKey("Recette.IDRecette"), nullable=False)

    recette = relationship("Recette", back_populates="etapes")


# ------------------------------------------------------------
# TABLE : Variante
# ------------------------------------------------------------
class Variante(Base):
    __tablename__ = "Variante"

    IDVariante = Column(Integer, primary_key=True, index=True)
    GuidVariante = Column(UNIQUEIDENTIFIER, nullable=False)
    IDRecetteBase = Column(Integer, ForeignKey("Recette.IDRecette"), nullable=False)
    IDRecetteVariante = Column(Integer, ForeignKey("Recette.IDRecette"), nullable=False)
    Difference = Column(Text)

    recette_base = relationship("Recette", foreign_keys=[IDRecetteBase], back_populates="variantes_base")
    recette_variante = relationship("Recette", foreign_keys=[IDRecetteVariante], back_populates="variantes_derivees")


# ------------------------------------------------------------
# TABLE : RecetteRecette
# ------------------------------------------------------------
class RecetteRecette(Base):
    __tablename__ = "RecetteRecette"

    IDRecetteRecette = Column(Integer, primary_key=True, index=True)
    IDRecetteParent = Column(Integer, ForeignKey("Recette.IDRecette"), nullable=False)
    IDRecetteEnfant = Column(Integer, ForeignKey("Recette.IDRecette"), nullable=False)

    recette_parent = relationship("Recette", foreign_keys=[IDRecetteParent], back_populates="recettes_enfants")
    recette_enfant = relationship("Recette", foreign_keys=[IDRecetteEnfant], back_populates="recettes_parents")