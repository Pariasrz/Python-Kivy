from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner

s = Spinner(text = "Home", values = ("Home", "Work", "Shop"),
            size_hint = (None, None),
            size = (100, 44),
            pos_hint = {'center_x' : .5, 'center_y' : .5})


def show_value(spinner, text):
    print("Spinner Text:", text)   

s .bind(text = show_value)
         
runTouchApp(s)
