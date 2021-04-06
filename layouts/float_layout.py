from kivy.app import App
from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string('''
                                
FloatLayout: 
    
    Button:
        text: "Click 1"
        pos_hint: {'x' : 0, 'top': 1}
        size_hint: .3, .2
        
    Button: 
        text: "Click 2"
        post_hint: {'y': 0, 'left':1}
        size_hint: .3, .1
    
                              
        
'''))


#or we can use the code below
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class myapp(App):
    def buil(self):
        
        f1 = FloatLayout()
        
        button1 = Button(text = 'Text 1', size_hint=(5 , 5),
                         post_hint = {'x' : .5, 'y': .5},
                         background_color = (.4, .8, .2, .1))
        
        f1.add_widget(button1)
        
        return f1
    
if __name__ == '__main__':
    myapp().run()
