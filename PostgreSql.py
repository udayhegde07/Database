import psycopg2


def createTable():
    conn = psycopg2.connect("dbname='myDB' user='postgres' password='toor' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insertData(item, quantity, price):
    conn = psycopg2.connect("dbname='myDB' user='postgres' password='toor' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='myDB' user='postgres' password='toor' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='myDB' user='postgres' password='toor' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s", (item,))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn  = psycopg2.connect("dbname='myDB' user='postgres' password='toor' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("UPDATE store SET price = %s , quantity = %s WHERE item = %s",(price, quantity, item))
    conn.commit()
    conn.close()



update("Glass", 60, 5000)
for i in view():
    print(i)
'''delete("Pipe")
insertData("Pipe", 50, 4000)
update("Pipe", 60, 5000)
for i in view():
    print(i)'''