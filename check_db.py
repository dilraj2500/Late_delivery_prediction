import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Dilrajno.1',
    database='late_delivery_db'
)
cursor = conn.cursor()
cursor.execute('SELECT * FROM prediction_history')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()