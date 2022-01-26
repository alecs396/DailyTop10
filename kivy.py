import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout).__init__(**kwargs)
        
        # Set Columns
        self.cols = 2
        
        # Add widgets
        self.add_widget(Label(text="Name: "))

class MyApp(App):
    def build(self):
        return Label(text="Hello World", font_size = 72)
    
if __name__ == '__main__':
    MyApp().run()