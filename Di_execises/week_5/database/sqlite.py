import sqlite3

conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()
print("Opened database successfully")

# cursor.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL);''')
# cursor.close()

# cursor.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE) VALUES (1, 'Razi', 14)");
# cursor.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE) VALUES (2, 'Jon', 19)");
# cursor.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE) VALUES (3, 'Martha', 35)");
# conn.commit()
# conn.close()

def add_employee():
    name = input('tell your name please :')
    age = int(input('tell your age please :'))
    cursor.execute(f"INSERT INTO EMPLOYEE (ID,NAME,AGE) VALUES (4, {name}, {age})")
    conn.commit()
    conn.close()
add_employee()