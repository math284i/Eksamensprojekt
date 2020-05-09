class MenuFunctions():
    """Class for all the functions in the dropdown menu"""

    def __init__(self, parent=None):
        """Refaring to the parent's"""
        self.MyApp = parent
        self.logic = parent.logic


    def resetZoom(self, btn):
        """Reset Zoom to original zoom the mapview was initialized with"""
        self.MyApp.mapview.zoom = 15
        self.MyApp.dropdown.select(btn.text)


    def zoomIn(self, btn):
        """Increase Zoom"""
        self.MyApp.mapview.zoom = self.MyApp.mapview.zoom + 1


    def zoomOut(self, btn):
        """Decrease Zoom"""
        self.MyApp.mapview.zoom = self.MyApp.mapview.zoom - 1


    def IncreaseLat(self, btn):
        """Increast Lat of the MapView"""
        self.lat = self.MyApp.mapview.lat + 0.01
        self.lon = self.MyApp.mapview.lon

        self.logic.moveMap(self.lat, self.lon)


    def DecreaseLat(self, btn):
        """Decrease Lat of the MapView"""
        self.lat = self.MyApp.mapview.lat - 0.01
        self.lon = self.MyApp.mapview.lon

        self.logic.moveMap(self.lat, self.lon)


    def IncreaseLon(self, btn):
        """Increase Lon of the MapView"""
        self.lat = self.MyApp.mapview.lat
        self.lon = self.MyApp.mapview.lon + 0.1

        self.logic.moveMap(self.lat, self.lon)


    def DecreaseLon(self, btn):
        """Decrease Lon of the MapView"""
        self.lat = self.MyApp.mapview.lat
        self.lon = self.MyApp.mapview.lon - 0.1

        self.logic.moveMap(self.lat, self.lon)


    def exit(self, btn):
        """Closing the window, and exiting the program"""
        self.MyApp.root_window.close()