from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton,MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class MainApp(MDApp):
    def build(self):
        screen =MDScreen()
        
        """ ui widgets """
        # toolbar
        self.toolbar =MDToolbar(title ="Bin2Dec Converter")
        self.toolbar.pos_hint ={"top": 1}
        screen.add_widget(self.toolbar)
        return screen

if __name__ == '__main__':
    app =MainApp()
    app.run()