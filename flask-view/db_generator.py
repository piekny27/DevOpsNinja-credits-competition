print('\nCreate dependency...', end='\r')
from competition.dbModels import *
print('\r\t\t\t\tdone')

class DBGenerator():
    def __init__(self):
        print('Connecting to \'' + db.engine.name + '\'...',end='\r')
        self.db = DBConnection()
        print('\r\t\t\t\tdone')

    def cleanDB(self):
        print('Drop all...', end='\r')
        self.db._engine.drop_all()
        print('\r\t\t\t\tdone')
        print('Create all...',end='\r')
        self.db._engine.create_all()
        print('\r\t\t\t\tdone')


if __name__ == "__main__":
    generator = DBGenerator()
    generator.cleanDB()

