from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string("""

RelativeLayout:
    ToggleButton:
        size_hint: None, None
        size: 0.25*root.width, 0.25*root.height
        pos : 0.125*root.width, 0.350*root.height
        text: "Toggle Button"
        group: "geometry"
                        
"""))
