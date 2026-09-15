import sqlite3

def search_files():
    conn = sqlite3.connect("file_index.db")
    cursor = conn.cursor()
    recent_results = []
    recent_filepaths = []
    print("\n" + "-"*40)
    print("Local file search engine running")
    print("Type a word to search for the file")
    print("Type a number to open the folder from Recents")
    print(recent_results)
    print("Type 'exit' to stop the engine")
    print("-"*40)
    
    while True:
        user_input = input("\n" + "Target file: ")
        
        
        if user_input.lower() =="exit":
            break
        if user_input == "":
            continue
        query = f"{user_input}*"

        try:
            recent_filepaths = []
            recent_results = []
            
            cursor.execute('''
                        SELECT filename, filepath FROM files
                        WHERE filename MATCH ?
                        ORDER BY RANK
                        LIMIT 10
                        ''', (query,))
            
            results = cursor.fetchall()
            if results:
                print(f"\n Found {len(results)} ")
                print(f"\n These are the top 10 Matches: ")
                for index, (filename,filepath) in enumerate (results, start = 1):
                    recent_results.append(filename)
                    recent_filepaths.append(filepath)
                    print(f"{index}.{filename}")
                    print(f"{filepath}")
                    print(f"\n")
            else:
                print("No matching files.")
            
        except Exception as e:
            print(f"Issue detected: {e}")
            print("Try not to use special characters when inputing the File Name.")
            
    conn.close()
    print("Engine has been closed.")

if __name__ == "__main__":
    search_files()