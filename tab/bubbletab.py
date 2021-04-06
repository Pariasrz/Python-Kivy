from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

class tab(TabbedPanel):
    Builder.load_file("tab.kv")

class tabwidget(App):
    def build(self):
        return tab()

tabwidget().run()
