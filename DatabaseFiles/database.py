from multiprocessing.connection import wait
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
    y = pd.read_sql("SELECT * FROM Usuários", conexao)
    print(y.head())

def signin():
    pass

def login(email = '', senha = ''):
    lista_emails = email_check()
    lista_senhas = password_check()
    
    if email != '':
        if email in lista_emails:
            if senha != '':
                if senha in lista_senhas:
                    s = dt_user_info(email)
                    if senha == s[3]:
                        print("Seja bem vindo(a)!")
                        nome = s[0]
                        idade = s[1]
                        print(nome)
                        return True, nome, idade, email, senha
                    else:
                        print("Senha incorreta!")
                        return False
                else: 
                    print("Senha incorreta!")
                    return False
            else:
                print("Campo senha é obrigatório!")
                return False
        else:
            print("Email não cadastrado, cadastrar?")
            return False
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

def dt_user_info(email):
    query = f"""SELECT * FROM Usuários
    WHERE email = '{email}'
    """
    for i in cursor.execute(query):
        nome_user = i[0]
        idade_user = i[1]
        email_user = i[2]
        senha_user = i[3]
        print(f"""
        Nome: {nome_user}
        Idade: {idade_user}
        Email: {email_user}
        Senha: {senha_user}""")
        return nome_user, idade_user, email_user, senha_user

    df = pd.read_sql(query, conexao)
    print(df.head())

def addProducts(nome_produto, preco_produto):
    seller = "Orion"
    query = f"""INSERT INTO Produtos(id, nome, price, seller, amount)
        VALUES
            (1, '{nome_produto}', {preco_produto}, '{seller}', 1)
    """