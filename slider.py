from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string("""

BoxLayout:
    
    padding: 50
    
    Slider:
        max: 450
        value: 20
        id : s1
        
    ProgressBar:
        max: 450
        value: s1.value

        
"""))
