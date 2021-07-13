from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton,MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class MainApp(MDApp):
    def flip(self):
        print('flipping ...')
    def build(self):
        screen =MDScreen()
        
        """ ui widgets """
        # toolbar
        self.toolbar =MDToolbar(title ="Bin2Dec Converter")
        self.toolbar.pos_hint ={"top": 1}
        self.toolbar.right_action_items =[ 
            ["rotate-3d-variant",lambda x: self.flip()]
        ]
        screen.add_widget(self.toolbar)
        
        # logo
        screen.add_widget(Image(
            source ='logo.png',
            pos_hint ={'center_x': 0.5, 'center_y': 0.7}
           )
        )
        # user input
        self.input =MDTextField(
            text ='enter a binary number',
            halign ='center',
            size_hint =(0.8, 1),
            pos_hint ={'center_x': 0.5, 'center_y': 0.45},
            font_size =22
        )
        screen.add_widget(self.input)
        self.label =MDLabel(
            text ='in decimal is:',
            halign ='center',
            pos_hint ={'center_x': 0.5, 'center_y': 0.35},
            theme_text_color ="Secondary"
        )
        screen.add_widget(self.label)
        return screen

if __name__ == '__main__':
    app =MainApp()
    app.run()