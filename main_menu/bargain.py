from models.user import *
import sqlite3

def bargain(username, listings):
    """
    Handles the Bargain functionality under the BARTERBOARD
    Args:
        username (str): The username of the current user.
        listings (list): The items displayed on the barterboard.
    """

    conn = sqlite3.connect("barterboard.db")
    cursor = conn.cursor()
    name = list(User.get_logged_in_user())
    final_name = name[1]

    while True:
        print("\nBARGAIN")
        print("Note: Type 'x' to exit at any time.")

        trade_request = input("\nEnter the ID of the item you want to trade: ")
        if trade_request.lower() == 'x':
            return

        if not trade_request.isdigit():
            print("Invalid ID. Please enter a numeric ID.")
            continue

        trade_request = int(trade_request)
        selected_item = next((item for item in listings if item["id"] == trade_request), None)

        if not selected_item:
            print("Item ID not found. Please try again.")
            continue

        if selected_item["username"] == final_name:
            print("You cannot trade for your own item.")
            continue

        print(f"\nYou selected Item ID {trade_request}: {selected_item['item']}")
        print("Proceeding to trade details...\n")

        # TRADE PROPOSAL DETAILS
        while True:
            item = input("Enter item name: ")
            if item.lower() == 'x':
                return
            if len(item) > 3:
                break
            print("Name must be longer than 3 characters.")
                
        while True:
            description = input("Enter item description: ")
            if description.lower() == 'x':
                return
            if len(description) > 5:
                break
            print("Description must be longer than 5 characters.")
        
        while True:
            quantity = input("Enter item quantity: ")
            if quantity.lower() == 'x':
                return
            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                break
            print("Quantity must be a positive number.")        

        while True:
            location = input("Enter pickup location: ")
            if location.lower() == 'x':
                return
            if len(location) > 3:
                break
            print("Location must be longer than 3 characters.")

        cursor.execute("SELECT id FROM listings WHERE id = ?", (trade_request,))
        listing_result = cursor.fetchone()

        if not listing_result:
            print("Error: Listing not found.")
            conn.close()
            return

        listing_id = listing_result[0]

        cursor.execute("""
        INSERT INTO proposals (username, item, description, from_user, status, listing_id)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (selected_item["username"], item, description, final_name, "Pending", listing_id))
        
        conn.commit()
        print("Trade request sent successfully!")
                
        print(f"Trade proposal for {item} has been sent to the other user!")
        conn.close()
        return