import json

# simulamos tamaño de celular
from kivy.core.window import Window
Window.size = (360, 640)

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image


# -------------------------------
# FUNCIONES PARA USUARIOS (JSON)
# -------------------------------

def leer_usuarios():
    try:
        with open("usuarios.json", "r") as f:
            return json.load(f)
    except:
        return {}

def guardar_usuarios(data):
    with open("usuarios.json", "w") as f:
        json.dump(data, f)


# -------------------------------
# BARRA SUPERIOR (ROJA)
# -------------------------------

def crear_barra():
    return MDBoxLayout(
        size_hint_y=None,
        height=60,
        md_bg_color=(0.85, 0.2, 0.2, 1)
    )


# -------------------------------
# PANTALLA 1: LOGIN
# -------------------------------

class Login(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = MDBoxLayout(orientation="vertical")
        root.add_widget(crear_barra())

        cont = MDBoxLayout(orientation="vertical", padding=20, spacing=20)

        # Imagen del corazón (debe estar en la misma carpeta)
        img = Image(
            source="heart.png",
            size_hint=(1, None),
            height=120
        )

        # tarjeta donde van los inputs
        card = MDCard(
            orientation="vertical",
            padding=20,
            spacing=15,
            radius=[20],
            size_hint=(1, None),
            height=260
        )

        # campos de entrada
        self.user = MDTextField(
            hint_text="Correo o usuario"
        )

        self.passw = MDTextField(
            hint_text="Contraseña",
            password=True
        )

        # botones
        btn_login = MDRaisedButton(text="Ingresar")
        btn_login.bind(on_press=self.verificar)

        btn_reg = MDRaisedButton(text="Crear cuenta")
        btn_reg.bind(on_press=lambda x: setattr(self.manager, "current", "registro"))

        self.msg = MDLabel(text="", halign="center")

        # agregamos todo
        card.add_widget(self.user)
        card.add_widget(self.passw)
        card.add_widget(btn_login)
        card.add_widget(btn_reg)

        cont.add_widget(img)
        cont.add_widget(card)
        cont.add_widget(self.msg)

        root.add_widget(cont)
        self.add_widget(root)

    def verificar(self, obj):
        datos = leer_usuarios()

        if self.user.text in datos and datos[self.user.text] == self.passw.text:
            self.manager.current = "formulario"
        else:
            self.msg.text = "Datos incorrectos"


# -------------------------------
# PANTALLA 2: REGISTRO
# -------------------------------

class Registro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = MDBoxLayout(orientation="vertical")
        root.add_widget(crear_barra())

        cont = MDBoxLayout(orientation="vertical", padding=20)

        card = MDCard(
            orientation="vertical",
            padding=20,
            spacing=15,
            radius=[20]
        )

        self.user = MDTextField(
            hint_text="Nuevo usuario"
        )

        self.passw = MDTextField(
            hint_text="Contraseña",
            password=True
        )

        btn = MDRaisedButton(text="Guardar")
        btn.bind(on_press=self.guardar)

        self.msg = MDLabel(text="", halign="center")

        card.add_widget(self.user)
        card.add_widget(self.passw)
        card.add_widget(btn)
        card.add_widget(self.msg)

        cont.add_widget(card)
        root.add_widget(cont)
        self.add_widget(root)

    def guardar(self, obj):
        datos = leer_usuarios()

        if self.user.text in datos:
            self.msg.text = "Ese usuario ya existe"
        else:
            datos[self.user.text] = self.passw.text
            guardar_usuarios(datos)
            self.manager.current = "login"


# -------------------------------
# PANTALLA 3: FORMULARIO
# -------------------------------

class Formulario(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = MDBoxLayout(orientation="vertical")
        root.add_widget(crear_barra())

        cont = MDBoxLayout(orientation="vertical", padding=20)

        card = MDCard(
            orientation="vertical",
            padding=15,
            spacing=10,
            radius=[20],
            size_hint=(1, None),
            height=500
        )

        # campos con ejemplos (helper_text)
        self.nombre = MDTextField(hint_text="Nombres")
        self.apellido = MDTextField(hint_text="Apellidos")
        self.edad = MDTextField(hint_text="Edad")

        self.presion = MDTextField(
            hint_text="Presión",
            helper_text="Ej: 100 - 180",
            helper_text_mode="on_focus"
        )

        self.colesterol = MDTextField(
            hint_text="Colesterol",
            helper_text="Ej: 150 - 300",
            helper_text_mode="on_focus"
        )

        self.glucosa = MDTextField(
            hint_text="Glucosa",
            helper_text="Ej: 70 - 200",
            helper_text_mode="on_focus"
        )

        self.tabaco = MDTextField(
            hint_text="Tabaco",
            helper_text="0: No | 1: Ocasional | 2: Frecuente",
            helper_text_mode="on_focus"
        )

        btn = MDRaisedButton(text="Predecir")
        btn.bind(on_press=self.ir_resultado)

        for w in [
            self.nombre, self.apellido, self.edad,
            self.presion, self.colesterol,
            self.glucosa, self.tabaco, btn
        ]:
            card.add_widget(w)

        cont.add_widget(card)
        root.add_widget(cont)
        self.add_widget(root)

    def ir_resultado(self, obj):
        self.manager.get_screen("resultado").calcular(
            self.nombre.text,
            self.apellido.text,
            self.edad.text,
            self.presion.text,
            self.colesterol.text,
            self.glucosa.text,
            self.tabaco.text
        )
        self.manager.current = "resultado"


# -------------------------------
# PANTALLA 4: RESULTADO
# -------------------------------

class Resultado(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = MDBoxLayout(orientation="vertical")
        root.add_widget(crear_barra())

        cont = MDBoxLayout(orientation="vertical", padding=20)

        self.texto = MDLabel(text="Resultado", halign="center")

        cont.add_widget(self.texto)
        root.add_widget(cont)

        self.add_widget(root)

    def calcular(self, nombre, apellido, edad, presion, colesterol, glucosa, tabaco):
        try:
            edad = int(edad)
            presion = int(presion)
            colesterol = int(colesterol)
            glucosa = int(glucosa)
            tabaco = int(tabaco)

            puntos = 0

            if edad > 50: puntos += 2
            if presion > 140: puntos += 3
            if colesterol > 200: puntos += 2
            if glucosa > 126: puntos += 2
            if tabaco == 1: puntos += 1
            if tabaco == 2: puntos += 3

            if puntos <= 2:
                riesgo = "BAJO"
            elif puntos <= 5:
                riesgo = "MEDIO"
            else:
                riesgo = "ALTO"

            self.texto.text = f"{nombre} {apellido}\nRiesgo: {riesgo}"

        except:
            self.texto.text = "Error en datos"


# -------------------------------
# APP PRINCIPAL
# -------------------------------

class AppSalud(MDApp):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(Login(name="login"))
        sm.add_widget(Registro(name="registro"))
        sm.add_widget(Formulario(name="formulario"))
        sm.add_widget(Resultado(name="resultado"))

        return sm


# ejecutamos la app
AppSalud().run()