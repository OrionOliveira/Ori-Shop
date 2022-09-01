from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class Manager(ScreenManager):
    pass

class Menu(Screen):
    box = ObjectProperty()

class Signin(Screen):
    seller = ObjectProperty(None)

    def singin(self):
        user_name = self.ids.user_name.text
        user_age = self.ids.user_age.text
        user_email = self.ids.user_email.text
        user_password = self.ids.user_password.text
        
class Admin(Screen):
    name = ObjectProperty(None)
    price = ObjectProperty(None)

    def addProducts(self):
        Menu.box.add_widget(Products(name = self.name.text, price = self.price, seller = Signin.seller))
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