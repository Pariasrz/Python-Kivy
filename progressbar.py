from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string("""

BoxLayout:
    ProgressBar:
        id : bar
        max: 10
        value: 2
        
"""))
