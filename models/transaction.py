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
     from_user TEXT,
     status TEXT DEFAULT 'Pending'
     )
     """)
    conn.commit()
    conn.close()

def save_proposal(listing_id, username, item, description, from_user):
    conn = sqlite3.connect("barterboard.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO proposals (listing_id, username, item, description, from_user, status)
        VALUES (?, ?, ?, ?, ?, 'Pending')
    """, (listing_id, username, item, description, from_user))
    conn.commit()
    conn.close()


def add_transaction_table():
    conn = sqlite3.connect("barterboard.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transaction_history (
        id INTEGER PRIMARY KEY,
        username TEXT,
        item TEXT,
        description TEXT,
        quantity INTEGER,
        location TEXT,
        traded_with TEXT
    )
    """)

    conn.commit()
    conn.close()