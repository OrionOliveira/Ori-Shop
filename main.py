from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, ListProperty
from DatabaseFiles import user_database, products_database
from kivy.graphics import *

class Manager(ScreenManager):
    pass

class Menu(Screen):
    _telaprodutos = ObjectProperty(None)
    dinheiro = ObjectProperty(None)

    def test(self):
        products_database.info_product('', '', '', 'Lorena', '')

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

class Botao(ButtonBehavior, Label):
    cor = ListProperty([1, 0.25, 0.4, 1])
    cor2 = ListProperty([0.7, 0.1, 0.3, 1])

    def __init__(self, **kwargs):
        super(Botao, self).__init__(**kwargs)
        self.atualizar()

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def on_press(self, *args):
        self.cor, self.cor2 = self.cor2, self.cor

    def on_release(self, *args):
        self.cor, self.cor2 = self.cor2, self.cor

    def on_cor(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()      
        with self.canvas.before:
            Color(rgba = self.cor)
            Ellipse(pos = (self.pos), 
                    size = (self.height, self.height))
            Ellipse(pos = (self.x + self.width - self.height, self.y), 
                    size = (self.height, self.height))
            Rectangle(pos = (self.x + self.height / 2, self.y), 
                    size = (self.width - self.height, self.height))

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
                self.parent.ids.usr._nomevendedor.title = self.nome
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
                self.parent.ids.mn.ids.wallet_button.text = str(f"R${self.parent.ids.tyc.user_money.text}.00")
                print("\033[32mLogin sucessfuly!\033[m")
        else:
            return self.nome, self.senhaa, self.emaill, self.password

class Products(BoxLayout):
    def __init__(self, id = 0, name = '', price = '', seller = '', amount = 1, **kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.ids.product_name_card.text = name
        self.ids.product_price_card.text = price
        self.ids.product_seller_card.text = seller
        self.amount = amount

class User(Screen):
    _nomeproduto = ObjectProperty(None)
    _precoproduto = ObjectProperty(None)
    _nomevendedor = ObjectProperty(None)
    _qtdproduto = ObjectProperty(None)
    _dinheirousuario = ObjectProperty(None)

    def addProducts(self):
        amounT = self._qtdproduto.text
        n = 0
        while n < int(amounT):
            i = products_database.addProducts(self._nomeproduto.text, self._precoproduto.text, self._nomevendedor.title)
            if i[1] == True:
                print(f"\033[32mO item {self._nomeproduto.text} foi adicionado ao banco de dados!\033[m")
                x = user_database.dt_user_info(email)
                id = i
                nome_p = self._nomeproduto.text
                price = (f"R${self._precoproduto.text}")
                seller = x[0]
                self.parent.ids.mn._telaprodutos.add_widget(Products(id, nome_p, price, seller, amounT))
            elif i[1] == False:
                products_database.updateAmount(i[0], i[2])
                x = user_database.dt_user_info(email)
                id = i
                nome_p = self._nomeproduto.text
                price = (f"R${self._precoproduto.text}")
                seller = x[0]
                self.parent.ids.mn._telaprodutos.add_widget(Products(id, nome_p, price, seller, amounT))
                print(f"Foram adicionados +{str(amounT)} itens...")
            n = n + 1
    
    def buy_product(self):
        self._dinheirousuario.text = self.parent.ids.mn.ids.wallet_button.text
        money = self._dinheirousuario.text.replace('R$', '')
        if float(money) >= int(self._precoproduto.text):
            print("Pode comprar!")
        else:
            print("Não pode comprar")
        
class Tycoon(Screen):
    user_money = ObjectProperty(None)
    generators = ["Simple Generator"]

    def addMoney(self):
        self.user_money.text = str(int(self.user_money.text) + 1)
        self.parent.ids.mn.ids.wallet_button.text = str(f"R${self.user_money.text}.00")
        self.parent.ids.usr.ids.user_money.text = str(f"{self.user_money.text}.00")
    
    def addGenerator(self):
        if int(self.user_money.text) == 14:
            print("É maior")
            x = self.ids.tycoon_box.add_widget(Tycoon_Area(button_name = (f"{self.generators[0]} R$30,00 to buy")))
        else:
            pass

class Tycoon_Area(BoxLayout):
    def __init__(self, button_name = '', **kwargs):
        super().__init__(**kwargs)
        self.ids.Area_Button.text = button_name
    pass

class OriShop(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    OriShop().run()