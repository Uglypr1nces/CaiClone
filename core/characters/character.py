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

def get_character(id):
    conn = sqlite3.connect('characters.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS characters (id INTEGER PRIMARY KEY, name TEXT, description TEXT)")
    c.execute("SELECT name FROM characters WHERE id = ?", (id,))
    character = c.fetchone()
    c.close()
    conn.close()
    return character

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
        characters = []
        for row in rows:
            characters.append(row)
        c.close()
        conn.close()
        return characters
    
    def save_character(self):
        conn = sqlite3.connect('characters.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS characters (id INTEGER PRIMARY KEY, name TEXT, description TEXT)")
        c.execute("INSERT OR IGNORE INTO characters (id, name, description) VALUES (?, ?, ?)", (self.id, self.name, self.description))
        conn.commit()
        c.close()
        conn.close()

        print("Character saved successfully")

    def delete_character(self, id):
        conn = sqlite3.connect('characters.db')
        c = conn.cursor()
        c.execute("DELETE FROM characters WHERE id = ?", (id,))
        conn.commit()
        c.close()
        conn.close()

    def clear_all_characters(self):
        conn = sqlite3.connect('characters.db')
        c = conn.cursor()
        c.execute("DELETE FROM characters")
        conn.commit()
        c.close()
        conn.close()

        print("Character deleted successfully")





    

    
