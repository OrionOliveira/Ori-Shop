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

    def Signed(self):
        if self.ids.signin_button.text == 'Logout':
            self.ids.sigin_button.text = 'Signin'
        self.ids.login_button.text = self.parent.ids.sgn.seller.text

    def removeProduct(self):
        self.ids.box_shop.remove_widget()

class Signin(Screen):
    seller = ObjectProperty(None)
    def __init__(self, nome = '', idade = '', email = '', senha = '', cadastro = False, **kwargs):
        super().__init__(**kwargs)
        self.a = NULL
        self.nome = nome
        self.cadastro = cadastro

    def signin(self):
        if self.cadastro == False:
            self.nome = str(self.seller.text)
            self.cadastro = True
            print('Cadastrado!')
        return 
        
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