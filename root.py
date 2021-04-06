from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string("""
                                
Label:
    
    Button:
        text: "Click 1"
        pos: root.x, root.top - self.height
        
    Button:
        text: "Click 2"
        pos : root.right - self.width, root.y 
        
    Button:
        text: "Click 3"
        pos : root.x , root.y 
        
    Button:
        text: "Click 4"
        pos: root.right - self.width, root.top - self.height
                                                               
"""))
