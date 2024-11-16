import pandas as pd
import mysql.connector
from mysql.connector import Error
import numpy as np

# Load Excel file
excel_file = "RestaurantDB_Excel.xlsx"
restaurants_df = pd.read_excel(excel_file, sheet_name="Restaurants")
restaurants_df.columns = restaurants_df.columns.str.strip()  # Strip whitespace from column names

try:
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mistoquente",
        auth_plugin='mysql_native_password',
        database="RestaurantsDB"
    )
    cursor = conn.cursor()

    # Get the UserID for danimellok
    cursor.execute("SELECT UserID FROM AppUser WHERE UserName = 'danimellok'")
    user_id = cursor.fetchone()[0]

    # Populate Restaurant table
    for _, row in restaurants_df.iterrows():
        # Ensure all NaN values are converted to None for each column individually
        restaurant_name = row['Restaurant Name'] if not pd.isna(row['Restaurant Name']) else None
        country = row['Country'] if not pd.isna(row['Country']) else None
        city = row['City'] if not pd.isna(row['City']) else None
        cuisine = row['Cuisine'] if not pd.isna(row['Cuisine']) else None
        michelin_rating = row['MichelinRating'] if not pd.isna(row['MichelinRating']) else None
        overall_rating = row['OverallRating'] if not pd.isna(row['OverallRating']) else None

        # Insert into Restaurant table
        cursor.execute('''INSERT INTO Restaurant (RestaurantName, Country, City, Cuisine, MichelinRating, Price)
                          VALUES (%s, %s, %s, %s, %s, %s)''', 
                       (restaurant_name, country, city, cuisine, michelin_rating, overall_rating))
        
        # Get the last inserted RestaurantID
        restaurant_id = cursor.lastrowid

        # Insert into Visit table without VisitDate, VisitPrice, and Reservation
        cursor.execute('''INSERT INTO Visit (RestaurantID, UserID)
                          VALUES (%s, %s)''', 
                       (restaurant_id, user_id))

        # Insert into Review table if OverallRating is available
        if overall_rating is not None:
            # Placeholder ratings if data is missing
            food_rating = None  # Replace with actual data if available
            service_rating = None  # Replace with actual data if available
            
            # Get the last inserted VisitID for the Review table
            visit_id = cursor.lastrowid
            cursor.execute('''INSERT INTO Review (OveralRating, FoodRating, ServiceRating, VisitID)
                              VALUES (%s, %s, %s, %s)''', 
                           (overall_rating, food_rating, service_rating, visit_id))

    # Commit all changes
    conn.commit()
    print("Data inserted successfully.")

except Error as e:
    print(f"Error: {e}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
