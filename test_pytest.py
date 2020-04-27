import pytest
import main
import os.path

def test_exists_database():
    """Is there a database"""
    assert os.path.exists(main.name_database) == True

def test_row_count_clients():
    """Number of Filled Rows in clients = 10"""
    assert len(main.CLIENTS.select()) == 10

def test_row_count_odders():
    """Number of Filled Rows in odders = 10"""
    assert len(main.ODDERS.select()) == 10

def test_coll_clients():
    """Does clients contain necessary columns"""
    try:
        x = main.CLIENTS.select(main.CLIENTS.ID,main.CLIENTS.NAME,main.CLIENTS.CITY, main.CLIENTS.ADDRESS)
    except:
        assert False

def test_coll_odders():
    """Does odders contain necessary columns"""
    try:
        x = main.ODDERS.select(main.ODDERS.ID,main.ODDERS.CLIENT_id,main.ODDERS.DATE, main.ODDERS.AMOUNT,main.ODDERS.DESCRIPTION)
    except:
        assert False
