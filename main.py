from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        """Returns a label with the text "Hello world"""

        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()
