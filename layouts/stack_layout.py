from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string("""
                                
StackLayout:
    orientation: 'bt-lr'
    spacing: 20
    padding: 25
    
    
    Button:
        text: "Click 1"
        size_hint: .2, .1
    
    Button:
        text: "Click 2"
        size_hint: .2, .1
        
    Button:
        text: "Click 3"
        size_hint: .2, .1
        
    Button:
        text: "Click 4"
        size_hint: .2, .1
    
    Button:
        text: "Click 5"
        size_hint: .2, .1
        
    Button:
        text: "Click 6"
        size_hint: .2, .1
                                       
        
""" ))

#LR: Left to Right
#RL: Right to Left
#TB: Top to Buttom
#BT: Bottom to Top
#default is LR, TB
