from kivy.app import App
from kivy.lang import Builder

mykv=Builder.load_string("""

Label:
    text:
        'Hello [u] World [/u]'
    font_size: '64pt'
    markup: True
                             
""")


"""
or
myv = Builder.load_file('kvfile.kv')
"""

class myapp(App):
    def build(self):
        return mykv
    
myApp = myapp()
myApp.run()
