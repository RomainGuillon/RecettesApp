# -*- coding: utf-8 -*-


from database.database import engine
from database.models import Base

def create_tables():
    print("Cr�ation des tables dans la base SQL Server...")
    Base.metadata.create_all(engine)
    print("Tables cr��es avec succ�s.")

if __name__ == "__main__":
    create_tables()
