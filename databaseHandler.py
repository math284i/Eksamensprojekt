import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

"""Connection to firebase-database"""
cred = credentials.Certificate("eksamensproject-firebase-adminsdk-qsqlg-134386dbd0.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://eksamensproject.firebaseio.com/'
})


class DBFunctions():
    """Class for all the database functions"""

    def __init__(self, parent=None):
        """Declaring the parent, and a few varibles"""
        self.minimumVisited = 4
        self.Logic = parent

    def get(self, koordinater):
        """Connect to db, and return 1 specific koordinat"""

        self.ref = db.reference('koordinater/' + str(koordinater))
        self.a = self.ref.get()
        return self.a


    def get_all(self):
        """Connect to db, and return all koordinats"""

        self.ref = db.reference('koordinater/')
        self.a = self.ref.get()
        return self.a


    def add(self, koordinater, visited = 1, active = 0):
        """Connect to db, check if koords are already there, if they aren't add them
            If they are there, add 1 to visit, and check if visit is above minimum, then call logic.DBAlert"""

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
                self.Logic.DBAlert(koordinater)

            self.update(koordinater, "visited", newVisit)

    def update(self, koordinater, key, value):
        """If the koords are already there, we can just update the value according to key"""

        self.ref = db.reference('koordinater/' + str(koordinater))
        if self.get(koordinater):
            print("Update called found something to updpate")
            self.ref.update({
                str(key): int(value)
            })

    def delete(self, koordinater):
        """Delete specific koord from database"""
        if self.get(id):
            ref = db.reference('koordinater/' + str(koordinater))
            ref.delete()
