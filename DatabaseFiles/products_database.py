from DatabaseFiles import connection_database as cndb
from DatabaseFiles import user_database as usdb

connect_results = cndb.connect()
cursor = connect_results[0]
conexao = connect_results[1]

def addProducts(nome_produto, preco_produto):
    global nome
    connect_results = cndb.connect()
    cursor = connect_results[0]
    seller = nome
    query = f"""INSERT INTO Produtos(id, nome, price, seller, amount)
        VALUES
            (1, '{nome_produto}', {preco_produto}, '{seller}', 1)
    """
    cursor.execute(query)
    cursor.commit()