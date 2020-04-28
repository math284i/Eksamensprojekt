from kivy.app import App
from kivy.garden.mapview import MapView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from Dyberg.databaseHandler import DBFunctions
from Dyberg.logic import Logic

class MyApp(App):




    def build(self): #Ville normalt være def __init__(self, parent=None):

        """Returns a label with the text "Hello world"""
        #return Label(text='Hello world')
        self.mapview = MapView(zoom=11, lat=56.0394, lon=12.457)
        print(self.mapview.__dir__())

        self.layout = BoxLayout(orientation="vertical")
        self.button1 = Button(text="One")

        self.button1.bind(on_press=DBFunctions.testPrint)

        self.button2 = Button(text="Two")

        self.button2.bind(on_press=Logic.testLogic)

        self.layout.add_widget(self.button1)

        self.layout.add_widget(self.mapview)

        self.layout.add_widget(self.button2)

        return self.layout

if __name__ == '__main__':
    MyApp().run()
