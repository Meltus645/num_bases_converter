from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton,MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class MainApp(MDApp):
    def flip(self):
        if self.state ==0:
            self.state =1
            self.toolbar.title ="Decimal to Binary"
            self.input.text ="enter decimal number"
            self.converted.text =""
            self.label.text =""
        else:
            self.state =0
            self.toolbar.title ="Binary to Decimal"
            self.input.text ="enter binary number"
            self.converted.text =""
            self.label.text =""
            
    def convert(self, args):
        if self.input.text !="":
            val =int(self.input.text, 2)
            self.converted.text =str(val)
            self.input_label.text =''
            self.label.text ='in decimal is:'
        else:
            self.input_label.font_size =14
            self.input_label.text ='this field is required!'
            
    def build(self):
        self.state =0
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
            text ='',
            halign ='center',
            size_hint =(0.8, 1),
            pos_hint ={'center_x': 0.5, 'center_y': 0.5},
            font_size =22
        )
        screen.add_widget(self.input)
        self.input_label =MDLabel(
            text ='enter a binary number',
            halign ='center',
            pos_hint ={'center_x': 0.5, 'center_y': 0.45},
            theme_text_color ="Secondary"
        )
        screen.add_widget(self.input_label)
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