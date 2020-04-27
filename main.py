import sys
import os.path
from peewee import *
import peewee
import classes_error as Error
import datetime
import random as rnd

version = 1.3
version_description = '''
python 3.5 works
'''
name_database = 'database.db'

db = SqliteDatabase(name_database)
        
class BaseModel(Model):
    class Meta:
        database = db
                
class CLIENTS(BaseModel):
    """Table CLIENTS"""
    
    ID = PrimaryKeyField()
    NAME = CharField(max_length=50)
    CITY = CharField(max_length=50)
    ADDRESS = CharField(max_length=50)
    
    class Meta:
        db_table = 'clients'
        order_by = ('ID',)
                
class ODDERS(BaseModel):
    """Table ODDERS"""
    
    ID = PrimaryKeyField()
    CLIENT = ForeignKeyField(CLIENTS,backref='client')
    DATE = DateTimeField(default=datetime.datetime.today())
    AMOUNT = IntegerField()
    DESCRIPTION = CharField(max_length=100)
    
    class Meta:
        db_table = 'odders'
        order_by = ('ID',)

if __name__ == '__main__':

    if len(sys.argv) == 1 or sys.argv[1] == '--help':
        """doc"""
        
        if not os.path.exists('doc.txt'):
            raise Error.NotFoundDocFile('File doc.txt not found')
        try:
            file_doc = open('doc.txt')
            for line in file_doc:
                print(line)
            file_doc.close()
        except:
            raise Error.OpenDocFileError('Failed to open doc.txt')

    elif len(sys.argv) == 2 and sys.argv[1] == '--version' or sys.argv[1] == '-v':
        """Show version"""
        
        #print(f'{version}')
        print(version)
        
    elif len(sys.argv) == 2 and sys.argv[1] == 'init':
        """init DB (empty)"""
        
        if os.path.exists(name_database):
            os.remove(name_database)
        
        try:
            db.connect()
            CLIENTS.create_table()
            ODDERS.create_table()
        except peewee.InternalError as px:
            print(str(px))
        
    elif len(sys.argv) == 2 and sys.argv[1] == 'fill':
        """fill DB (10 row)"""
        
        try:
            db.connect()
            for i in range(10):
                #CLIENTS.create(NAME='NAME{i+1}',CITY=f'CITY{i+1}',ADDRESS=f'ADDRESS{i+1}')
                CLIENTS.create(NAME='NAME'+str(i+1),CITY='CITY'+str(i+1),ADDRESS='ADDRESS'+str(i+1))
                #ODDERS.create(CLIENT=rnd.randint(0,10),AMOUNT=i+1,DESCRIPTION=f'test')
                ODDERS.create(CLIENT=rnd.randint(0,10),AMOUNT=i+1,DESCRIPTION='test')
        except peewee.InternalError as px:
            print(str(px))
            
    elif len(sys.argv) == 3 and sys.argv[1] == 'show':
        """Show table for name"""
        
        TABLES_NAME = ['CLIENTS','ODDERS']
        if sys.argv[2].upper() not in TABLES_NAME:
            raise Error.TableNameError('There is no such table in the database')
        try:
            db.connect()
            if sys.argv[2].upper()=='CLIENTS':
                print('--------TABLES CLIENTS--------')
                print(' ID\tNAME\tCITY\tADDRESS')
                for row in CLIENTS.select():
                    #print(f' {row.ID}\t{row.NAME}\t{row.CITY}\t{row.ADDRESS}')
                    print(row.ID,'\t',row.NAME,'\t',row.CITY,'\t',row.ADDRESS)

            if sys.argv[2].upper()=='ODDERS':
                print('--------TABLES ODDERS--------')
                print(' ID\tCLIENT_id\tDATE\t\t\tAMOUNT\tDESCRIPTION')
                for row in ODDERS.select():
                    #print(f' {row.ID}\t{row.CLIENT_id}\t{row.DATE}\t{row.AMOUNT}\t{row.DESCRIPTION}')
                    print(row.ID,'\t',row.CLIENT_id,'\t',row.DATE,'\t',row.AMOUNT,'\t',row.DESCRIPTION)
                
        except peewee.InternalError as px:
            print(str(px))

    else:
        raise Error.ArgsInputError('Incorrect input of program arguments')
