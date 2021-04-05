from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

class testapp(App):
    Window.size = (320, 260)
    title = "My Application"
    
    def build(self):
        return Button(text = "Hello")


testapp().run()
