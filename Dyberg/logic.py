from Dyberg.databaseHandler import DBFunctions


class Logic():
    def __init__(self, parent=None):
        self.DBFunctions = DBFunctions(self) #Bliver ikke brugt pt

    def testLogic(self):
        DBFunctions.testPrint(self)

