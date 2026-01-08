# Application de gestion de recettes

Ce projet est une application PySide6 + SQLAlchemy permettant de gérer des recettes de cuisine avec :

- ingrédients
- unités
- étapes
- variantes
- recettes imbriquées
- recherche avancée
- impression

## 📁 Structure du projet## 🗄 Base de données

Les scripts SQL se trouvent dans `/database` :

- `create_database.sql` : création complète de la base
- `insert_unites.sql` : unités standard
- `insert_types_ingredients.sql` : types d’ingrédients
- `sample_data.sql` : données d’exemple

## 🚀 Lancer le projet

1. Exécuter les scripts SQL
2. Configurer SQLAlchemy dans `database.py`
3. Lancer l’application :
## 🧰 Technologies

- Python
- PySide6
- SQLAlchemy
- SQL Server
- Qt Designer