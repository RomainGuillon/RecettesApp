------------------------------------------------------------
-- BASE DE DONNÉES
------------------------------------------------------------
CREATE DATABASE Recettes;
GO

USE Recettes;
GO

------------------------------------------------------------
-- TABLE : TypeIngredient
------------------------------------------------------------
CREATE TABLE TypeIngredient (
    IDTypeIngredient INT IDENTITY PRIMARY KEY,
    GuidTypeIngredient UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
    Nom NVARCHAR(255) NOT NULL
);
GO

------------------------------------------------------------
-- TABLE : Unite
------------------------------------------------------------
CREATE TABLE Unite (
    IDUnite INT IDENTITY PRIMARY KEY,
    GuidUnite UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
    Nom NVARCHAR(50) NOT NULL,
    Description NVARCHAR(255)
);
GO

------------------------------------------------------------
-- TABLE : Ingredient
------------------------------------------------------------
CREATE TABLE Ingredient (
    IDIngredient INT IDENTITY PRIMARY KEY,
    GuidIngredient UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
    Nom NVARCHAR(255) NOT NULL,
    IDTypeIngredient INT NOT NULL,

    CONSTRAINT FK_Ingredient_TypeIngredient
        FOREIGN KEY (IDTypeIngredient)
        REFERENCES TypeIngredient(IDTypeIngredient)
);
GO

------------------------------------------------------------
-- TABLE : Recette
------------------------------------------------------------
CREATE TABLE Recette (
    IDRecette INT IDENTITY PRIMARY KEY,
    GuidRecette UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
    Nom NVARCHAR(255) NOT NULL,
    Description NVARCHAR(MAX),
    Origine NVARCHAR(255),
    Type NVARCHAR(255),
    TempsPreparation INT,
    TempsCuisson INT,
    PartsParDefaut INT
);
GO

------------------------------------------------------------
-- TABLE : IngredientRecette
------------------------------------------------------------
CREATE TABLE IngredientRecette (
    IDIngredientRecette INT IDENTITY PRIMARY KEY,
    GuidIngredientRecette UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
    IDRecette INT NOT NULL,
    IDIngredient INT NOT NULL,
    Quantite FLOAT NOT NULL,
    IDUnite INT NOT NULL,

    CONSTRAINT FK_IngredientRecette_Recette
        FOREIGN KEY (IDRecette)
        REFERENCES Recette(IDRecette),

    CONSTRAINT FK_IngredientRecette_Ingredient
        FOREIGN KEY (IDIngredient)
        REFERENCES Ingredient(IDIngredient),

    CONSTRAINT FK_IngredientRecette_Unite
        FOREIGN KEY (IDUnite)
        REFERENCES Unite(IDUnite)
);
GO

------------------------------------------------------------
-- TABLE : Etape
------------------------------------------------------------
CREATE TABLE Etape (
    IDEtape INT IDENTITY PRIMARY KEY,
    GuidEtape UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
    NomEtape NVARCHAR(255),
    DescriptionEtape NVARCHAR(MAX),
    NumeroEtape INT NOT NULL,
    IDRecette INT NOT NULL,

    CONSTRAINT FK_Etape_Recette
        FOREIGN KEY (IDRecette)
        REFERENCES Recette(IDRecette)
);
GO

------------------------------------------------------------
-- TABLE : Variante
------------------------------------------------------------
CREATE TABLE Variante (
    IDVariante INT IDENTITY PRIMARY KEY,
    GuidVariante UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
    IDRecetteBase INT NOT NULL,
    IDRecetteVariante INT NOT NULL,
    Difference NVARCHAR(MAX),

    CONSTRAINT FK_Variante_RecetteBase
        FOREIGN KEY (IDRecetteBase)
        REFERENCES Recette(IDRecette),

    CONSTRAINT FK_Variante_RecetteVariante
        FOREIGN KEY (IDRecetteVariante)
        REFERENCES Recette(IDRecette)
);
GO

------------------------------------------------------------
-- TABLE : RecetteRecette (recettes imbriquées)
------------------------------------------------------------
CREATE TABLE RecetteRecette (
    IDRecetteRecette INT IDENTITY PRIMARY KEY,
    IDRecetteParent INT NOT NULL,
    IDRecetteEnfant INT NOT NULL,

    CONSTRAINT FK_RecetteRecette_Parent
        FOREIGN KEY (IDRecetteParent)
        REFERENCES Recette(IDRecette),

    CONSTRAINT FK_RecetteRecette_Enfant
        FOREIGN KEY (IDRecetteEnfant)
        REFERENCES Recette(IDRecette)
);
GO