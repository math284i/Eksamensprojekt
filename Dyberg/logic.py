from Dyberg.databaseHandler import DBFunctions
from kivy.animation import Animation
from kivy.garden.mapView import MapMarker

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
        koords = koords.replace("X", ".").replace("H", " ")
        lat, lon = koords.split(" ")
        return lat, lon

    def PlaceFotoVogn(self):
        """What should it be doing?

        1) pull all Kods from database, using DBFunctions.get_all()

        2) check if kods.active (bool)

        3) if its active, it should be added to the mapview

        """

        self.ALL = self.DBFunctions.get_all()
        for i in self.ALL:
            active = self.ALL[i].pop('active')
            if active == 1:
                self.latVogn, self.lonVogn = self.getLatLon(i)
                self.foto = MapMarker(lat=self.latVogn, lon=self.lonVogn)
                self.MyApp.mapview.add_marker(self.foto)


    def Alert(self, ActiveKods):
        """What should it be doing?

        1) check if the personKods is within a sertain range, of the active kods

        2) if it is, make the alarm button blink red, and play alarm

        """

        print("Active kods: " + str(ActiveKods))
        """Now by using the system we implemented earlier we can call system with the kods and get lat and lon returned"""
        self.latAlert, self.lonAlert = self.getLatLon(ActiveKods)

        """Since our Placefotovogn only runs at initialization,
         and there is no point in trying to place every marker again, we can just place it here"""
        self.foto = MapMarker(lat=self.latAlert, lon=self.lonAlert)
        self.MyApp.mapview.add_marker(self.foto)

        """Now lets alert the user"""
        self.anmiate_the_button(self.MyApp.buttonAlert)

    """Creating our function, for animating our alert button"""
    def anmiate_the_button(self, widget, *args):

        anim = Animation(background_color=self.MyApp.Lightred)
        for i in range(10):
            anim += Animation(opacity=1, duration=.2)
            anim += Animation(opacity=0.2, duration=.2)
        anim += Animation(opacity=0, duration=.2)
        anim += Animation(background_color=self.MyApp.Lightred)
        anim.start(widget)

    """Function, to move the map around, according to gps koords"""
    def moveMap(self, newLat, newLon):
        self.lat = newLat
        self.lon = newLon

        self.MyApp.mapview.center_on(self.lat, self.lon)