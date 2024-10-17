import sqlite3

def get_last_id():
    conn = sqlite3.connect('characters.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS characters (id INTEGER PRIMARY KEY, name TEXT, description TEXT)")
    c.execute("SELECT id FROM characters ORDER BY id DESC LIMIT 1")
    last_id = c.fetchone()
    c.close()
    conn.close()
    return last_id

class Character:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


    def print_database(self):
        conn = sqlite3.connect('characters.db')
        c = conn.cursor()
        c.execute("SELECT * FROM characters")
        rows = c.fetchall()
        for row in rows:
            print(row)
        c.close()
        conn.close()
    
    def save_character(self):
        conn = sqlite3.connect('characters.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS characters (id INTEGER PRIMARY KEY, name TEXT, description TEXT)")
        c.execute("INSERT OR IGNORE INTO characters (id, name, description) VALUES (?, ?, ?)", (self.id, self.name, self.description))
        conn.commit()
        c.close()
        conn.close()




    

    
