import pyodbc
import pandas as pd
from main import Admin, Signin, Config, Login

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

    count = cursor.execute(comando).rowcount
    cursor.commit()
    print(f"Usuário(s) adicionado(s): {str(count)}")

def print_usuário(c = 0):
    query = ("INSERT INTO Usuários(nome, idade, email, senha) VALUES ('Raul', 18, 'raul@gmail.com', 13289674)")
    # Usuários
    if c == 1:
        print("Usuários")
        for row in cursor.execute(query):
            print(f"""
            ====================================
            Nome: {row.nome}
            Idade: {row.idade}
            Email: {row.email}
            Senha: {row.senha}
            ====================================""")
    # Número de usuários
    elif c == 2:
        print("Número de Usuários")
        count = cursor.execute(query).rowcount
        print(f"Rows inserted: {str(count)}")
        cursor.commit()

def login(email = '', senha = '', login = False):
    lista_emails = []
    lista_senhas = []

    query1 = ("SELECT email FROM Usuários")
    query2 = ("SELECT senha FROM Usuários")

    for e in cursor.execute(query1):
        lista_emails.append(e.email)
    for s in cursor.execute(query2):
        lista_senhas.append(s.senha)
    
    if email != '':
        if email in lista_emails:
            if senha != '':
                if senha in lista_senhas:
                    print("Seja bem vindo(a)!")
                    l = Login()
                    l.trocar_tela()
                else: 
                    print("Senha incorreta!")
            else:
                print("Campo senha é obrigatório!")
        else:
            print("Email não cadastrado, cadastrar?")
    else:
        print("Campo email é obrigatório!")
    