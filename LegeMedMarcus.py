from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line


class MyPaintWidget(Widget):
    pass

class MyPaintApp(App):

    def build(self):
        parent = Widget()
        self.clearbtn = Button(text='Clear')
        self.clearbtn.bind(on_release=self.tryk)
        parent.add_widget(self.clearbtn)
        return parent

    def tryk(self, obj):
        print("Du har trykket")
        print(self.clearbtn.__dir__())

if __name__ == '__main__':
    MyPaintApp().run()