
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string("""

GridLayout:
    CheckBox:
        size_hint_y : None
        height: '500dp'
        active: True
"""))
