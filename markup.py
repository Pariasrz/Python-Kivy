from kivy.app import App
from kivy.uix.label import Label

class firstapp(App):
    def build(self):
        return Label(text='[b][s][color=FF9945][i]Hello[/i][/color][/s] [size=40][u]world[/u][/size][/b]', markup=True)


"""
b to bold
i for italic
s for strikeThrough
"""

firstapp().run()
