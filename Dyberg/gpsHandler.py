from kivy.app import App
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog
from Dyberg.logic import Logic
from kivy.garden.mapview import MapView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.clock import Clock

class GpsHelper():
    has_centered_map = False
    print("this is called")

    def __init__(self, parent = None):
        self.MyApps = parent
        self.logic = Logic(self)

    def run(self):
        # Get a reference to GpsBlinker, then call blink()
        gps_blinker = self.MyApps.get_running_app().root.ids.mapview.ids.blinker
        # Start blinking the GpsBlinker
        gps_blinker.blink()

        # Request permissions on Android
        if platform == 'android':
            from android.permissions import Permission, request_permissions
            def callback(permission, results):
                if all([res for res in results]):
                    print("Got all permissions")
                else:
                    print("Did not get all permissions")

            request_permissions([Permission.ACCESS_COARSE_LOCATION,
                                 Permission.ACCESS_FINE_LOCATION], callback)

        # Configure GPS
        if platform == 'android' or platform == 'ios':
            from plyer import gps
            gps.configure(on_location=self.update_blinker_position,
                          on_status=self.on_auth_status)
            gps.start(minTime=1000, minDistance=0)

        else:
            print("Not an android")


    def update_blinker_position(self, *args, **kwargs):
        my_lat = kwargs['lat']
        my_lon = kwargs['lon']
        print("GPS POSITION", my_lat, my_lon)
        # Update GpsBlinker position
        gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker
        gps_blinker.lat = my_lat
        gps_blinker.lon = my_lon
        print(gps_blinker.lat)


    def on_auth_status(self, general_status, status_message):
        if general_status == 'provider-enabled':
            pass
        else:
            self.open_gps_access_popup()

    def open_gps_access_popup(self):
        dialog = MDDialog(title="GPS Error", text="You need to enable GPS access for the app to function properly")
        dialog.size_hint = [.8, .8]
        dialog.pos_hint = {'center_x': .5, 'center_y': .5}
        dialog.open()