from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from DatabaseFiles import connection_database, user_database, products_database
from Telas import signin
from kivy.graphics import *

class Manager(ScreenManager):
    pass

class Menu(Screen):
    _telaprodutos = ObjectProperty(None)

    def removeProduct(self):
        self.ids.box_shop.remove_widget()

    def resignin(self):
        btn_name = self.ids.signin_button.text

        if btn_name == 'Logout':
            self.ids.login_button.text = 'Login'
            self.ids.signin_button.text = 'Signin'
        elif btn_name == 'Signin':
            self.parent.ids.sgn._name.text = ''
            self.parent.ids.sgn._age.text = ''
            self.parent.ids.sgn._email.text = ''
            self.parent.ids.sgn._password.text = ''
            self.parent.current = 'signin'

class Signin(Screen):
    _name = ObjectProperty(None)
    _age = ObjectProperty(None)
    _email = ObjectProperty(None)
    _password = ObjectProperty(None)

    def signin(self):
        self.nome = str(self._name.text)
        self.idade = str(self._age.text)
        self.email = str(self._email.text)
        self.senha = str(self._password.text)

        if self.nome == '' or self.idade == '' or self.email == '' or self.senha == '':
            print('Preencha os campos obrigatórios!')
        else:
            global email
            self.parent.ids.mn.ids.login_button.text = self.nome
            self.parent.ids.mn.ids.signin_button.text = "Logout"
            self.parent.current = 'main_menu'
            self.cadastro = True
            email = self.email
            user_database.database_save(self.nome, self.idade, self.email, self.senha)
            print("\033[32mSignin sucessfuly!")

class Login(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def __init__(self, nome = '', idade = '', emaill = '', senhaa = '', login = False, **kwargs):
        super().__init__(**kwargs)
        self.login = login
        self.nome = nome
        self.idade = idade
        self.email = emaill
        self.senha = senhaa

    def logar(self):
        if Login().login == False:
            c = user_database.login(self.email.text, self.password.text)
            if c == False:
                pass 
            else:
                global email
                self.nome = c[1]
                self.idade = c[2]
                self.emaill = c[3]
                email = self.emaill
                self.senhaa = c[4]
                self.login = True
                self.parent.current = 'user'
                self.email.text = ''
                self.password.text = ''
                self.parent.ids.mn.ids.login_button.text = self.nome
                self.parent.ids.mn.ids.signin_button.text = 'Logout'
                print("\033[32mLogin sucessfuly!\033[m")
        else:
            return self.nome, self.senhaa, self.emaill, self.password
        

class Products(BoxLayout):
    def __init__(self, name = '', price = '', seller = '', **kwargs):
        super().__init__(**kwargs)
        self.ids.product_name_card.text = name
        self.ids.product_price_card.text = price
        self.ids.product_seller_card.text = seller

email = ''
class User(Screen):
    _nomeproduto = ObjectProperty(None)
    _precoproduto = ObjectProperty(None)

    def addProducts(self):
        signin.print_oi()
        global email
        products_database.addProducts(self._nomeproduto.text, self._precoproduto.text)
        print(f"\033[32mO item {self._nomeproduto.text} foi adicionado ao banco de dados!\033[m")
        x = user_database.dt_user_info(email)
        nome_p = self._nomeproduto.text
        price = (f"\033[33mR${str(self._precoproduto.text)}\033[m")
        seller = x[0]
        self.parent.ids.mn._telaprodutos.add_widget(Products(nome_p, price, seller))

class OriShop(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    OriShop().run()