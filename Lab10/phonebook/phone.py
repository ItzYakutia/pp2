import psycopg2
from func import *

phoneboard = int(input("Hello!\n0 for create table\n1 for insert data\n2 for update\n3 for query\n4 for delete data\n"))

if phoneboard == 0:
    """creates table"""
    create_table()
elif phoneboard == 1:
    """insert new data in table"""
    insert_data()
elif phoneboard == 2:
    """updates the number, firstly name"""
    update(input(), input())
elif phoneboard == 3: 
    """query"""
    query()
elif phoneboard == 4: 
    """deletes"""
    delete_data()