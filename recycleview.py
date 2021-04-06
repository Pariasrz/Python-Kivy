from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView

Builder.load_string("""

<rv>:
    viewclass: "Button"
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'

""")

class rv(RecycleView):

    def __init__(self,**kwargs):
        super(rv, self).__init__(**kwargs)
        self.data=[{'text': str(x)} for x in range(100)]

class rvapp(App):
    def build(self):
        return rv()

if __name__== '__main__':
    rvapp().run()
