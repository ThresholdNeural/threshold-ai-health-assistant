import sqlite3

conn = sqlite3.connect("utills/database/health.db")

cursor = conn.cursor()

cursor.execute("""
               
    CREATE TABLE IF NOT EXISTS health_data (
        
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        steps INTEGER, 
        sleep_hours INTEGER,
        water_intake TEXT
        
        
        
    ) """)

print("Table created sucessfully")

# save changes
conn.commit()

#close connection 
conn.close()