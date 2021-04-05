from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string("""
                                
GridLayout:
    cols: 2
    spacing: 20
    
    Button:
        text: "Click 1"
        
    Button:
        text: "Click 2"
        
    Button:
        text: "Click 3"
    
    Button:
        text: "Click 4"
    
    Button:
        text: "Click 5"
        
    Button:
        text: "Click 6"
        
    Button:
        text: "Click 7"
    
    Button:
        text: "Click 8"
                                       
        
""" ))
