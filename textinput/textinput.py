from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class btntext(App):
    def build(self):
        
        b = BoxLayout(orientation = 'vertical')
        
        t = TextInput(font_size= 30, 
                      size_hint_y = None, 
                      height = 100,
                      password = False,
                      readonly = False)
        
        btn = Button(text = 'Push me' , font_size = "20sp")
        
        b.add_widget(t)
        b.add_widget(btn)
        
        return b


btntext().run()
