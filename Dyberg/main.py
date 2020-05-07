from kivy.app import App
from kivy.garden.mapview import MapView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.garden.mapView import *
from kivy.garden.mapView import MapMarker
from kivy.clock import Clock
from Dyberg.databaseHandler import DBFunctions
import time
from Dyberg.logic import Logic
from kivy.uix.dropdown import DropDown
from Dyberg.gpsHandler import GpsHelper
from Dyberg.menFuncs import MenuFunctions


class MyApp(App):

    """Building our app, normmally it would be the __init__ function"""
    def build(self): #Ville normalt være def __init__(self, parent=None):

        self.logic = Logic(self)
        self.dropdown = DropDown(size_hint_x=0.2)
        self.MenuFuncs = MenuFunctions(self)

        self.gpsHelper = GpsHelper()
        # GpsHelper.run(self.gpsHelper)

        """initalizing the few colors in kivy binary"""
        self.Lightred = [1111111111, 0, 0, 1]
        self.black = [0, 0, 0, 1]
        self.green = [0, 1111111, 0, 1]


        """Creating MapView, which let us determ, zoom, lat and lon, essentiel it would be pulling from gps signlas"""
        self.mapview = MapView(zoom=11, lat=56.04, lon=12.457) #56.0394 , 12.457

        """Making a layout, as a boxlayout, making it vertical to match our desired design"""
        self.layout = BoxLayout(orientation="vertical")


        """Initializing our buttons, then after connection them to functions, when they are pressed"""
        self.buttonAnmeld = Button(text="ANMELD!", font_size=100, color=self.black, background_color=self.green)

        self.buttonAnmeld.bind(on_press=lambda dt: self.logic.FotoVognSpotted(self.mapview.lat, self.mapview.lon))

        self.buttonAlert = Button(text="ALARM!", font_size=200, color=self.black,
                                  background_color=self.Lightred, disabled=True, opacity=0)

        self.top_layout = AnchorLayout(anchor_x="left", anchor_y="top")

        notes = ['  Reset Zoom', 'Zoom In', 'Zoom Out','  Increase LAT', '  Decrease LAT', '  Increase LON',
                 '  Decrease LON', "  Exit"]

        functions = [self.MenuFuncs.resetZoom, self.MenuFuncs.zoomIn, self.MenuFuncs.zoomOut,
                     self.MenuFuncs.IncreaseLat, self.MenuFuncs.DecreaseLat,
                     self.MenuFuncs.IncreaseLon, self.MenuFuncs.DecreaseLon, self.MenuFuncs.exit]

        for note, func in zip(notes, functions):
            self.btn = Button(text=note, size_hint_y=None, height=45, halign="left", valign= "middle")
            self.btn.bind(size=self.btn.setter('text_size'))
            self.btn.bind(on_release=func)

            self.dropdown.add_widget(self.btn)

        self.mainbutton = Button(text='  Menu', size_hint_y=None, height=35,
                                 halign="left", valign= "middle", size_hint_x=0.2)

        self.mainbutton.bind(size=self.mainbutton.setter('text_size'))
        self.mainbutton.bind(on_release=self.dropdown.open)

        """Adding all the different stuff to our layout, in the desired order"""
        self.layout.add_widget(self.mainbutton)
        self.layout.add_widget(self.buttonAnmeld)
        self.layout.add_widget(self.mapview)
        self.layout.add_widget(self.buttonAlert)

        self.logic.PlaceFotoVogn()

        """Returning the layout"""
        return self.layout

if __name__ == '__main__':
    MyApp().run()
