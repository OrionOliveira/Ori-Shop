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
    pass

class Signin(Screen):
    seller = ObjectProperty(None)
    trocatxt = ObjectProperty(None)
    def __init__(self, nome = '', idade = '', email = '', senha = '', cadastro = False, **kwargs):
        super().__init__(**kwargs)
        self.a = NULL
        self.nome = nome

    def test(self):
        self.a = 5
        print(self.a)

    def signin(self):
        self.nome = self.seller.text
        age = self.ids.user_age.text
        email = self.ids.user_email.text
        password = self.ids.user_password.text
        print(self.nome) 
        
class Login(Screen):
    pass

class Products(BoxLayout):
    # Criar subclasses, contendo uma tela para cada produto
    def __init__(self, name = '', price = '', seller = '', **kwargs): #price, seller
        super().__init__(**kwargs)
        self.ids.product_name_card.text = name
        self.name = name
        #self.name = self.ids.product_name_card.text
        self.ids.product_price_card.text = price
        #self.price = self.ids.product_price_card.text
        self.ids.product_seller_card.text = seller
        self.seller = seller

class Admin(Screen):
    _nomeproduto = ObjectProperty(None)
    _precoproduto = ObjectProperty(None)
    #nome_item = Products(name = _nomeproduto.text)

    def addProducts(self):
        produtos = Signin()
        produtos.signin()
        p1 = self.add_widget(Products(self._nomeproduto.text, self._precoproduto.text, str(produtos.name)))
        #self.parent.ids.prd.product_name_card.text = self._nomeproduto.text
        print(f"""
        Nome do Vendedor: {produtos.seller.text}
        Produto: {self._nomeproduto.text} 
        Price: ${self._precoproduto.text}""")

class Config(Screen):

    def outro_test(self):
        siginIntance = Signin()
        siginIntance.test()
        #siginIntance.signin()
        print(f"Nome do vendedor: {siginIntance.x}")
        print(f"10/2 = "+str(siginIntance.a))

class OriShop(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    OriShop().run()