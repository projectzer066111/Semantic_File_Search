import sqlite3

def main():
    try:
        conn = sqlite3.connect("file_index.db")
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM files")
        conn.commit()
        
        print("Table successfully reset.")
        
    except sqlite3.OperationalError as e:
        print(f"Nothing to reset. (Error: {e})")
        
    finally:
        # The finally block ensures the connection ALWAYS closes, 
        # even if an error happens above.
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    main()