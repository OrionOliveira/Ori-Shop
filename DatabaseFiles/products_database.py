from DatabaseFiles import connection_database as cndb

connect_results = cndb.connect()
cursor = connect_results[0]
conexao = connect_results[1]

def info_product(seller):
    query = f"""SELECT * FROM Produtos
    WHERE seller = '{seller}'
    """
    ids = []
    products = []
    p_amount = []
    for x in cursor.execute(query):
        id = x[0]
        produto = x[1]
        qtd = x[4]
        ids.append(id)
        products.append(produto)
        p_amount.append(qtd)
        
    print(ids)
    print(products)
    print(p_amount)
    return ids, products, p_amount

def addProducts(nome_produto, preco_produto, seller):
    connect_results = cndb.connect()
    cursor = connect_results[0]
    count = 0
    
    lists = info_product(seller)
    l_product = lists[1]
    id = 0

    if nome_produto in l_product:
        query_row = []
        p_id = ''
        amount = ''
        query = f"""SELECT * FROM Produtos
        WHERE nome = '{nome_produto}' and price = '{preco_produto}' and seller = '{seller}'"""
        for i in cursor.execute(query):
            query_row.append(i)
            p_infos = query_row[0]
            p_id = p_infos[0]
            print(p_id)
            amount = p_infos[4]
            print(amount)
        return p_id, False, amount
    else:
        query1 = f"""SELECT * FROM Produtos
        """
        for i in cursor.execute(query1):
            count = count + 1

        print(f"O contador resultou em: {count}")
        id = count + 1
        print(f"O id é: {id}")
        
        query = f"""INSERT INTO Produtos(id, nome, price, seller, amount)
            VALUES
                ({id}, '{nome_produto}', {preco_produto}, '{seller}', 1)
        """
        cursor.execute(query)
        cursor.commit()
        return id, True

def updateAmount(id, amount):
    newAmount = amount + 1
    query = f"""UPDATE Produtos SET amount = {newAmount}
    WHERE id = {id}"""

    cursor.execute(query)
    cursor.commit()