import psycopg2
from proc import *

con = psycopg2.connect(host="localhost", dbname="suppliers", user="postgres", password="123") 
cur = con.cursor() 

while True: 
    command = input("""Choose number or operation:
        \t0 - search, \t2 - insert,
        \t1 - update, \t3 - exit,
    """)  
    if command == '0': 
        n = input("Enter the name or the number:\n\t") 
        word = '%' + n + '%' 
        cur.execute("SELECT * FROM get_table(%s);", (word,))
        rows = cur.fetchall()
        for x in rows:
            print(x)
        if len(rows) == 0:
            print("Contacts doesn't exist")
             
    if command == '1': 
        id, name, phone_num = int(input("Enter ID:\t")), input("Enter name:\t"), input("Enter the number:\t")  
        cur.execute(commands['update'], (id, name, phone_num)) 
        print("Contact have been added or changed")

    if command == '2': 
        name = input("Enter the name or the number to delete: ") 
        cur.execute(commands['delete'], (name,)) 
        print("Contact deletted")
        con.commit() 

    if command == '3': 
        print("Goodbye! See you next time")
        break 
         
cur.close() 
con.commit() 
con.close()