from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton,MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class MainApp(MDApp):
    def flip(self):
        if self.state ==0:
            self.state =1
            self.toolbar.title ="Decimal to Binary"
            self.input_label.text ="Enter a decimal number"
            self.converted.text =""
            self.input.text =''
            self.label.text =""
        else:
            self.state =0
            self.toolbar.title ="Binary to Decimal"
            self.input_label.text ="Enter a binary number"
            self.converted.text =""
            self.input.text =''
            self.label.text =""
            
    def convert(self, args):
        if self.input.text =="":
            self.error_label.font_size =14
            self.error_label.text ='This field is required!'
        else:
            if self.state ==0:
                val =int(self.input.text, 2)
                self.converted.text =str(val)
                self.error_label.text =''
                self.label.text ='In Decimal is:'
            else:
                val =bin(int(self.input.text))[2:]
                self.converted.text =val
                self.error_label.text =''
                self.label.text ='In Binary is:'
            
    def build(self):
        self.state =0
        self.title ="Number Bases Converter"
        self.theme_cls.font_styles["JetBrainsMono"] = [
            "JetBrainsMono",
            16,
            False,
            0.15,
        ]
        self.theme_cls.primary_hue = "600"
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
        self.input_label =MDLabel(
            text ='Enter a binary number',
            halign ='left',
            pos_hint ={'center_x': 0.6, 'center_y': 0.55},
            theme_text_color ="Secondary",
            font_size =15
        )
        screen.add_widget(self.input_label)
        self.input =MDTextField(
            text ='',
            halign ='left',
            size_hint =(0.8, 1),
            pos_hint ={'center_x': 0.5, 'center_y': 0.5},
            font_size =15
        )
        screen.add_widget(self.input)
        self.error_label =MDLabel(
            text ='',
            halign ='left',
            pos_hint ={'center_x': 0.6, 'center_y': 0.45},
            theme_text_color ="Error"
        )
        screen.add_widget(self.error_label)
        self.label =MDLabel(
            halign ='center',
            pos_hint ={'center_x': 0.5, 'center_y': 0.42},
            theme_text_color ="Secondary"
        )
        # output
        self.converted =MDLabel(
            halign ='center',
            pos_hint ={'center_x': 0.5, 'center_y': 0.37},
            theme_text_color ="Primary",
            font_style ="H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)
        
        # convert button
        screen.add_widget(MDRectangleFlatButton(
                text ="Convert",
                font_size =17,
                pos_hint ={'center_x': 0.5, 'center_y': 0.25},
                on_press =self.convert
            )
        )
        return screen

if __name__ == '__main__':
    app =MainApp()
    app.run()