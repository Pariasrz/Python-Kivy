from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string("""
                                
PageLayout:
    Button:
        text: "Click 1"
    
    Button:
        text: "Click 2"
        
    Button:
        text: "Click 3"
                                       
        
""" ))

#we can drag pages
