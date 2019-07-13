import sqlite3

def createTable():
    conn = sqlite3.connect("myDB")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insertData(item, quantity, price):
    conn = sqlite3.connect("myDB")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("myDB")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("myDB")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?", (item,))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn  = sqlite3.connect("myDB")
    cur = conn.cursor()
    cur.execute("UPDATE store SET price = ? , quantity = ? WHERE item = ?",(price, quantity, item))
    conn.commit()
    conn.close()

delete("Pipe")
insertData("Pipe", 50, 4000)
update("Pipe", 60, 5000)
for i in view():
    print(i)