from databaseHandler import DBFunctions
from kivy.animation import Animation
from kivy.garden.mapview import MapMarker

class Logic():
    """Creating init function, where we can declare the otherr class, this class will be pulling from"""
    def __init__(self, parent=None):
        self.DBFunctions = DBFunctions(self)
        self.MyApp = parent


    def FotoVognSpotted(self, lat, lon): #takes 2 argument, the gps koods
        """What should it be doing?

        1) Call Database with lat and lon, check if they are already there

            If they aren't there, call add function from DBFunctions, which will add them, with the standards values
            break

            If they are in database, check how many times its been visited, then  add 1

        2) If we dident break in 1), we check if the kods.active(its a bool)

            if kods.active
                :return

            if not, check if kods.visited is higher than the minimum required (its a varialbe)

            if it is higher, then change bool to true

            if not
                return
        """

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
        What should it be doing?

        1) pull all Kods from database, using DBFunctions.get_all()

        2) check if kods.active (bool)

        3) if its active, it should be added to the mapview

        Its called, if a koord gets active, so we should place marker and animate our alert button

        """

        self.ALL = self.DBFunctions.get_all()
        """Check if there is anything to add"""
        print(self.ALL)
        if str(self.ALL) != "None":
            for i in self.ALL:
                active = self.ALL[i].pop('active')
                if active == 1:
                    self.latVogn, self.lonVogn = self.getLatLon(i)
                    self.foto = MapMarker(lat=self.latVogn, lon=self.lonVogn, source='fotovogn.png')
                    self.MyApp.mapview.add_marker(self.foto)


    def Alert(self, ActiveKods):
        """Now by using the system we implemented earlier we can call
         system with the kods and get lat and lon returned"""
        self.latAlert, self.lonAlert = self.getLatLon(ActiveKods)

        """Since our Placefotovogn only runs at initialization,
         and there is no point in trying to place every marker again, we can just place it here"""
        self.foto = MapMarker(lat=self.latAlert, lon=self.lonAlert, source='fotovogn.png')
        self.MyApp.mapview.add_marker(self.foto)

        """Now lets alert the user"""
        self.anmiate_the_button(self.MyApp.buttonAlert)


    def anmiate_the_button(self, widget, *args):
        """Creating our function, for animating our alert button"""

        anim = Animation(background_color=self.MyApp.Lightred)
        """7 is the duration of Alert, opacity means if we can see it, duration, if its instant or faded"""
        for i in range(7): #Duration of Alert
            anim += Animation(opacity=1, duration=.5)
            anim += Animation(opacity=0.2, duration=.5)
        anim += Animation(opacity=0, duration=.2)
        anim += Animation(background_color=self.MyApp.Lightred)
        anim.start(widget)

    def moveMap(self, newLat, newLon):
        """Function, to move the map and person around, according to gps menu functions"""
        self.lat = newLat
        self.lon = newLon

        self.MyApp.mapview.center_on(self.lat, self.lon)
        self.MyApp.person.lat = self.lat
        self.MyApp.person.lon = self.lon
