import sqlite3

conn = sqlite3.connect("fiyatlar.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM urunler")
veriler = cursor.fetchall()

for veri in veriler:
    print(veri)

conn.close()