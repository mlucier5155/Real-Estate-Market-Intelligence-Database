import sqlite3
import pandas as pd
import os


# Database setup - this builds the DB from CSV files automatically
def init_db():
    print("Checking database files...")
    db = sqlite3.connect('real_estate.db')

    # must match CSV filenames exactly
    files = {
        'property.csv': 'PROPERTY',
        'zipcode.csv': 'ZIPCODE',
        'price_history.csv': 'PRICE_HISTORY'
    }

    for f, table in files.items():
        if os.path.exists(f):
            data = pd.read_csv(f)
            data.to_sql(table, db, if_exists='replace', index=False)
        else:
            print(f"Warning: {f} not found in folder.")

    db.close()
    print("Database is ready.\n")


def run_app():
    init_db()
    conn = sqlite3.connect('real_estate.db')

    while True:
        print("\n--- Real Estate Insights Portal ---")
        print("1. Find City/State by Address")
        print("2. Check Price History")
        print("3. Properties in a Zip Code")
        print("4. Show Large Houses (>3 beds)")
        print("5. Update Square Footage")
        print("0. Exit")

        user_input = input("Choose an option: ")

        # Feature 1: Join Property and Zipcode
        if user_input == '1':
            search = input("Enter address (e.g. 101 Main St): ")
            sql = """
                SELECT P.Address, Z.City, Z.State 
                FROM PROPERTY P 
                JOIN ZIPCODE Z ON P.ZipCode = Z.ZipCode 
                WHERE P.Address = ?
            """
            res = conn.execute(sql, (search,)).fetchall()
            if res:
                for r in res:
                    print(f"Result: {r[0]} is located in {r[1]}, {r[2]}")
            else:
                print(f"Sorry, no property was found with the address: '{search}'")

        # Feature 2: Join Property and Price History
        elif user_input == '2':
            id_val = input("Enter Property ID (e.g. P1): ")
            sql = """
                SELECT P.Address, H.SalePrice 
                FROM PRICE_HISTORY H 
                JOIN PROPERTY P ON H.PropertyID = P.PropertyID 
                WHERE P.PropertyID = ?
            """
            res = conn.execute(sql, (id_val,)).fetchall()
            if res:
                print(f"Showing history for {id_val}:")
                for r in res:
                    print(f" - {r[0]} | Last Sold: ${r[1]:,}")
            else:
                print(f"No price history records found for ID: '{id_val}'")

        # Feature 3: Join Property and Zipcode (Filter)
        elif user_input == '3':
            zip_val = input("Enter Zip Code: ")
            sql = """
                SELECT P.Address, Z.City 
                FROM PROPERTY P 
                JOIN ZIPCODE Z ON P.ZipCode = Z.ZipCode 
                WHERE P.ZipCode = ?
            """
            res = conn.execute(sql, (zip_val,)).fetchall()
            if res:
                print(f"Properties found in {zip_val}:")
                for r in res:
                    print(f" - {r[0]} ({r[1]})")
            else:
                print(f"No properties found in the database for Zip Code: {zip_val}")

        # Feature 4: Simple Select
        elif user_input == '4':
            sql = "SELECT Address, Bedrooms FROM PROPERTY WHERE Bedrooms > 3"
            res = conn.execute(sql).fetchall()
            if res:
                print("Houses with more than 3 bedrooms:")
                for r in res:
                    print(f" - {r[0]} ({r[1]} bedrooms)")
            else:
                print("No large houses (4+ bedrooms) were found in the database.")

        # Feature 5: Update with check
        elif user_input == '5':
            target_id = input("Property ID to update: ")

            # check if the ID exists first so we can show an error if it doesn't
            check = conn.execute("SELECT Address FROM PROPERTY WHERE PropertyID = ?", (target_id,)).fetchone()

            if check:
                new_val = input(f"Enter new Square Footage for {check[0]}: ")
                conn.execute("UPDATE PROPERTY SET SquareFootage = ? WHERE PropertyID = ?", (new_val, target_id))
                conn.commit()
                print("Update successful!")
            else:
                print(f"Error: Property ID '{target_id}' does not exist. No update performed.")

        elif user_input == '0':
            print("Closing application...")
            break

        else:
            print("That is not a valid option, please try again.")

    conn.close()


if __name__ == "__main__":
    run_app()