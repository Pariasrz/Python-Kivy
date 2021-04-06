from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label

class myapp(GridLayout):
    
    def __init__(self):
        super(myapp,self).__init__()
        
        self.cols = 2
        
        self.myslider = Slider(min = 0, max = 100)
        self.add_widget(self.myslider)
        
        self.lblvalue = Label(text = "Slider Value")
        self.add_widget(self.lblvalue)
        self.myslider.bind(value = self.onvalue)
        
    def onvalue(self, instance, b):
        self.lblvalue.text = "% d" % b
        
class sliderapp(App):
    def build(self):
        return myapp()

sliderapp().run()
