from kivy.app import App
from kivy.garden.mapview import MapView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapView import *
from src.logic import Logic
from kivy.uix.dropdown import DropDown
from src.gpsHandler import GpsHandler
from src.menFuncs import MenuFunctions
from kivy.garden.mapview import MapMarker
from kivy.clock import Clock
import math

class MyApp(App):
    """Main class for all our kivy stuff, there is a few functions in here, update which is called in
    on_start, which call update every 0.1 seconds"""

    def update(self, _):
        """Get gps signals, update them, if its not android, update according to center of mapview"""

        print(self.logic.placedVogne)

        """Check, if its an andorid device, if it is, gps signals are recieved"""
        if not self.gpshandler.androidBool:
            self.latitude = self.mapview.lat
            self.longitude = self.mapview.lon

        else:
            self.latitude = self.gpshandler.my_lat
            self.longitude = self.gpshandler.my_lon

        if not self.logic.alerting:
            for i in self.logic.placedVogne:
                if math.fabs((float(self.latitude) - float(i[0]))) < self.offset and math.fabs((float(self.longitude) - float(i[1]))) < self.offset:
                    self.logic.Alert()

        self.person.lat = self.latitude
        self.person.lon = self.longitude


    def on_start(self):
        """When app is started, this is called, which starts a clock calling update"""
        Clock.schedule_interval(self.update, 0.1)

    def build(self):
        """In here, we build all the basic for our kivy stuff, like making our layout, initialize our mapview,
        our different buttons and so on, its also in here we call our gpsHandler, and call our placephotovogn"""

        self.logic = Logic(self)
        self.MenuFuncs = MenuFunctions(self)
        self.gpshandler = GpsHandler(self)
        self.offset = 0.001

        """initalizing the few colors in kivy binary"""
        self.Lightred = [1111111111, 0, 0, 1]
        self.black = [0, 0, 0, 1]
        self.green = [0, 1111111, 0, 1]


        """Creating MapView, which let us determ, zoom, lat and lon, essentiel it would be pulling from gps signlas"""
        self.mapview = MapView(zoom=15, lat=56.04, lon=12.457) #56.0394 , 12.457
        self.person = MapMarker(lat=self.mapview.lat, lon=self.mapview.lon, source='images/car.png')
        self.mapview.add_marker(self.person)
        """Making a layout, as a boxlayout, making it vertical to match our desired design"""
        self.layout = BoxLayout(orientation="vertical")


        """Initializing our buttons, then after connection them to functions, when they are pressed"""
        self.buttonAnmeld = Button(text="ANMELD!", font_size=100, color=self.black, background_color=self.green)
        self.buttonAlert = Button(text="ALARM!", font_size=200, color=self.black,
                                  background_color=self.Lightred, disabled=True, opacity=0)

        """Binding our botton to a specific function, lambda is so the function wont get called when iniialized"""
        self.buttonAnmeld.bind(on_press=lambda dt: self.logic.FotoVognSpotted(self.mapview.lat, self.mapview.lon))


        """Creating the dropdown menu"""
        self.dropdown = DropDown(size_hint_x=0.2)

        """Labels"""
        labels = ['  Reset Zoom', '  Zoom In', '  Zoom Out', ' Increase LAT', '  Decrease LAT', '  Increase LON',
                 '  Decrease LON', "  Exit"]

        """Functions"""
        functions = [self.MenuFuncs.resetZoom, self.MenuFuncs.zoomIn, self.MenuFuncs.zoomOut,
                     self.MenuFuncs.IncreaseLat, self.MenuFuncs.DecreaseLat,
                     self.MenuFuncs.IncreaseLon, self.MenuFuncs.DecreaseLon, self.MenuFuncs.exit]

        """Creating buttons for each label, give them their corresponding function, allign them at  left,
        and last, adding them to the dropdown widget"""
        for label, func in zip(labels, functions):
            self.btn = Button(text=label, size_hint_y=None, height=45, halign="left", valign= "middle")
            self.btn.bind(size=self.btn.setter('text_size'))
            self.btn.bind(on_release=func)

            self.dropdown.add_widget(self.btn)

        """Creating our menuMainButton, also alligned at left"""
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
        self.gpshandler.run()

        """Returning the layout"""
        return self.layout

if __name__ == '__main__':
    MyApp().run()
