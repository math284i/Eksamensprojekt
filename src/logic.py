from src.databaseHandler import DBFunctions
from kivy.animation import Animation
from kivy.garden.mapview import MapMarker

class Logic():
    """Creating init function, where we can declare the otherr class, this class will be pulling from"""
    def __init__(self, parent=None):
        self.DBFunctions = DBFunctions(self)
        self.MyApp = parent
        self.placedVogne = []
        self.alerting = False


    def FotoVognSpotted(self, lat, lon): #takes 2 argument, the gps koods
        """Koordinat system, it contains lat + a seperater,
         which we decides to be H + lon, and "." is replaced with "X" """

        lat = str(round(lat, 3))
        lon = str(round(lon, 3))

        koods = lat + "H" + lon
        print(koods)

        """We need to remove "." because we cant use special characters, for database name, so we use x instead,
         also we needed to indicate where lat and lon is, when he re pull the koods"""
        koods = koods.replace(".", "X")
        print("new koods: " + str(koods))
        self.DBFunctions.add(koods)


    def getLatLon(self, koords):
        """'decoding' the system we made earlier, from koords to lat and lon"""
        koords = koords.replace("X", ".").replace("H", " ")
        lat, lon = koords.split(" ")
        return lat, lon


    def PlaceFotoVogn(self):
        """Placing all photovagens all ready in db at startup
        """

        self.ALL = self.DBFunctions.get_all()
        """Check if there is anything to add"""
        print(self.ALL)
        if str(self.ALL) != "None":
            for i in self.ALL:
                active = self.ALL[i].pop('active')
                if active == 1:
                    self.latVogn, self.lonVogn = self.getLatLon(i)
                    self.placedVogne.append([self.latVogn, self.lonVogn])
                    self.foto = MapMarker(lat=self.latVogn, lon=self.lonVogn, source='images/fotovogn.png')
                    self.MyApp.mapview.add_marker(self.foto)


    def DBAlert(self, ActiveKods):
        """Now by using the system we implemented earlier we can call
         system with the kods and get lat and lon returned, this function will also make a marker,
         Since our Placefotovogn only runs at initialization,
         and there is no point in trying to place every marker again, we can just place it here"""
        self.latAlert, self.lonAlert = self.getLatLon(ActiveKods)
        self.placedVogne.append([self.latAlert, self.lonAlert])
        self.foto = MapMarker(lat=self.latAlert, lon=self.lonAlert, source='images/fotovogn.png')
        self.MyApp.mapview.add_marker(self.foto)

        """Now lets alert the user"""
        self.anmiate_the_button(self.MyApp.buttonAlert)

    def Alert(self):
        """This function is for alert alone, called when person is within a sertain range of a speed trap"""

        """Now lets alert the user"""
        self.anmiate_the_button(self.MyApp.buttonAlert)


    def anmiate_the_button(self, widget, *args):
        """Creating our function, for animating our alert button"""
        self.alerting = True
        anim = Animation(background_color=self.MyApp.Lightred)
        """7 is the duration of Alert, opacity means if we can see it, duration, if its instant or faded"""
        for i in range(5): #Duration of Alert
            anim += Animation(opacity=1, duration=.5)
            anim += Animation(opacity=0.2, duration=.5)
        anim += Animation(opacity=0, duration=.2)
        anim += Animation(background_color=self.MyApp.Lightred)
        anim.bind(on_complete=self.animationBool)
        anim.start(widget)

    def animationBool(self, widget, *args):
        """amination on_completes need to bind to a function """
        self.alerting = False

    def moveMap(self, newLat, newLon):
        """Function, to move the map and person around, according to gps menu functions"""
        self.lat = newLat
        self.lon = newLon

        self.MyApp.mapview.center_on(self.lat, self.lon)
        self.MyApp.person.lat = self.lat
        self.MyApp.person.lon = self.lon
