import sqlite3

def add_proposal_table():
    conn = sqlite3.connect("barterboard.db")
    cursor = conn.cursor()
    # Create the proposals table if it doesn't exist
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS proposals (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     listing_id INTEGER NOT NULL, 
     username TEXT,
     item TEXT,
     description TEXT,
     quantity INTEGER,
     from_user TEXT,
     status TEXT DEFAULT 'Pending'
     )
     """)
    conn.commit()
    conn.close()

def save_proposal(listing_id, username, item, description, quantity, from_user):
    conn = sqlite3.connect("barterboard.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO proposals (listing_id, username, item, description, quantity, from_user, status)
        VALUES (?, ?, ?, ?, ?, 'Pending')
    """, (listing_id, username, item, description, quantity, from_user))
    conn.commit()
    conn.close()


def add_transaction_table():
    conn = sqlite3.connect("barterboard.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        from_user TEXT,
        to_user TEXT,
        item TEXT,
        description TEXT,
        quantity INTEGER,
        location TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()