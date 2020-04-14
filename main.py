from kivy.app import App
from kivy.uix.label import Label
from kivy.garden.mapview import MapView

class MyApp(App):

    def build(self):

        """Returns a label with the text "Hello world"""
        #return Label(text='Hello world')
        mapview = MapView(zoom=11, lat=56.040371, lon=12.579490)
        return mapview

if __name__ == '__main__':
    MyApp().run()
