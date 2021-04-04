from kivy.app import App

#label
from kivy.uix.label import Label
class firstapp(App):
    def build(self):
        return Label(text="Hello world", font_size=60)
    
firstapp().run()

#button
from kivy.uix.button import Button
class firstapp(App):
    def build(self):
        return Button(text="Hello world", font_size=60)
    
firstapp().run()
