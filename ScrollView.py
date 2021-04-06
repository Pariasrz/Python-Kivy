from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.properties import StringProperty


Builder.load_string("""

<ScrollableLabel>:

    Label:

        text: "My Name is Paria. My Name is Paria. My Name is Paria. My Name is Paria. "
        font_size: 160
        text_size: self.width,None
        size_hint_y: None
        height: self.texture_size[1]
""")

class ScrollableLabel(ScrollView):
    text=StringProperty('')


runTouchApp(ScrollableLabel())
