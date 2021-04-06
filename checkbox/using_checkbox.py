from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout

class CheckApp(GridLayout):
    
    def __init__(self, **kwargs):
        super(CheckApp, self).__init__(**kwargs)
            
        self.cols = 2
        self.add_widget(Label(text = "Male"))
        self.active = CheckBox(active = False)
        self.add_widget(self.active)
            
        self.add_widget(Label(text = "Female"))
        self.active = CheckBox(active = False)
        self.add_widget(self.active)
        
        self.add_widget(Label(text = "Other"))
        self.active = CheckBox(active = False)
        self.add_widget(self.active)
            
class checkboxapp(App):
    def build(self):
        return CheckApp()
 
checkboxapp().run()
