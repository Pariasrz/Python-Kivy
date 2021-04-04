from kivy.app import App
from kivy.uix.label import Label
class firstapp(App):
    def build(self):
        return Label(text="Hello world", font_size=60)
    
firstapp().run()
