from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string("""
                                
BoxLayout:
    
    orientation: 'vertical'
    spacing: 10
    
    Button:
        text: 'Click 1'
        
    Button:
        text: 'Click 2'
        
    Button:
        text: 'Click 3'
                                       
        
""" ))


#or we use the code below
