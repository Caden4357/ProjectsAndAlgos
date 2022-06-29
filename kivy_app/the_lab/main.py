
import kivy
#import app to run kivy app
from kivy.app import App
# boxlayout is like a grid system we use to design we can add widgets and all sorts of things its responsive
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
# from kivy.uix.button import Button

class BoxLayoutExample(BoxLayout):
    # # doing design inside the python file vs the .kv file 
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     # by default elements are put together horizantily this is how you change that 
    #     self.orientation = "vertical"
    #     # creating 3 buttons 
    #     button1=Button(text="Hello Button")
    #     button2=Button(text="Hello Button Two")
    #     button3=Button(text="Hello Button Three")
    #     # adding the buttons to the screen 
    #     self.add_widget(button1)
    #     self.add_widget(button2)
    #     self.add_widget(button3)
    pass
class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

if __name__ == "__main__":
    TheLabApp().run()