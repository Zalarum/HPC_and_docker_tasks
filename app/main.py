import psycopg2

def fetch_data():
    try:
        conn = psycopg2.connect(
            dbname="example_db",
            user="user",
            password="password",
            host="db"
        )
        cur = conn.cursor()
        
        cur.execute("INSERT INTO example_table (name) VALUES ('David');")
        
        conn.commit()
        
        cur.execute("SELECT * FROM example_table;")
        rows = cur.fetchall()
        
        print("Fetched rows:", rows)
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    fetch_data()