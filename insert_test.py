import sqlite3

conn = sqlite3.connect("utills/database/health.db")

cursor = conn.cursor()

cursor.execute("""
               
       INSERT INTO health_data (
           steps,
           sleep_hours,
           water_intake
           )        
               
       VALUES (?,?,?) """, (7000,8,"completed"))

conn.commit()

conn.close()

print("Data inserted successfully")

