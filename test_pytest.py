import pytest
from peewee import *
import peewee
import datetime
#import main
import os.path
#-------------------------------------------------
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
#-------------------------------------------------

def test_exists_database():
    """Is there a database"""
    assert os.path.exists(name_database) == True

def test_row_count_clients():
    """Number of Filled Rows in clients = 10"""
    assert len(CLIENTS.select()) == 10

def test_row_count_odders():
    """Number of Filled Rows in odders = 10"""
    assert len(ODDERS.select()) == 10

def test_coll_clients():
    """Does clients contain necessary columns"""
    try:
        x = CLIENTS.select(CLIENTS.ID,CLIENTS.NAME,CLIENTS.CITY,CLIENTS.ADDRESS)
    except:
        assert False

def test_coll_odders():
    """Does odders contain necessary columns"""
    try:
        x = ODDERS.select(ODDERS.ID,ODDERS.CLIENT_id,ODDERS.DATE, ODDERS.AMOUNT,ODDERS.DESCRIPTION)
    except:
        assert False
