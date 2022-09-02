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
    def signin(self):
        #user_age = self.ids.user_age.text
        #user_email = self.ids.user_email.text
        #user_password = self.ids.user_password.text
        # global nomevendedor
        print(self.seller.text)
        pass

class Admin(Screen):
    _nomeproduto = ObjectProperty(None)
    _precoproduto = ObjectProperty(None)

    def addProducts(self):
        #self.parent.ids.prd.product_name_card.text = self._nomeproduto.text
        print(f"""
        Nome do Vendedor: ???
        Produto: {self._nomeproduto.text} 
        Price: ${self._precoproduto.text}""")
        # print(f"Nome do vendedor é: {_vendedor_nome}")
        
class Login(Screen):
    pass

class Products(BoxLayout):
    # Criar subclasses, contendo uma tela para cada produto
    def __init__(self, name = '', price = '', seller = '', **kwargs):
        super().__init__(**kwargs)
        name = self.ids.product_name_card.text
        price = self.ids.product_price_card.text
        seller = self.ids.product_seller_card.text

class OriShop(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    OriShop().run()