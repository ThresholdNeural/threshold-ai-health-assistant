import sqlite3

#function
def insert_health_data(
    steps,
    sleep_hours,
    water_intake
    
):
 print("Data inserting")   
#connect
 conn = sqlite3.connect("utills/database/health.db")

 cursor = conn.cursor()

# INSERT QUERY

 cursor.execute("""
               
      INSERT INTO health_data (
          
          steps,
          sleep_hours,
          water_intake
          
      )         
       
      VALUES (?,?,?)
      """, (
          
          steps,
          sleep_hours,
          water_intake
      ))      
 
def fetch_health_data():
    
    conn = sqlite3.connect("utills/database/health.db") 
    
    cursor = conn.cursor()
    
    cursor.execute("""
           SELECT*FROM health_data 
                   """)
 
    data = cursor.fetchall()
    
    conn.close()
    
    return data