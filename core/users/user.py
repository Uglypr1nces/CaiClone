import sqlite3

class User:
    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username
        self._initialize_database()

    def _initialize_database(self):
        try:
            with sqlite3.connect('users.db') as conn:
                c = conn.cursor()
                # Create users table if not exists
                c.execute("CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT, username TEXT)")
                # Create characters table if not exists
                c.execute("""
                    CREATE TABLE IF NOT EXISTS characters (
                        user_email TEXT,
                        character_id TEXT,
                        PRIMARY KEY (user_email, character_id),
                        FOREIGN KEY (user_email) REFERENCES users (email)
                    )
                """)
                # Create messages table if not exists
                c.execute("""
                    CREATE TABLE IF NOT EXISTS messages (
                        user_email TEXT,
                        character_id TEXT,
                        message TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        PRIMARY KEY (user_email, character_id, timestamp),
                        FOREIGN KEY (user_email) REFERENCES users (email),
                        FOREIGN KEY (character_id) REFERENCES characters (character_id)
                    )
                """)
                conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")

    def update_user(self, mail, password, username):
        self.email = mail
        self.password = password
        self.username = username

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
                # Create users table if not exists
                c.execute("CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT, username TEXT)")
                c.execute("INSERT OR IGNORE INTO users (email, password, username) VALUES (?, ?, ?)", (self.email, self.password, self.username))
                conn.commit()
            print("User saved successfully")
        except sqlite3.Error as e:
            print(f"Error saving user: {e}")

    def verify_user(self):
        try:
            with sqlite3.connect('users.db') as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM users WHERE email = ? AND password = ?", (self.email, self.password))
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
                c.execute("DELETE FROM characters WHERE user_email = ?", (self.email,))
                c.execute("DELETE FROM messages WHERE user_email = ?", (self.email,))
                conn.commit()
            print(f"User with email {self.email} deleted successfully")
        except sqlite3.Error as e:
            print(f"Error deleting user: {e}")

    def clear_all_users(self):
        try:
            with sqlite3.connect('users.db') as conn:
                c = conn.cursor()
                c.execute("DELETE FROM users")
                c.execute("DELETE FROM characters")
                c.execute("DELETE FROM messages")
                conn.commit()
            print("All users deleted successfully")
        except sqlite3.Error as e:
            print(f"Error clearing users: {e}")

    def add_character(self, character_id):
        try:
            with sqlite3.connect('users.db') as conn:
                c = conn.cursor()
                # Create characters table if not exists
                c.execute("""
                    CREATE TABLE IF NOT EXISTS characters (
                        user_email TEXT,
                        character_id TEXT,
                        PRIMARY KEY (user_email, character_id),
                        FOREIGN KEY (user_email) REFERENCES users (email)
                    )
                """)
                # Insert character for the user
                c.execute("INSERT OR IGNORE INTO characters (user_email, character_id) VALUES (?, ?)", (self.email, character_id))
                conn.commit()
            print(f"Character {character_id} added for user {self.email}")
        except sqlite3.Error as e:
            print(f"Error adding character: {e}")

    def add_message(self, character_id, message):
        try:
            with sqlite3.connect('users.db') as conn:
                c = conn.cursor()
                # Create messages table if not exists
                c.execute("""
                    CREATE TABLE IF NOT EXISTS messages (
                        user_email TEXT,
                        character_id TEXT,
                        message TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        PRIMARY KEY (user_email, character_id, timestamp),
                        FOREIGN KEY (user_email) REFERENCES users (email),
                        FOREIGN KEY (character_id) REFERENCES characters (character_id)
                    )
                """)
                # Insert message for the character
                c.execute("INSERT INTO messages (user_email, character_id, message) VALUES (?, ?, ?)", (self.email, character_id, message))
                conn.commit()
            print("Message saved successfully")
        except sqlite3.Error as e:
            print(f"Error saving message: {e}")

    def get_messages_for_character(self, character_id):
        try:
            with sqlite3.connect('users.db') as conn:
                c = conn.cursor()
                # Retrieve messages for the given character_id for the user
                c.execute("""
                    SELECT message, timestamp FROM messages
                    WHERE user_email = ? AND character_id = ?
                    ORDER BY timestamp
                """, (self.email, character_id))
                messages = c.fetchall()
                return messages if messages else None
        except sqlite3.Error as e:
            print(f"Error fetching messages: {e}")
            return None
        
    def get_characters(self):
        try:
            with sqlite3.connect('users.db') as conn:
                c = conn.cursor()
                c.execute("SELECT character_id FROM characters WHERE user_email = ?", (self.email,))
                characters = c.fetchall()
                return [character[0] for character in characters] if characters else []
        except sqlite3.Error as e:
            print(f"Error fetching characters: {e}")
            return None
        

    def get_username(self):
        try:
            with sqlite3.connect('users.db') as conn:
                c = conn.cursor()
                c.execute("SELECT username FROM users WHERE email = ?", (self.email,))
                result = c.fetchone()
                if result:
                    return result[0]
                else:
                    print("Username not found for the provided email")
                    return None
        except sqlite3.Error as e:
            print(f"Error fetching username: {e}")
            return None
