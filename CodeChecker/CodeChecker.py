# Library can be installed using Anaconda Poershell Promt: 
# 1) activate main
# 2) conda install -c conda-forge kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import time

class CodeChecker(App):
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.35, 0.65)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # image widget
        self.window.add_widget(Image(source="error.png"))

        # label widget
        self.askforerror = Label(
                        text= "Podaj numer błędu",
                        font_size= 18,
                        color= '#00FFCE'
                        )
        self.window.add_widget(self.askforerror)

        # text input widget
        self.user = TextInput(
                    multiline= False,
                    halign="center",
                    font_size = 24,
                    #padding_x= (20,20),
                    #padding_y= (20,20),
                    size_hint= (1,0.6)
                    )
        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                      text= "Sprawdź",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#00FFCE'
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        
        # label widget
        self.response = Label(
                        text= "",
                        font_size= 20,
                        color= '#00FFCE'
                        )
        self.window.add_widget(self.response)

        return self.window


    def callback(self, instance):
        if self.user.text == "100":
            self.response.text = "Kod błędu 100: \n" + dictionary["100"]
            self.user.text = ''
        elif self.user.text == "200":
            self.response.text = "Kod błędu 200: \n" + dictionary["200"]
            self.user.text = ''
        elif self.user.text == "300":
            self.response.text = "Kod błędu 300: \n" + dictionary["300"]
            self.user.text = ''
        else:
            self.response.text = "Kod błędu " + self.user.text + ": \nNieznany błąd. Skontaktuj się z serwisem!"
            self.user.text = ''


dictionary = {
        "100": "Minął termin ważności przeglądu!", 
        "200": "Popsuta pompa!", 
        "300": "Popsuta sprężarka"
        }

# Run CodeChecker
if __name__ == "__main__":
    CodeChecker().run()