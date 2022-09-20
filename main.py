from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from DatabaseFiles import database
from telas import Config as cf

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

l = ''
class Signin(Screen):
    _name = ObjectProperty(None)
    _age = ObjectProperty(None)
    _email = ObjectProperty(None)
    _password = ObjectProperty(None)
    
    def __init__(self, nome = '', idade = '', email = '', senha = '', cadastro = False, **kwargs):
        super().__init__(**kwargs)
        self.nome = nome
        self.idade = idade
        self.email = email
        self.senha = senha
        self.cadastro = cadastro

    def signin(self):
        self.nome = str(self._name.text)
        self.idade = str(self._age.text)
        self.email = str(self._email.text)
        self.senha = str(self._password.text)

        if self.nome or self.idade or self.email or self.senha == '':
            print('Preencha os campos obrigatórios!')
        else:
            self.parent.ids.mn.ids.login_button.text = self.nome
            self.parent.ids.mn.ids.signin_button.text = "Logout"
            self.parent.current = 'main_menu'
            self.cadastro = True
            l = self.email
            database.database_save(self.nome, self.idade, self.email, self.senha)

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
            c = database.login(self.email.text, self.password.text)
            if c == False:
                print('Tenta denovo')      
            else:
                self.nome = c[1]
                self.idade = c[2]
                self.emaill = c[3]
                self.senhaa = c[4]
                self.login = True
                self.parent.current = 'user'
                self.email.text = ''
                self.password.text = ''
                self.parent.ids.mn.ids.login_button.text = self.nome
                self.parent.ids.mn.ids.signin_button.text = 'Logout'
                l = self.email.text
        else:
            return self.nome, self.senhaa, self.emaill, self.password
        
class Config(Screen):
    def trocar_tema(self, tema):
        c = cf.theme(tema)
        print(c)
        #self.ids.color.rgba = c

class Products(BoxLayout):
    def __init__(self, name = '', price = '', seller = '', **kwargs):
        super().__init__(**kwargs)
        self.ids.product_name_card.text = name
        self.ids.product_price_card.text = price
        self.ids.product_seller_card.text = seller

class User(Screen):
    _nome_user = ObjectProperty(None)
    _age_user = ObjectProperty(None)
    _email_user = ObjectProperty(None)
    _password_user = ObjectProperty(None)
    _nomeproduto = ObjectProperty(None)
    _precoproduto = ObjectProperty(None)

    def addProducts(self):
        database.addProducts(self._nomeproduto.text, self._precoproduto.text)
        x = database.dt_user_info(l)
        print(x)
        nome_p = self._nomeproduto.text
        price = (f"R${self._precoproduto.text}")
        #seller = x[0]
        #seller = self.parent.ids.sgn._name.text
        seller = "Orion"
        self.parent.ids.mn._telaprodutos.add_widget(Products(nome_p, price, seller))

class OriShop(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    OriShop().run()