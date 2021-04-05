from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        
        btn = Button(text = 'Push me' , size_hint = (.2, .2), 
                     background_color = (1,0,1,1),
                     color = (1,1,1,1),
                     pos = (100,290))

#background_normal = 'a.png', background_down = 'b.png'

        btn.bind(on_press = self.myfunc)
        
        return btn
    def myfunc(self, event):
        print("Button Pressed!")



ButtonApp().run()
