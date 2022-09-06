from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class Manager(ScreenManager):
    pass

class Menu(Screen):
    pass

class Signin(Screen):
    seller = ObjectProperty(None)
    nome_do_cara = seller
    def __init__(self, nome = '', idade = '', email = '', senha = '', cadastro = False, **kwargs):
        super().__init__(**kwargs)

    def signin(self):
        nome = self.seller.text
        age = self.ids.user_age.text
        email = self.ids.user_email.text
        password = self.ids.user_password.text
        print(self.seller.text)
        return nome, age, email, password
        
class Login(Screen):
    pass

class Products(BoxLayout):
    # Criar subclasses, contendo uma tela para cada produto
    def __init__(self, name = '', price = '', seller = '', **kwargs): #price, seller
        super().__init__(**kwargs)
        self.ids.product_name_card.text = name
        self.ids.product_price_card.text = price
        #Signin.seller.text = seller

class Admin(Screen):
    _nomeproduto = ObjectProperty(None)
    _precoproduto = ObjectProperty(None)
    #nome_item = Products(name = _nomeproduto.text)
    def addProducts(self):
        p1 = self.add_widget(Products(self._nomeproduto.text, self._precoproduto.text))
        #self.parent.ids.prd.product_name_card.text = self._nomeproduto.text
        print(f"""
        Nome do Vendedor: ???
        Produto: {self._nomeproduto.text} 
        Price: ${self._precoproduto.text}""")
        # print(f"Nome do vendedor é: {_vendedor_nome}")

class Config(Screen):
    pass

class OriShop(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    OriShop().run()