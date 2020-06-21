from kivy.utils import platform
#from src.kivymd.uix import MDDialog

class GpsHandler():
    """Get the android gps koords, and return them"""
    def __init__(self, parent=None):
        """Initialize, a few variables, and parent"""
        self.MyApp = parent
        self.my_lat = self.MyApp.mapview.lat
        self.my_lon = self.MyApp.mapview.lon
        self.androidBool = False

    def run(self):
        """This function is called when the class is called, GpsHandler.run()"""
        # Request permissions on Android
        if platform == 'android':
            from android.permissions import Permission, request_permissions
            def callback(permission, results):
                """Check for any errors, with permissions"""
                if all([res for res in results]):
                    print("Got all permissions")
                else:
                    print("Did not get all permissions")

            request_permissions([Permission.ACCESS_COARSE_LOCATION,
                                 Permission.ACCESS_FINE_LOCATION], callback)

        # Configure GPS
        if platform == 'android' or platform == 'ios':
            self.androidBool = True
            from plyer import gps
            gps.configure(on_location=self.updateGpsLatLon,
                          on_status=self.onAuthStatus)
            gps.start(minTime=1000, minDistance=0)

        else:
            self.androidBool = False


    def updateGpsLatLon(self, *args, **kwargs):
        self.my_lat = kwargs['lat']
        self.my_lon = kwargs['lon']
        print("GPS POSITION", self.my_lat, self.my_lon)



    def onAuthStatus(self, general_status, status_message):
        if general_status == 'provider-enabled':
            pass
        else:
            self.openGpsAcessPopup()

    def openGpsAcessPopup(self):
        dialog = MDDialog(title="GPS Error", text="You need to enable GPS access for the app to function properly")
        dialog.size_hint = [.8, .8]
        dialog.pos_hint = {'center_x': .5, 'center_y': .5}
        dialog.open()
        print("Dialog")
