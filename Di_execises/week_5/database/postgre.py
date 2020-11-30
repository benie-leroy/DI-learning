import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'jeff'
DATABASE = 'hd'

connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

cursor = connection.cursor()

query = "SELECT * FROM countries LIMIT 20;"
cursor.execute(query)
results = cursor.fetchall()
connection.close()
for items in results:
    print(items)
