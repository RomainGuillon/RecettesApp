import os
import warnings
from sqlalchemy.exc import SAWarning

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
from database.models import Base


# Charger les variables d'environnement depuis .env
load_dotenv()
warnings.filterwarnings("ignore",category=SAWarning)

# -------------------------------------------------------------------
# 1. Lecture de la chaîne de connexion SQL Server
# -------------------------------------------------------------------
DB_SERVER = os.getenv("DB_SERVER", "localhost")
DB_NAME = os.getenv("DB_NAME", "Recettes")
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# Chaîne de connexion SQL Server via pyodbc
if DB_USER and DB_PASSWORD:
    CONNECTION_STRING = (
        f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
else:
    # Connexion Windows (Trusted Connection)
    CONNECTION_STRING = (
        f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
        "&trusted_connection=yes"
    )


# -------------------------------------------------------------------
# 2. Création de l'engine SQLAlchemy
# -------------------------------------------------------------------
try:
    engine = create_engine(
        CONNECTION_STRING,
        echo=False,            # Passe à True pour debug SQL
        future=True,
        pool_pre_ping=True     # Vérifie que la connexion est vivante
    )
except SQLAlchemyError as e:
    print("❌ Erreur lors de la création de l'engine SQLAlchemy :", e)
    raise

# -------------------------------------------------------------------
# 3. Session factory
# -------------------------------------------------------------------
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True
)

# -------------------------------------------------------------------
# 4. Fonction utilitaire pour obtenir une session
# -------------------------------------------------------------------
def get_session():
    """
    Fournit une session SQLAlchemy dans un contexte sécurisé.
    Usage :
        with get_session() as db:
            ...
    """
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

# -------------------------------------------------------------------
# 5. Fonction pour créer toutes les tables (optionnel)
# -------------------------------------------------------------------
def create_all_tables(Base):
    """
    Crée toutes les tables définies dans models.py
    Exemple d'utilisation :
        from models import Base
        create_all_tables(Base)
    """
    try:
        Base.metadata.create_all(bind=engine)
        print("✔ Tables créées avec succès")
    except SQLAlchemyError as e:
        print("❌ Erreur lors de la création des tables :", e)
        raise