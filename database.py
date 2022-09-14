import pyodbc
from main import Admin, Signin, Config

dados_conexao = ( 
    "Driver={SQL Server};"
    "Server=USAINBOLT\SQLORION;"
    "Database=OriShop;"
    )

print("Connecting...")
conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

def database_save(nome = '', idade = '', email = '', senha = ''):
    comando = f""" INSERT INTO Usuários
        VALUES
            ('{nome}', '{idade}', '{email}', '{senha}')"""
    print("Adicionado ao banco de dados!")
    cursor.execute(comando)
    cursor.commit( )

def print_usuário(nome = '', idade = '', email = '', senha = ''):
    print(f"""
        Nome: {nome}
        Idade: {idade}
        Email: {email}
        Senha: {senha}
        """)