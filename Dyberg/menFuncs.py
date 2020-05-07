from kivy.app import App
from kivy.garden.mapview import MapView
from kivy.uix.button import Button
from Dyberg.logic import Logic

class MenuFunctions():
    def __init__(self, parent=None):
        self.MyApp = parent
        self.logic = parent.logic

    def test(self, btn):
        print("det virker")
        self.MyApp.dropdown.select(btn.text)


    def resetZoom(self, btn):
        self.MyApp.mapview.zoom = 11
        self.MyApp.dropdown.select(btn.text)


    def zoomIn(self, btn):
        self.MyApp.mapview.zoom = self.MyApp.mapview.zoom + 1


    def zoomOut(self, btn):
        self.MyApp.mapview.zoom = self.MyApp.mapview.zoom - 1

    def IncreaseLat(self, btn):
        self.lat = self.MyApp.mapview.lat + 0.01
        self.lon = self.MyApp.mapview.lon

        self.logic.moveMap(self.lat, self.lon)


    def DecreaseLat(self, btn):
        self.lat = self.MyApp.mapview.lat - 0.01
        self.lon = self.MyApp.mapview.lon

        self.logic.moveMap(self.lat, self.lon)


    def IncreaseLon(self, btn):
        self.lat = self.MyApp.mapview.lat
        self.lon = self.MyApp.mapview.lon + 0.1

        self.logic.moveMap(self.lat, self.lon)


    def DecreaseLon(self, btn):
        self.lat = self.MyApp.mapview.lat
        self.lon = self.MyApp.mapview.lon - 0.1

        self.logic.moveMap(self.lat, self.lon)

    def exit(self, btn):
        self.MyApp.root_window.close()