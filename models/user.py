# THE USER CLASS
import sqlite3

# Database setup

current_user = None

def setup_database():
    conn = sqlite3.connect("barterboard.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

class User:
    def __init__(self, username, password):
        """ Initialize the User object with a username and password. """
        self.username = username
        self.password = password

    @staticmethod
    def register(username, password):
        """ Registers a new user in the database. """
        conn = sqlite3.connect("barterboard.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            print("Account successfully created!")
            return True
        except sqlite3.IntegrityError:
            print("Username already exists. Please try again.")
            return False
        finally:
            conn.close()

    @staticmethod
    def login(username, password):
        """Checks user credentials in the database."""
        conn = sqlite3.connect("barterboard.db")
        global current_user
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            current_user = user
            print(f"Logged in as {username}")
            return True
        else:
            print("Invalid username or password.")
            return False
    
    @staticmethod
    def get_logged_in_user():
        """Returns the logged-in user if available"""
        return current_user
    
        