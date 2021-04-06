from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label

class AccordionApp(App):
    def build(self):
        root = Accordion()
        root = Accordion(min_space = 60)
        
        root = Accordion(orientation = 'vertical')
        
        for x in range(5):
            item = AccordionItem(title = "Item %d" %x)
            item.add_widget(Label(text = "Text \n"*6))
            root.add_widget(item)
        
        return root

AccordionApp().run()
