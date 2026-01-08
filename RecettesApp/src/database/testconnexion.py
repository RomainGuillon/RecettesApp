import pyodbc

conn = pyodbc.connect(r"""
    DRIVER={ODBC Driver 17 for SQL Server};
    SERVER=(localdb)\MSSQLLocalDB;
    DATABASE=Recettes;
    Trusted_Connection=yes;
""")


print("Connexion OK")
