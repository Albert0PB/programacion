import pymysql

conn = pymysql.connect(host="localhost",
                       user="alberto",
                       passwd="alberto",
                       database="personal")
cursor = conn.cursor()

entries = "SELECT * FROM Usuarios;"

cursor.execute(entries)
rows = cursor.fetchall()

for fila in rows:
    print(fila)

# Finalizar
conn.commit()
conn.close()
