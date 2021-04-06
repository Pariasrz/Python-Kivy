from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import AsyncImage

Builder.load_string("""
<centerAsyncImage>:
    size_hint: 0.8, 0.8
    pos_hin: {'center_x': 0.5, 'center_y': 0.5}
    mipmp : True                    
""")

class centerAsyncImage(AsyncImage):
    pass

class textasyncimageapp(App):
    def build(self):
        url = ('https://i.redd.it/szncuech07651.png')
        return centerAsyncImage(source = url)
    
if __name__ == '__main__':
    textasyncimageapp().run()
