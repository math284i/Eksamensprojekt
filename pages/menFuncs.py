from kivy.app import App
from kivy.garden.mapview import MapView
from kivy.uix.button import Button
from pages.logic import Logic

"""Class for all the functions in the dropdown menu"""
class MenuFunctions():
    def __init__(self, parent=None):
        """Refaring to the parent's"""
        self.MyApp = parent
        self.logic = parent.logic

    """Reset Zoom to original zoom the mapview was initialized with"""
    def resetZoom(self, btn):
        self.MyApp.mapview.zoom = 11
        self.MyApp.dropdown.select(btn.text)

    """Increase Zoom"""
    def zoomIn(self, btn):
        self.MyApp.mapview.zoom = self.MyApp.mapview.zoom + 1

    """Decrease Zoom"""
    def zoomOut(self, btn):
        self.MyApp.mapview.zoom = self.MyApp.mapview.zoom - 1

    """Increast Lat of the MapView"""
    def IncreaseLat(self, btn):
        self.lat = self.MyApp.mapview.lat + 0.01
        self.lon = self.MyApp.mapview.lon

        self.logic.moveMap(self.lat, self.lon)

    """Decrease Lat of the MapView"""
    def DecreaseLat(self, btn):
        self.lat = self.MyApp.mapview.lat - 0.01
        self.lon = self.MyApp.mapview.lon

        self.logic.moveMap(self.lat, self.lon)

    """Increase Lon of the MapView"""
    def IncreaseLon(self, btn):
        self.lat = self.MyApp.mapview.lat
        self.lon = self.MyApp.mapview.lon + 0.1

        self.logic.moveMap(self.lat, self.lon)

    """Decrease Lon of the MapView"""
    def DecreaseLon(self, btn):
        self.lat = self.MyApp.mapview.lat
        self.lon = self.MyApp.mapview.lon - 0.1

        self.logic.moveMap(self.lat, self.lon)

    """Closing the window, and exiting the program"""
    def exit(self, btn):
        self.MyApp.root_window.close()