import sqlite3
import os
import time
DB_file = "file_index.db"

def create_database ():
    conn = sqlite3.connect("file_index.db")
    cursor = conn.cursor()
    
    cursor.execute('''
                   CREATE VIRTUAL TABLE IF NOT EXISTS files USING fts5 (
                       filename,
                       keywords,
                       filepath UNINDEXED       
                   )
                   ''') 
    #Filename stores file name
    #Keywords will store the keywords from succesful prompts where the file is correctly identified
    #filepath is left unindexed to not waste cpu cycles running through it.
    conn.commit()
    return conn


def file_indexer(conn):
    cursor = conn.cursor()
    target_directory = ""  #initial folder to start looking through and start indexing.
    # Remember to delete above !!!
    try:
        cursor.execute('''
                   DELETE FROM files
                   ''')
        to_index=[]
        for roots,directories,files in os.walk(target_directory):
            for file_name in files:
                full_path = os.path.join(roots, file_name)
                print(full_path)
                to_index.append((file_name,"",full_path))
    #filename is saved normally
    #The file path is also saved normally
    #The keyword column is left blank as there isnt any need to save atp.
    
        print("Files have been recorded and will index shortly")
        print("These are the located files")
        print(to_index)
    #Saving into the local db
        cursor.executemany('''
                    INSERT INTO files (filename,keywords,filepath) 
                    VALUES (?,?,?)
                    ''',to_index)
        conn.commit()
        print("Files successfully executed")
    except Exception as e:
            print(f"Issue detected: {e}")


            
def main():
    conn = create_database()
    file_indexer(conn)
    conn.close()

    
    
if __name__ == "__main__":

    main()