from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string("""
                                
ActionBar:
    
    pos_hint : {'top': 1}
    
    ActionView:
        ActionPrevious:
            title: "Menu"
        
        ActionButton: 
            text: "Open"
            
        ActionButton:
            text : "Save"
        
        ActionButton:
            text: "Exit"
                                                               
"""))
