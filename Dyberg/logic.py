from Dyberg.databaseHandler import DBFunctions


class Logic():
    """Creating init function, where we can declare the otherr class, this class will be pulling from"""
    def __init__(self, parent=None):
        self.DBFunctions = DBFunctions(self) #Bliver ikke brugt pt

    def testLogic(self):
        DBFunctions.testPrint(self)

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

    def PlaceFotoVogn(self):
        """What should it be doing?

        1) pull all Kods from database, using DBFunctions.get_all()

        2) check if kods.active (bool)

        3) if its active, it should be added to the mapview

        self.foto = MapMarker(lat=Placeholder, lon=Placeholder)
        self.mapview.add_marker(self.foto)

        also append them to a list

        4) call Alert with the active list

        """

    def Alert(self, ActiveKods, PersonLat, PersonLon):
        """What should it be doing?

        1) check if the personKods is within a sertain range, of the active kods

        2) if it is, make the alarm button blink red, and play alarm

        """
