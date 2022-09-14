from asyncio.windows_events import NULL
from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import database 
import json

class random(BoxLayout):
    pass

class Manager(ScreenManager):
    pass

class Menu(Screen):
    _telaprodutos = ObjectProperty(None)

    def removeProduct(self):
        self.ids.box_shop.remove_widget()

class Signin(Screen):
    users_list = []
    _name = ObjectProperty(None)
    _age = ObjectProperty(None)
    _email = ObjectProperty(None)
    _password = ObjectProperty(None)
    
    def __init__(self, nome = '', idade = '', email = '', senha = '', **kwargs):
        super().__init__(**kwargs)
        self.loadData()
        self.a = NULL
        self.nome = nome
        self.idade = idade
        self.email = email
        self.senha = senha        

    def signin(self):
        self.nome = str(self._name.text)
        self.idade = str(self._age.text)
        self.email = str(self._email.text)
        self.senha = str(self._password.text)

        if self.nome == '' or self.idade == '' or self.email == '' or self.senha == '':
            print('Preencha os campos obrigatórios!')
        elif self.nome in self.users_list:
            print('Esse usuário já existe, deseja logar?')
        else:
            self.users_list.append(self.nome)
            self.saveData()
            print('Cadastrado!')
            print(f"Lista de usuários: {self.users_list}")
            self.parent.ids.mn.ids.login_button.text = self.nome
            self.parent.ids.mn.ids.signin_button.text = "Logout"
            self.parent.current = 'main_menu'
            #usuário = [self.nome, self.idade, self.email, self.senha]
            #print(f"""
            #Nome: {nome}
            #Idade: {idade}
            #Email: {email}
            #Senha: {senha}
            #""")
            database.database_save(self.nome, self.idade, self.email, self.senha)
        
    def saveData(self):
        with open('users.json', 'w') as data:
            json.dump(self.users_list, data)

    def loadData(self):
        with open('users.json', 'r') as data:
            self.users_list = json.load(data)
            
class Login(Screen):
    pass

class Products(BoxLayout):
    def __init__(self, name = '', price = '', seller = '', id = 1, amount = 1, **kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.ids.product_name_card.text = name
        self.ids.product_price_card.text = price
        self.ids.product_seller_card.text = seller
        self.amount = amount

class Admin(Screen):
    _nomeproduto = ObjectProperty(None)
    _precoproduto = ObjectProperty(None)

    #def usa_modulo(x):
    #    database.print_nome()

    def addProducts(self):
        nome = self._nomeproduto.text
        price = self._precoproduto.text
        seller = self.parent.ids.sgn._name.text
        self.parent.ids.mn._telaprodutos.add_widget(Products(nome, price, seller))
        return nome

class Config(Screen):
    def teste():
        a = input("Qual seu nome?")
        print(f"Olá {a} seja bem vindo!")
        return a
    # def outro_test(self):
    #     siginIntance = Signin()
    #     siginIntance.test()
    #     print(f"Nome do vendedor: {siginIntance.nome}")
    #     print(f"10/2 = "+str(siginIntance.a))
    pass


class OriShop(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    OriShop().run()