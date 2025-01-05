import sqlite3

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def print_database(self):
        try:
            with sqlite3.connect('users.db') as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM users")
                rows = c.fetchall()
                return rows
        except sqlite3.Error as e:
            print(f"Error reading database: {e}")
            return []

    def save_user(self):
        try:
            with sqlite3.connect('users.db') as conn:
                c = conn.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT)")
                c.execute("INSERT OR IGNORE INTO users (email, password) VALUES (?, ?)", (self.email, self.password))
                conn.commit()
            print("User saved successfully")
        except sqlite3.Error as e:
            print(f"Error saving user: {e}")

    def verify_user(self):
        try:
            with sqlite3.connect('users.db') as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM users WHERE email = ? AND password = ?", (self.email,self.password))
                user = c.fetchone()
                if user:
                    print(f"User found: {user}")
                    return True
                else:
                    print("User not found")
                    return False
                    
        except sqlite3.Error as e:
            print(f"Error verifying user: {e}")
            return False

    def delete_user(self):
        try:
            with sqlite3.connect('users.db') as conn:
                c = conn.cursor()
                c.execute("DELETE FROM users WHERE email = ?", (self.email,))
                conn.commit()
            print(f"User with email {self.email} deleted successfully")
        except sqlite3.Error as e:
            print(f"Error deleting user: {e}")

    def clear_all_users(self):
        try:
            with sqlite3.connect('users.db') as conn:
                c = conn.cursor()
                c.execute("DELETE FROM users")
                conn.commit()
            print("All users deleted successfully")
        except sqlite3.Error as e:
            print(f"Error clearing users: {e}")

    def add_message(self, message, id):
        try:
            with sqlite3.connect('users.db') as conn:
                c = conn.cursor()
                c.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id TEXT PRIMARY KEY,
                        message TEXT
                    )
                """)

                # Check if the ID already exists
                c.execute("SELECT message FROM users WHERE id = ?", (id,))
                result = c.fetchone()

                if result:
                    # If the ID exists, append the new message to the existing ones
                    existing_messages = result[0]
                    updated_messages = f"{existing_messages}|{message}"
                    c.execute("UPDATE users SET message = ? WHERE id = ?", (updated_messages, id))
                else:
                    # If the ID doesn't exist, insert a new record
                    c.execute("INSERT INTO users (id, message) VALUES (?, ?)", (id, message))

                conn.commit()
                print("User saved successfully")
        except sqlite3.Error as e:
            print(f"Error saving user: {e}")

    def get_character_messages(self, id):
        try:
            with sqlite3.connect('users.db') as conn:
                c = conn.cursor()

                # Check if the ID exists and fetch the message(s)
                c.execute("SELECT message FROM users WHERE id = ?", (id,))
                result = c.fetchone()

                if result:
                    return result[0]  # Return the message(s) associated with the ID
                else:
                    return None  # No record found for the given ID
        except sqlite3.Error as e:
            print(f"Error fetching messages: {e}")
            return None  # Return None in case of an error

