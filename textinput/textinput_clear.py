from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class btntext(App):
    def build(self):
        
        self.box = BoxLayout(orientation = "horizontal" , spacing = 20)
        self.txt = TextInput(hint_text = "Write Here", size_hint = (.5, .1))
        self.btn = Button(text = "Clear All", size_hint = (.1 ,.1), on_press = self.cleartext)

        self.box.add_widget(self.txt)
        self.box.add_widget(self.btn)

        return self.box        
    
    def cleartext(self, instance):
        self.txt.text = ''


btntext().run()
