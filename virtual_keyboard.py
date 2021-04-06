from kivy.app import App
from kivy.uix.vkeyboard import VKeyboard

class test(VKeyboard):
    player = VKeyboard()
    
class vkeyboardapp(App):
    def build(self):
        return test()
    
if __name__ == "__main__":
    vkeyboardapp().run()
