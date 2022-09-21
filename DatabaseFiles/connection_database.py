import pyodbc
import pandas as pd

def connect():
    dados_conexao = ( 
        "Driver={SQL Server};"
        "Server=USAINBOLT\SQLORION;"
        "Database=OriShop;"
        "Trusted_Connection=yes"
        )

    print("Connecting...")
    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()
    return cursor, conexao