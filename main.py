from asyncio.windows_events import NULL
from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
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
    seller = ObjectProperty(None)
    users_list = []

    def __init__(self, nome = '', idade = '', email = '', senha = '', cadastro = False, **kwargs):
        super().__init__(**kwargs)
        self.loadData()
        self.a = NULL
        self.nome = nome
        self.cadastro = cadastro

    def signin(self):
        m = Menu()
        m.__init__()
        self.nome = str(self.seller.text)
        if self.nome == '':
            print('Vai dar não!')
        elif self.nome in self.users_list:
            print('Esse usuário já existe, deseja logar?')
        else:
            self.users_list.append(self.nome)
            #self.cadastro = True
            self.saveData()
            print('Cadastrado!')
            print(f"Lista de usuários: {self.users_list}")
    
    def saveData(self):
        with open('users.json', 'w') as data:
            json.dump(self.users_list, data)

    def loadData(self):
        with open('users.json', 'r') as data:
            self.users_list = json.load(data)
        
class Login(Screen):
    pass

class Products(BoxLayout):
    def __init__(self, name = '', price = '', seller = '', **kwargs):
        super().__init__(**kwargs)
        self.ids.product_name_card.text = name
        self.ids.product_price_card.text = price
        self.ids.product_seller_card.text = seller

class Admin(Screen):
    _nomeproduto = ObjectProperty(None)
    _precoproduto = ObjectProperty(None)

    def addProducts(self):
        self.parent.ids.mn._telaprodutos.add_widget(Products(self._nomeproduto.text, self._precoproduto.text, self.parent.ids.sgn.seller.text))

class Config(Screen):

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