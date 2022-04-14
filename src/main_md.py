from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    # Here specify the required parameters for MDTextFieldRound:
    # [...]


class ScanWindow(Screen):
    pass


class LoginWindow(Screen):
    def on_login(self, app):
        # self.current = "scan"
        app.root.current = "scan"
        self.manager.transition.direction = "right"
        print("App....", app)


class InfoWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    def show_name(self):
        print("Bienfait shomari")

    # def build(self):
    #     return Builder.load_file('mainapp.kv')


MainApp().run()
