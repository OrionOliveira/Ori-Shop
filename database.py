import pyodbc
import main as mn

nome = mn.Admin.addProducts()

print(f"""
Produtos
Nome: {nome}
Preço: 4200
Vendedor: Orion
""")


hack_nome = mn.Config.teste()

print(f"Nome obtido: {hack_nome}")