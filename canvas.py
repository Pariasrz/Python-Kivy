from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color

class canvaswidget(Widget):
    def __init__(self, **kwargs):
        super(canvaswidget, self).__init__(**kwargs)
        
        with self.canvas:
            Color(.234, .346, .378, .8)
            self.rect = Rectangle(pos = self.center,
                                  size = (self.width/2., self.height/2.)) 
            self.bind(pos = self.updaterec, size = self.updaterec)
            
    def updaterec(self,*args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class canvasapp(App):
    def build(self):
        return canvaswidget()

canvasapp().run()
