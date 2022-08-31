from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class Manager(ScreenManager):
    pass

class Menu(Screen):
    produtos = {}

    def addProducts(self):
        self.ids.box_shop.add_widget(Products(name = 'notebook', price = '$4,200', seller = 'Orion'))

class Signin(Screen):
    def singin(self):
        user_name = self.ids.user_name.text
        user_age = self.ids.user_age.text
        user_email = self.ids.user_email.text
        user_password = self.ids.user_password.text
        
class Admin(Screen):
    pass

class Login(Screen):
    pass

class Products(BoxLayout):
    # Criar subclasses, contendo uma tela para cada produto
    def __init__(self, name = '', price = '', seller = '', **kwargs):
        super().__init__(**kwargs)
        name = self.ids.product_name.text
        price = self.ids.product_price.text
        seller = self.ids.product_seller.text

class OriShop(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    OriShop().run()