from asyncio.windows_events import NULL
from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class random(BoxLayout):
    pass

class Manager(ScreenManager):
    pass

class Menu(Screen):
    _telaprodutos = ObjectProperty(None)

    def novoproduto(self):
        x = Admin()
        x.add()
        self.ids.box_shop.add_widget(Products(x._nomeproduto.text, x._precoproduto.text, x._nomeadmin.title))

class Signin(Screen):
    seller = ObjectProperty(None)
    trocatxt = ObjectProperty(None)
    def __init__(self, nome = '', idade = '', email = '', senha = '', cadastro = True, **kwargs):
        super().__init__(**kwargs)
        self.a = NULL
        self.nome = nome
        self.cadastro = cadastro

    def test(self):
        self.a = 5
        print(self.a)

    def signin(self):
        self.nome = str(self.seller.text)
        print(self.nome)
        return self.nome
        
class Login(Screen):
    pass

class Products(BoxLayout):
    # Criar subclasses, contendo uma tela para cada produto
    def __init__(self, name = '', price = '', seller = '', **kwargs): #price, seller
        super().__init__(**kwargs)
        self.ids.product_name_card.text = name
        #self.name = self.ids.product_name_card.text
        self.ids.product_price_card.text = price
        #self.price = self.ids.product_price_card.text
        self.ids.product_seller_card.text = seller

class Admin(Screen):
    _nomeproduto = ObjectProperty(None)
    _precoproduto = ObjectProperty(None)
    _nomeadmin = ObjectProperty(None)
    #nome_item = Products(name = _nomeproduto.text)

    def addProducts(self):
        self.parent.ids.mn._telaprodutos.add_widget(Products(self._nomeproduto.text, self._precoproduto.text, self._nomeadmin.title))

class Config(Screen):

    def outro_test(self):
        siginIntance = Signin()
        siginIntance.test()
        #siginIntance.signin()
        print(f"Nome do vendedor: {siginIntance.nome}")
        print(f"10/2 = "+str(siginIntance.a))

class OriShop(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    OriShop().run()