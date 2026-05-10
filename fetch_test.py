import sqlite3

conn = sqlite3.connect("utills/database/health.db")

cursor = conn.cursor()

cursor.execute("""
               SELECT * FROM health_data
               """)

data = cursor.fetchall()

print(data)

conn.close()