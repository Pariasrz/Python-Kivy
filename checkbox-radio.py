
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string("""

GridLayout:
    cols: 4
    CheckBox:
        active: True
    
    CheckBox:
        group: "Radio Button"
        active: True
    
    CheckBox: 
        group: "Radio Button"
        active: False
        
    Label:
        text: "Radio Button"
              
"""))


