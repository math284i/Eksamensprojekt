import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from kivy.clock import Clock

cred = credentials.Certificate("eksamensproject-firebase-adminsdk-qsqlg-134386dbd0.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://eksamensproject.firebaseio.com/'
})

class DBFunctions():
    def __init__(self, parent=None):
        self.minimumVisited = 4
        self.Logic = parent

    def get(self, koordinater):
        self.ref = db.reference('koordinater/' + str(koordinater))
        self.a = self.ref.get()
        return self.a


    def get_all(self):
        self.ref = db.reference('koordinater/')
        self.a = self.ref.get()
        return self.a


    def add(self, koordinater, visited = 1, active = 0):
        self.ref = db.reference('koordinater/')
        if not self.get(koordinater):
            #print(koordinater)
            self.ref.update({
                "visited" : visited,
                "active" : active
            })

            print("this koods arent therre")

        elif self.get(koordinater):
            self.values = self.get(koordinater)
            newVisit = int(self.values.pop("visited")) + 1

            if newVisit > self.minimumVisited:
                self.update(koordinater, "active", 1)
                self.Logic.Alert(koordinater)

            self.update(koordinater, "visited", newVisit)


    def update(self, koordinater, key, value):
        self.ref = db.reference('koordinater/' + str(koordinater))
        if self.get(koordinater):
            print("Update called found something to updpate")
            self.ref.update({
                str(key): int(value)
            })


    def delete(self, koordinater):
        if self.get(id):
            ref = db.reference('koordinater/' + str(koordinater))
            ref.delete()
