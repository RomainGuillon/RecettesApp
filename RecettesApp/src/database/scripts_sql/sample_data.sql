USE Recettes;
GO

-- Exemple d'ingrédients
INSERT INTO Ingredient (Nom, IDTypeIngredient) VALUES
('Farine', 8),
('Beurre', 7),
('Sel', 5),
('Pommes', 2),
('Sucre', 12);

-- Exemple de recette
INSERT INTO Recette (Nom, Description, Origine, Type, TempsPreparation, TempsCuisson, PartsParDefaut)
VALUES ('Tarte aux pommes', 'Une tarte classique et délicieuse.', 'Française', 'Dessert', 20, 30, 6);

-- Récupérer l’ID de la recette
DECLARE @idRecette INT = (SELECT TOP 1 IDRecette FROM Recette WHERE Nom='Tarte aux pommes');

-- Ingrédients de la recette
INSERT INTO IngredientRecette (IDRecette, IDIngredient, Quantite, IDUnite) VALUES
(@idRecette, 1, 250, 1), -- Farine 250g
(@idRecette, 2, 125, 1), -- Beurre 125g
(@idRecette, 3, 1, 7),   -- Sel 1 pincée
(@idRecette, 4, 4, 7),   -- Pommes 4 pièces
(@idRecette, 5, 50, 1);  -- Sucre 50g

-- Étapes
INSERT INTO Etape (IDRecette, NumeroEtape, NomEtape, DescriptionEtape) VALUES
(@idRecette, 1, 'Préparer la pâte', 'Mélanger la farine, le beurre et le sel.'),
(@idRecette, 2, 'Préparer les pommes', 'Éplucher et couper les pommes.'),
(@idRecette, 3, 'Cuisson', 'Cuire au four 30 minutes à 180°C.');
GO