import pyodbc
import pandas as pd

dados_conexao = ( 
    "Driver={SQL Server};"
    "Server=USAINBOLT\SQLORION;"
    "Database=OriShop;"
    "Trusted_Connection=yes"
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

def signin():
    pass

def login(email = '', senha = ''):
    lista_emails = email_check()
    lista_senhas = password_check()
    
    if email != '':
        if email in lista_emails:
            if senha != '':
                if senha in lista_senhas:
                    print("Seja bem vindo(a)!")
                    user_info(email)
                    return True
                else: 
                    print("Senha incorreta!")
            else:
                print("Campo senha é obrigatório!")
        else:
            print("Email não cadastrado, cadastrar?")
    else:
        print("Campo email é obrigatório!")
        return False

def email_check():
    lista_emails = []
    query1 = ("SELECT email FROM Usuários")

    for e in cursor.execute(query1):
        lista_emails.append(e.email)
    return lista_emails

def password_check():
    lista_senhas = []
    query2 = ("SELECT senha FROM Usuários")

    for s in cursor.execute(query2):
        lista_senhas.append(s.senha)
    return lista_senhas

def user_info(email):
    user_list = []
    query = """
    USE OriShop
    SELECT nome FROM Usuários WHERE email='orion@gmail.com'"""
    for i in cursor.execute(query):
        print(i.nome, i.idade, i.email, i.senha)

    #User_dic = {f'Nome': {user_list[0]}, 
    #             'Idade': {user_list[1]}, 
    #             'Email': {user_list[2]}, 
    #             'Senha': {user_list[3]}}
    #print(User_dic)