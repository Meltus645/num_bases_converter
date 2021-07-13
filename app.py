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
    def convert(self, args):
        val =int(self.input.text, 2)
        self.converted.text =str(val)
        self.label.text ='in decimal is:'
    def build(self):
        screen =MDScreen()
        
        """ ui widgets """
        # toolbar
        self.toolbar =MDToolbar(title ="Binary to Decimal")
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
            pos_hint ={'center_x': 0.5, 'center_y': 0.5},
            font_size =22
        )
        screen.add_widget(self.input)
        self.label =MDLabel(
            halign ='center',
            pos_hint ={'center_x': 0.5, 'center_y': 0.35},
            theme_text_color ="Secondary"
        )
        # output
        self.converted =MDLabel(
            halign ='center',
            pos_hint ={'center_x': 0.5, 'center_y': 0.3},
            theme_text_color ="Primary",
            font_style ="H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)
        
        # convert button
        screen.add_widget(MDFillRoundFlatButton(
                text ="Convert",
                font_size =17,
                pos_hint ={'center_x': 0.5, 'center_y': 0.15},
                on_press =self.convert
            )
        )
        return screen

if __name__ == '__main__':
    app =MainApp()
    app.run()