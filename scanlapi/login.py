# import cv2
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog


class Login(Screen):
    def logger(self, app):
        print(self.ids)
        # print(dir(self.parent))
        self.parent.current = "photo"
        # self.parent.manager.transition.direction = "right"
        # self.root.ids.welcome_label.text = f' bienvenu(e) {self.root.ids.user.text}!'


class Photo(Screen):
    dialog = None
    theme_style = "Dark"
    primary_palette = "BlueGray"

    def clear(self):
        print(dir(self.parent))
        # clear or reset text_input_matricule
        self.ids.input_input_matricule.text = ""

    def close_dialogue(self, *args, **kwargs):
        if self.dialog:
            self.dialog.dismiss()

    def valide(self,  *args, **kwargs):
        self.parent.current = "resultat"
        print("valide or submit")
        self.close_dialogue()

    def open_dialogue(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="voulez vous soumettre ce numéro de plaque?",
                buttons=[
                    MDFlatButton(
                        text="OUI",
                        theme_text_color="Custom",
                        # text_color=self.primary_color,
                        on_release=self.valide
                    ),
                    MDFlatButton(
                        text="ANNULER",
                        theme_text_color="Custom",
                        # text_color=self.primary_color,
                        on_release=self.close_dialogue
                    ),
                ],
            )
        self.dialog.open()


class Resultat(Screen):
    pass


class WindowManager(ScreenManager):
    pass

# kv = Builder.load_file('essai.kv')


class MainApp(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('essai.kv')

    def clear(self):  # la fonction qui supprime dans login.kv
        self.root.ids.welcome_label.text = "BIENVENU(E)"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

    def ouverture_camera(self):
        print("ouverture camera!!!")


MainApp().run()
