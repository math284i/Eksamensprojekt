from kivy.app import App
from kivy.garden.mapview import MapView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapView import *
from Dyberg.databaseHandler import DBFunctions
import time
from Dyberg.logic import Logic

darkred = [1111111, 0, 0, 1]
Lightred = [11111111, 0, 0, 1]
testRed = [1, 0, 0, 1]

class MyApp(App):

    """Building our app, normmally it would be the __init__ function"""
    def build(self): #Ville normalt være def __init__(self, parent=None):

        self.logic = Logic(self)

        """Returns a label with the text "Hello world"""
        #return Label(text='Hello world')
        """Creating MapView, which let us determ, zoom, lat and lon, essentiel it would be pulling from gps signlas"""
        self.mapview = MapView(zoom=11, lat=56.03940, lon=12.457) #56.0394 , 12.457
        #print(self.mapview.__dir__())
        print(self.mapview.lat)

        self.foto = MapMarker(lat=56.0394, lon=12.457)
        self.mapview.add_marker(self.foto)

        """Making a layout, as a boxlayout, making it vertical to match our desired design"""
        self.layout = BoxLayout(orientation="vertical")

        """Initializing our buttons, then after connection them to functions, when they are pressed"""
        self.button1 = Button(text="One")
        #self.button1.bind(on_press=DBFunctions.testPrint)
        self.button1.bind(on_press=lambda dt: self.logic.FotoVognSpotted(self.mapview.lat, self.mapview.lon))

        self.button2 = Button(text="ALERT!", font_size=100, color=darkred, background_color=Lightred, disabled=True)
        #self.button2.background_color = Lightred

        """Adding all the different stuff to our layout, in the desired order"""
        self.layout.add_widget(self.button1)
        self.layout.add_widget(self.mapview)
        self.layout.add_widget(self.button2)

        """Returning the layout"""
        return self.layout

if __name__ == '__main__':
    MyApp().run()
