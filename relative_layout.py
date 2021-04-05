from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout

class Relative_Layout(App):
    def build(self):
        
        r = RelativeLayout()
        
        b1 = Button(text = 'Click 1' , size_hint = (.2, .2), pos_hint= { 'x': 0, 'y': 0})
        b2 = Button(text = 'Click 2' , size_hint = (.2, .2), pos_hint= { 'right': 1, 'y': 0})
        b3 = Button(text = 'Click 3' , size_hint = (.2, .2), pos_hint= { 'center_x': .5, 'center_y': .5})
        b4 = Button(text = 'Click 4' , size_hint = (.2, .2), pos_hint= { 'x': 0, 'top': 1})
        b5 = Button(text = 'Click 5' , size_hint = (.2, .2), pos_hint= { 'right': 1, 'top': 1})
        
        
        r.add_widget(b1)
        r.add_widget(b2)
        r.add_widget(b3)
        r.add_widget(b4)
        r.add_widget(b5)
        
        return r

Relative_Layout().run()
