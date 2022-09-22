from DatabaseFiles import connection_database as cndb
import pandas as pd

connect_results = cndb.connect()
cursor = connect_results[0]
conexao = connect_results[1]

def database_save(nome = '', idade = '', email = '', senha = ''):
    comando = f""" INSERT INTO Usuários
        VALUES
            ('{nome}', '{idade}', '{email}', '{senha}')"""
    print("Adicionado ao banco de dados!")
    
    cursor.execute(comando)
    cursor.commit()
    #y = pd.read_sql("SELECT * FROM Usuários", conexao)
    #print(y.head())

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
                        nome = s[0]
                        idade = s[1]
                        return True, nome, idade, email, senha
                    else:
                        print("\033[31mSenha incorreta!\033[m")
                        return False
                else: 
                    print("\033[31mSenha incorreta!\033[m")
                    return False
            else:
                print("\033[31mCampo senha é obrigatório!\033[m")
                return False
        else:
            print("\033[31mEmail não cadastrado, cadastrar?\033[m")
            return False
    else:
        print("\033[31mCampo email é obrigatório!\033[m")
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

nome = ''
def dt_user_info(email):
    query = f"""SELECT * FROM Usuários
    WHERE email = '{email}'
    """
    for i in cursor.execute(query):
        global nome
        nome_user = i[0]
        nome = nome_user
        idade_user = i[1]
        email_user = i[2]
        senha_user = i[3]
        return nome_user, idade_user, email_user, senha_user

    #df = pd.read_sql(query, conexao)
    #print(df.head())