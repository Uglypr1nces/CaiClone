import sqlite3

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


    def print_database(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        rows = c.fetchall()
        users = []
        for row in rows:
            users.append(row)
        c.close()
        conn.close()
        return users
    
    def save_user(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT)")
        c.execute("INSERT OR IGNORE INTO users (email, password) VALUES (?, ?)", (self.email, self.password))
        conn.commit()
        c.close()
        conn.close()

        print("Character saved successfully")

    def delete_character(self, id):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE id = ?", (id,))
        conn.commit()
        c.close()
        conn.close()

    def clear_all_users(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("DELETE FROM users")
        conn.commit()
        c.close()
        conn.close()

        print("Character deleted successfully")





    

    
