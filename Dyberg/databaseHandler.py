import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("Dyberg/eksamensproject-firebase-adminsdk-qsqlg-134386dbd0.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://eksamensproject.firebaseio.com/'
})

class DBFunctions():
    def __init__(self, parent=None):
        pass

    def testPrint(self):
        print("Det virker")

    def get(self, koordinater):
        self.ref = db.reference('Player_Info/' + str(koordinater))
        self.a = self.ref.get()
        return self.a

    def get_all(self):
        self.ref = db.reference('Player_Info/')
        self.a = self.ref.get()
        return self.a

    def add(self, koordinater, visited = 1, active = 0):
        self.ref = db.reference('Player_Info')
        if not self.get(koordinater):
            print("this koods arent therre")

            #ref.update({
           #     str(key): str(value)
           # })

    def update(self, koordinater, key, value):
        ref = db.reference('Player_Info/' + str(koordinater))
        if self.get(koordinater):
            print("Update called found something to updpate")



    def delete(self, koordinater):
        if self.get(id):
            ref = db.reference('Player_Info/' + str(koordinater))
            ref.delete()


#DBFunctions().add(201082527824347136, "Dyberg")
#DBFunctions().add(330761716386234369, "Rune")
#DBFunctions().add(184896015218900992, "Lohmann")