from kivy.app import App
from kivy.uix.switch import Switch
from kivy.uix.gridlayout import GridLayout

class switchapp(GridLayout):

    def __init__(self,**kwargs):
        super(switchapp,self).__init__(**kwargs)
        
        self.cols = 2
        self.sw=Switch(active = False)
        self.add_widget(self.sw)
        self.sw.bind(active = switch_value)

def switch_value(switchObject, switchValue):
    if (switchValue):
        print ("Switch On")
    else:
        print("Switch Off")

class mainapp(App):
    def build(self):
        return switchapp()
    
mainapp().run()
