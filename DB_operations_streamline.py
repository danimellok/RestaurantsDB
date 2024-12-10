import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px


# Database configuration
DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mistoquente',
    'database': 'RestaurantsDB'
}


def export_csv(dataframe, filename):
    """
    Creates a CSV download button in Streamlit.

    Args:
        dataframe (pd.DataFrame): The DataFrame to export.
        filename (str): The name of the CSV file to be downloaded.
    """
    csv = dataframe.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name=filename,
        mime="text/csv",
    )


# Function to connect to MySQL
def get_connection():
    return mysql.connector.connect(**DATABASE_CONFIG)


# HOME PAGE
#HOME PAGE V1
#def home_page():
    """
    Displays the home page with a program description and basic statistics.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor()

        # Query to get total number of restaurants
        cursor.execute("SELECT COUNT(*) FROM Restaurant WHERE is_active = 1")
        total_restaurants = cursor.fetchone()[0]

        # Query to get the number of unique cities
        cursor.execute("SELECT COUNT(DISTINCT City) FROM Restaurant WHERE is_active = 1")
        total_cities = cursor.fetchone()[0]

        # Query to get the number of unique countries
        cursor.execute("SELECT COUNT(DISTINCT Country) FROM Restaurant WHERE is_active = 1")
        total_countries = cursor.fetchone()[0]

        # Display program description
        st.title("Welcome to the Restaurant Database Management System!")
        st.write("""
            This application helps you manage, view, and analyze data about high-quality restaurants.
            Whether you're exploring Michelin-starred establishments, filtering by cuisine, or reviewing 
            overall ratings, this tool is designed to provide an easy and interactive experience.
        """)

        # Display statistics
        st.header("Current Database Statistics")
        st.metric(label="Total Restaurants", value=total_restaurants)
        st.metric(label="Cities Covered", value=total_cities)
        st.metric(label="Countries Covered", value=total_countries)

    except mysql.connector.Error as e:
        st.error(f"An error occurred: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


#HOME PAGE V2 - Graphs and search bar
#def home_page():
    """
    Home page for the application with interactive graphs, charts, and search functionality.
    """
    st.title("Restaurant Database Dashboard")
    st.write("Welcome to the Restaurant Database application! Explore a curated list of restaurants, their ratings, and visits. Use the filters and interactive graphs below to analyze and search data.")

    # Connect to MySQL database
    try:
        conn = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = conn.cursor()

        # Query for statistics
        cursor.execute("SELECT COUNT(*) FROM Restaurant WHERE is_active = 1")
        total_restaurants = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(DISTINCT City) FROM Restaurant WHERE is_active = 1")
        total_cities = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(DISTINCT Country) FROM Restaurant WHERE is_active = 1")
        total_countries = cursor.fetchone()[0]

        # Display stats
        st.metric("Total Restaurants", total_restaurants)
        st.metric("Unique Cities", total_cities)
        st.metric("Unique Countries", total_countries)

        # Interactive Graphs and Charts
        st.subheader("Cuisine Distribution")
        cursor.execute("SELECT Cuisine, COUNT(*) FROM Restaurant WHERE is_active = 1 GROUP BY Cuisine")
        cuisine_data = cursor.fetchall()
        if cuisine_data:
            df_cuisine = pd.DataFrame(cuisine_data, columns=["Cuisine", "Count"])
            st.plotly_chart(px.pie(df_cuisine, names="Cuisine", values="Count", title="Cuisine Distribution"))
        else:
            st.write("No data available for cuisine distribution.")

        st.subheader("Top 10 Cities by Restaurant Count")
        cursor.execute("SELECT City, COUNT(*) FROM Restaurant WHERE is_active = 1 GROUP BY City ORDER BY COUNT(*) DESC LIMIT 10")
        city_data = cursor.fetchall()
        if city_data:
            df_city = pd.DataFrame(city_data, columns=["City", "Count"])
            st.bar_chart(df_city.set_index("City"))
        else:
            st.write("No data available for top cities.")

        # Interactive Search
        st.subheader("Search Restaurants")
        search_query = st.text_input("Search for a restaurant by name:")
        if search_query:
            cursor.execute("SELECT RestaurantName, City, Country FROM Restaurant WHERE RestaurantName LIKE %s AND is_active = 1", (f"%{search_query}%",))
            search_results = cursor.fetchall()

            if search_results:
                st.write("Search Results:")
                for result in search_results:
                    st.write(f"**{result[0]}** - {result[1]}, {result[2]}")
            else:
                st.write("No restaurants found matching your search.")

    except mysql.connector.Error as e:
        st.error(f"An error occurred: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

#HOME PAGE V3 - WIth search bar new
# HOME PAGE V2 - Graphs and search bar with detailed search results
def home_page():
    """
    Home page for the application with interactive graphs, charts, and enhanced search functionality.
    """
    st.title("Restaurant Database Dashboard")
    st.write("Welcome to the Restaurant Database application! Explore a curated list of restaurants, their ratings, and visits. Use the filters and interactive graphs below to analyze and search data.")

    # Connect to MySQL database
    try:
        conn = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = conn.cursor()

        # Query for statistics
        cursor.execute("SELECT COUNT(*) FROM Restaurant WHERE is_active = 1")
        total_restaurants = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(DISTINCT City) FROM Restaurant WHERE is_active = 1")
        total_cities = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(DISTINCT Country) FROM Restaurant WHERE is_active = 1")
        total_countries = cursor.fetchone()[0]

        # Display stats
        st.metric("Total Restaurants", total_restaurants)
        st.metric("Unique Cities", total_cities)
        st.metric("Unique Countries", total_countries)

        # Interactive Graphs and Charts
        st.subheader("Cuisine Distribution")
        cursor.execute("SELECT Cuisine, COUNT(*) FROM Restaurant WHERE is_active = 1 GROUP BY Cuisine")
        cuisine_data = cursor.fetchall()
        if cuisine_data:
            df_cuisine = pd.DataFrame(cuisine_data, columns=["Cuisine", "Count"])
            st.plotly_chart(px.pie(df_cuisine, names="Cuisine", values="Count", title="Cuisine Distribution"))
        else:
            st.write("No data available for cuisine distribution.")

        st.subheader("Top 10 Cities by Restaurant Count")
        cursor.execute("SELECT City, COUNT(*) FROM Restaurant WHERE is_active = 1 GROUP BY City ORDER BY COUNT(*) DESC LIMIT 10")
        city_data = cursor.fetchall()
        if city_data:
            df_city = pd.DataFrame(city_data, columns=["City", "Count"])
            st.bar_chart(df_city.set_index("City"))
        else:
            st.write("No data available for top cities.")

        # Interactive Search
        st.subheader("Search Restaurants")
        search_query = st.text_input("Search for a restaurant by name:")
        if search_query:
            cursor.execute("""
                SELECT 
                    Restaurant.RestaurantName, 
                    Restaurant.City, 
                    Restaurant.Country, 
                    COALESCE(Restaurant.MichelinRating, 'No Michelin Star') AS MichelinStar, 
                    AVG(Review.OveralRating) AS OverallRating
                FROM Restaurant
                LEFT JOIN Visit ON Restaurant.RestaurantID = Visit.RestaurantID
                LEFT JOIN Review ON Visit.VisitID = Review.VisitID
                WHERE Restaurant.RestaurantName LIKE %s AND Restaurant.is_active = 1
                GROUP BY Restaurant.RestaurantID
            """, (f"%{search_query}%",))
            search_results = cursor.fetchall()

            if search_results:
                st.write("Search Results:")
                for result in search_results:
                    restaurant_name, city, country, michelin_star, overall_rating = result
                    st.write(f"**{restaurant_name}** - {city}, {country}")
                    st.write(f"- Michelin Star: {michelin_star}")
                    st.write(f"- Overall Rating: {overall_rating:.2f}")

                    # Fetch dish reviews for this restaurant
                    cursor.execute("""
                        SELECT DishName, DishRating, Notes 
                        FROM MenuItem 
                        WHERE RestaurantID = (
                            SELECT RestaurantID 
                            FROM Restaurant 
                            WHERE RestaurantName = %s AND is_active = 1
                        )
                    """, (restaurant_name,))
                    dish_reviews = cursor.fetchall()

                    if dish_reviews:
                        st.write("  - **Dish Reviews:**")
                        for dish in dish_reviews:
                            dish_name, dish_rating, notes = dish
                            st.write(f"    - {dish_name} (Rating: {dish_rating}) - Notes: {notes}")
                    else:
                        st.write("  - **Dish Reviews:** None Available")
            else:
                st.write("No restaurants found matching your search.")

    except mysql.connector.Error as e:
        st.error(f"An error occurred: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# VIEW ALL RESTAURANTS
def view_all_restaurants():
    """
    Displays all restaurants with relevant details and allows CSV export.
    Excludes RestaurantID and is_active, and replaces Price with OverallRating.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        
        # Updated query
        query = """
    SELECT 
        RestaurantName, 
        Country, 
        City, 
        Cuisine,  -- Ensure this matches the actual column name
        MichelinRating, 
        (
            SELECT AVG(Review.OveralRating)
            FROM Visit
            JOIN Review ON Visit.VisitID = Review.VisitID
            WHERE Visit.RestaurantID = Restaurant.RestaurantID
        ) AS OverallRating
    FROM Restaurant
    WHERE is_active = 1;
"""
        cursor.execute(query)
        results = cursor.fetchall()
        
        # Display results
        if results:
            df = pd.DataFrame(results)
            df['OverallRating'] = df['OverallRating'].round(2)  # Round ratings for better display
            st.dataframe(df)
            export_csv(df, "all_restaurants.csv")
        else:
            st.write("No restaurants found.")
    finally:
        conn.close()


#2. FILTER RESTAURANTS
def filter_restaurants(country='', city='', cuisine='', overall_rating=None, michelin_only=False):
    """
    Filters restaurants based on provided criteria.

    Args:
        country (str): Country to filter by (optional).
        city (str): City to filter by (optional).
        cuisine (str): Cuisine to filter by (optional).
        overall_rating (int): Overall rating to filter by (optional).
        michelin_only (bool): Whether to filter only Michelin-rated restaurants.

    Returns:
        list: Filtered restaurant results as dictionaries.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT 
                Restaurant.RestaurantName, 
                Restaurant.Country, 
                Restaurant.City, 
                Restaurant.Cuisine, 
                Restaurant.MichelinRating, 
                (
                    SELECT AVG(Review.OveralRating)
                    FROM Review
                    JOIN Visit ON Review.VisitID = Visit.VisitID
                    WHERE Visit.RestaurantID = Restaurant.RestaurantID
                ) AS OverallRating
            FROM Restaurant
            WHERE is_active = 1
        """
        params = []

        if country:
            query += " AND Restaurant.Country = %s"
            params.append(country)

        if city:
            query += " AND Restaurant.City = %s"
            params.append(city)

        if cuisine:
            query += " AND Restaurant.Cuisine = %s"
            params.append(cuisine)

        if overall_rating is not None:
            query += " HAVING OverallRating >= %s"
            params.append(overall_rating)

        if michelin_only:
            query += " AND Restaurant.MichelinRating IS NOT NULL AND Restaurant.MichelinRating > 0"

        cursor.execute(query, params)
        results = cursor.fetchall()
        return results

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


# 3. View Reviews
def fetch_reviews(filter_type=None, filter_value=None):
    """
    Fetches detailed reviews with optional filters for country, city, or cuisine.

    Args:
        filter_type (str): The column to filter by (e.g., 'Country', 'City', 'Cuisine').
        filter_value (str): The value to filter by (e.g., 'USA', 'New York', 'Italian').

    Returns:
        list: List of reviews as dictionaries.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT 
                Restaurant.RestaurantName,
                AppUser.UserName,
                Review.OveralRating,
                Review.FoodRating,
                Review.ServiceRating,
                Visit.VisitDate,
                Visit.VisitPrice,
                Visit.Reservation,
                MenuItem.DishName,
                MenuItem.DishRating,
                MenuItem.Notes
            FROM Review
            JOIN Visit ON Review.VisitID = Visit.VisitID
            JOIN Restaurant ON Visit.RestaurantID = Restaurant.RestaurantID
            JOIN AppUser ON Visit.UserID = AppUser.UserID
            LEFT JOIN MenuItem ON MenuItem.RestaurantID = Restaurant.RestaurantID
            WHERE 1=1
        """

        params = []
        if filter_type and filter_value:
            query += f" AND Restaurant.{filter_type} = %s"
            params.append(filter_value)

        cursor.execute(query, params)
        results = cursor.fetchall()
        return results

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()



def add_restaurant_visit(username, restaurant_name, country, city, cuisine, michelin_rating, price,
                         visit_date, visit_price, reservation, overall_rating, food_rating, service_rating, menu_items):
    """
    Adds a new restaurant visit with user, restaurant, visit, review, and optional menu item details.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor()

        # Check if username exists
        cursor.execute("SELECT UserID FROM AppUser WHERE UserName = %s", (username,))
        user = cursor.fetchone()

        if user:
            user_id = user[0]
        else:
            return "User not found. Please create a new user."

        # Handle Michelin Rating
        michelin_rating = michelin_rating if michelin_rating != 0 else None

        # Get or create the restaurant
        cursor.execute(
            """
            SELECT RestaurantID FROM Restaurant 
            WHERE RestaurantName = %s AND Country = %s AND City = %s AND Cuisine = %s
            """,
            (restaurant_name, country, city, cuisine)
        )
        restaurant = cursor.fetchone()
        if restaurant:
            restaurant_id = restaurant[0]
        else:
            cursor.execute(
                """
                INSERT INTO Restaurant (RestaurantName, Country, City, Cuisine, MichelinRating, Price)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (restaurant_name, country, city, cuisine, michelin_rating, price)
            )
            restaurant_id = cursor.lastrowid

        # Add visit details
        cursor.execute(
            """
            INSERT INTO Visit (VisitDate, VisitPrice, Reservation, RestaurantID, UserID)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (visit_date, visit_price, reservation, restaurant_id, user_id)
        )
        visit_id = cursor.lastrowid

        # Add review details
        cursor.execute(
            """
            INSERT INTO Review (OveralRating, FoodRating, ServiceRating, VisitID)
            VALUES (%s, %s, %s, %s)
            """,
            (overall_rating, food_rating, service_rating, visit_id)
        )

        # Add menu items if provided
        for item in menu_items:
            cursor.execute(
                """
                INSERT INTO MenuItem (DishName, DishRating, Notes, RestaurantID)
                VALUES (%s, %s, %s, %s)
                """,
                (item["DishName"], item["DishRating"], item["Notes"], restaurant_id)
            )

        conn.commit()
        return "All details for the visit have been successfully added."
    except mysql.connector.Error as e:
        conn.rollback()
        return f"An error occurred: {e}"
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()



### 4. ADD RESTAURANT VISIT #V1 - Not adding the dish names
#def add_restaurant_visit(username, restaurant_name, country, city, cuisine, michelin_rating, price,
                         #visit_date, visit_price, reservation, overall_rating, food_rating, service_rating, menu_items):
    """
    Adds a new restaurant visit with user, restaurant, visit, review, and menu item details.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor()

        # Check if username exists
        cursor.execute("SELECT UserID FROM AppUser WHERE UserName = %s", (username,))
        user = cursor.fetchone()

        if user:
            user_id = user[0]
        else:
            return "User not found. Please create a new user."

        # Handle Michelin Rating
        michelin_rating = michelin_rating if michelin_rating != 0 else None

        # Get or create the restaurant
        cursor.execute(
            """
            SELECT RestaurantID FROM Restaurant 
            WHERE RestaurantName = %s AND Country = %s AND City = %s AND Cuisine = %s
            """,
            (restaurant_name, country, city, cuisine)
        )
        restaurant = cursor.fetchone()
        if restaurant:
            restaurant_id = restaurant[0]
        else:
            cursor.execute(
                """
                INSERT INTO Restaurant (RestaurantName, Country, City, Cuisine, MichelinRating, Price)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (restaurant_name, country, city, cuisine, michelin_rating, price)
            )
            restaurant_id = cursor.lastrowid

        # Add visit details
        cursor.execute(
            """
            INSERT INTO Visit (VisitDate, VisitPrice, Reservation, RestaurantID, UserID)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (visit_date, visit_price, reservation, restaurant_id, user_id)
        )
        visit_id = cursor.lastrowid

        # Add review details
        cursor.execute(
            """
            INSERT INTO Review (OveralRating, FoodRating, ServiceRating, VisitID)
            VALUES (%s, %s, %s, %s)
            """,
            (overall_rating, food_rating, service_rating, visit_id)
        )

        # Add menu items if provided
        for item in menu_items:
            cursor.execute(
                """
                INSERT INTO MenuItem (DishName, DishRating, Notes, RestaurantID)
                VALUES (%s, %s, %s, %s)
                """,
                (item["dish_name"], item["dish_rating"], item["notes"], restaurant_id)
            )

        conn.commit()
        return "All details for the visit have been successfully added."
    except mysql.connector.Error as e:
        conn.rollback()
        return f"An error occurred: {e}"
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

### CREATE USER FUNCTION TO ASSIST WITH ADD RESTAURANT
def create_user(username, join_date, email):
    """
    Creates a new user in the database.

    Args:
        username (str): The username of the new user.
        join_date (str): Join date of the new user.
        email (str): Email of the new user.

    Returns:
        str: Success message or error details.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor()

        # Insert the new user
        cursor.execute(
            "INSERT INTO AppUser (JoinDate, UserName, email) VALUES (%s, %s, %s)",
            (join_date, username, email)
        )
        conn.commit()
        return f"User '{username}' created successfully!"
    except mysql.connector.Error as e:
        conn.rollback()
        return f"An error occurred: {e}"
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


### 5. DELETE OR UPDATE 
def delete_or_update_restaurant():
    """
    Provides options to delete or update a restaurant's information.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)

        # Fetch all restaurants
        cursor.execute("SELECT RestaurantID, RestaurantName FROM Restaurant")
        restaurants = cursor.fetchall()

        if not restaurants:
            st.warning("No restaurants found.")
            return

        # Display restaurants in a dropdown
        restaurant_options = {r["RestaurantName"]: r["RestaurantID"] for r in restaurants}
        selected_restaurant = st.selectbox("Select a restaurant to delete or update:", list(restaurant_options.keys()))

        if selected_restaurant:
            restaurant_id = restaurant_options[selected_restaurant]
            action = st.radio("What do you want to do?", ["Delete", "Update"])

            if action == "Delete":
                if st.button(f"Delete {selected_restaurant}"):
                    # Delete related records in Review, Visit, and MenuItem
                    cursor.execute("DELETE FROM Review WHERE VisitID IN (SELECT VisitID FROM Visit WHERE RestaurantID = %s)", (restaurant_id,))
                    cursor.execute("DELETE FROM Visit WHERE RestaurantID = %s", (restaurant_id,))
                    cursor.execute("DELETE FROM MenuItem WHERE RestaurantID = %s", (restaurant_id,))
                    
                    # Delete the restaurant itself
                    cursor.execute("DELETE FROM Restaurant WHERE RestaurantID = %s", (restaurant_id,))
                    
                    conn.commit()
                    st.success(f"Restaurant '{selected_restaurant}' and all associated records have been permanently deleted.")

            elif action == "Update":
                # Update restaurant details
                st.subheader(f"Update details for '{selected_restaurant}'")
                new_name = st.text_input("New Restaurant Name", value=selected_restaurant)
                new_country = st.text_input("New Country")
                new_city = st.text_input("New City")
                new_cuisine = st.text_input("New Cuisine")
                new_michelin_rating = st.number_input("New Michelin Rating (Leave blank for none)", min_value=0, step=1)
                new_price = st.number_input("New Price Rating", min_value=0, step=1)

                if st.button(f"Update {selected_restaurant}"):
                    # Update only the fields with new values
                    if new_name:
                        cursor.execute("UPDATE Restaurant SET RestaurantName = %s WHERE RestaurantID = %s", (new_name, restaurant_id))
                    if new_country:
                        cursor.execute("UPDATE Restaurant SET Country = %s WHERE RestaurantID = %s", (new_country, restaurant_id))
                    if new_city:
                        cursor.execute("UPDATE Restaurant SET City = %s WHERE RestaurantID = %s", (new_city, restaurant_id))
                    if new_cuisine:
                        cursor.execute("UPDATE Restaurant SET Cuisine = %s WHERE RestaurantID = %s", (new_cuisine, restaurant_id))
                    if new_michelin_rating:
                        cursor.execute("UPDATE Restaurant SET MichelinRating = %s WHERE RestaurantID = %s", (new_michelin_rating, restaurant_id))
                    if new_price:
                        cursor.execute("UPDATE Restaurant SET Price = %s WHERE RestaurantID = %s", (new_price, restaurant_id))
                    
                    conn.commit()
                    st.success(f"Restaurant '{new_name}' has been updated.")
    except mysql.connector.Error as e:
        st.error(f"An error occurred: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

### SUPPORT FUNCTION FOR 5
def delete_review():
    """
    Permanently deletes a specific review based on ReviewID.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        # Fetch all reviews
        cursor.execute("""
            SELECT Review.ReviewID, Restaurant.RestaurantName, AppUser.UserName, Review.OveralRating 
            FROM Review
            JOIN Visit ON Review.VisitID = Visit.VisitID
            JOIN Restaurant ON Visit.RestaurantID = Restaurant.RestaurantID
            JOIN AppUser ON Visit.UserID = AppUser.UserID
        """)
        reviews = cursor.fetchall()

        if not reviews:
            st.warning("No reviews found.")
            return

        # Display reviews in a dropdown
        review_options = {
            f"Review by {r['UserName']} for {r['RestaurantName']} (Rating: {r['OveralRating']})": r["ReviewID"]
            for r in reviews
        }
        selected_review = st.selectbox("Select a review to delete:", list(review_options.keys()))

        if selected_review:
            review_id = review_options[selected_review]
            if st.button(f"Delete Review"):
                # Permanently delete the review
                cursor.execute("DELETE FROM Review WHERE ReviewID = %s", (review_id,))
                
                conn.commit()
                st.success(f"Review '{selected_review}' has been permanently deleted.")
    except mysql.connector.Error as e:
        st.error(f"An error occurred: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

### 6. MICHELIN STAR RESTAURANTS MENU OPTION
def michelin_star_restaurants():
    """
    Streamlit interface to view Michelin-rated restaurants with Overall Ratings based on criteria.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)

        st.subheader("Michelin Star Restaurants")

        # User choice for filtering Michelin stars
        star_level = st.radio(
            "Filter Michelin Restaurants by star level:",
            ["All Michelin Restaurants", "1-Star", "2-Star", "3-Star"],
            index=0,
            key="michelin_stars_filter"
        )

        # Input for optional country and city filters
        country = st.text_input("Filter by Country (optional):", key="michelin_country_filter").strip()
        city = st.text_input("Filter by City (optional):", key="michelin_city_filter").strip()

        # Base query using the high_rated_restaurants view
        query = """
            SELECT RestaurantName, Country, City, Cuisine, MichelinRating, OverallRating 
            FROM high_rated_restaurants 
            WHERE 1=1
        """
        params = []

        # Add filters based on user selection
        if star_level == "1-Star":
            query += " AND MichelinRating = %s"
            params.append(1)
        elif star_level == "2-Star":
            query += " AND MichelinRating = %s"
            params.append(2)
        elif star_level == "3-Star":
            query += " AND MichelinRating = %s"
            params.append(3)

        if country:
            query += " AND Country = %s"
            params.append(country)
        if city:
            query += " AND City = %s"
            params.append(city)

        # Execute the query with parameters
        cursor.execute(query, params)
        restaurants = cursor.fetchall()

        # Display results
        if restaurants:
            st.write("### Michelin Star Restaurants with Overall Ratings")
            for restaurant in restaurants:
                st.write(
                    f"**Name:** {restaurant['RestaurantName']} | **Country:** {restaurant['Country']} | "
                    f"**City:** {restaurant['City']} | **Cuisine:** {restaurant['Cuisine']} | "
                    f"**Michelin Rating:** {restaurant['MichelinRating']} | "
                    f"**Overall Rating:** {restaurant['OverallRating']:.2f}"
                )

            # Option to export results to a CSV
            if st.button("Export to CSV"):
                df = pd.DataFrame(restaurants)
                export_csv(df, "michelin_star_restaurants_with_ratings.csv")
                st.success("Data exported to 'michelin_star_restaurants_with_ratings.csv'")
        else:
            st.warning("No restaurants found with the selected criteria.")

    except mysql.connector.Error as e:
        st.error(f"An error occurred: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()



### 7. Filter by Overall Rating
def filter_by_overall_rating():
    """
    Streamlit interface to filter restaurants by Overall Rating (1-3) with optional Country, City, and Cuisine filters.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)

        # Explanation of ratings
        st.subheader("Filter Restaurants by Overall Rating")
        st.markdown("""
        **Note**: This database includes only restaurants that are considered above average for most people. 
        Just by being in this list, each restaurant signifies a high level of quality and dining experience.

        **Ratings Explained**:
        - **1** - Very good restaurant (Decent meal): This is an excellent restaurant where you can expect a high-quality meal.
        - **2** - Amazing restaurant (Above average meal): These restaurants go beyond expectations and offer remarkable food and service.
        - **3** - Incredible restaurant (Exceptional): These are outstanding restaurants, offering an exceptional dining experience that is hard to surpass.
        """)

        # Prompt user for overall rating filter
        rating = st.radio("Select Overall Rating to filter by:", [1, 2, 3], key="overall_rating_filter")

        # Optional filters for country, city, and cuisine
        country = st.text_input("Filter by Country (optional):", key="overall_rating_country_filter").strip()
        city = st.text_input("Filter by City (optional):", key="overall_rating_city_filter").strip()
        cuisine = st.text_input("Filter by Cuisine (optional):", key="overall_rating_cuisine_filter").strip()

        # Base query with overall rating filter
        query = """
            SELECT Restaurant.RestaurantName, Restaurant.Country, Restaurant.City, Restaurant.Cuisine, Review.OveralRating 
            FROM Restaurant
            JOIN Visit ON Restaurant.RestaurantID = Visit.RestaurantID
            JOIN Review ON Visit.VisitID = Review.VisitID
            WHERE Review.OveralRating = %s
        """
        params = [rating]

        # Add optional filters
        if country:
            query += " AND Restaurant.Country = %s"
            params.append(country)
        if city:
            query += " AND Restaurant.City = %s"
            params.append(city)
        if cuisine:
            query += " AND Restaurant.Cuisine = %s"
            params.append(cuisine)

        # Execute query
        cursor.execute(query, params)
        restaurants = cursor.fetchall()

        # Display results
        if restaurants:
            st.write(f"### Restaurants with Overall Rating {rating}")
            for restaurant in restaurants:
                st.write(
                    f"**Name:** {restaurant['RestaurantName']} | **Country:** {restaurant['Country']} | "
                    f"**City:** {restaurant['City']} | **Cuisine:** {restaurant['Cuisine']} | "
                    f"**Overall Rating:** {restaurant['OveralRating']}"
                )

            # Option to export results to CSV
            if st.button("Export to CSV", key="export_overall_rating_csv"):
                df = pd.DataFrame(restaurants)
                export_csv(df, f"filtered_restaurants_rating_{rating}.csv")
                st.success(f"Data exported to 'filtered_restaurants_rating_{rating}.csv'")
        else:
            st.warning("No restaurants found with the selected criteria.")

    except mysql.connector.Error as e:
        st.error(f"An error occurred: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


### 8. Average rating by city
def average_rating_by_city():
    """
    Groups restaurants by city and calculates the average overall rating, with Streamlit interface.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)

        # SQL query for aggregation with GROUP BY
        query = """
            SELECT City, AVG(Review.OveralRating) AS AvgRating
            FROM Restaurant
            JOIN Visit ON Restaurant.RestaurantID = Visit.RestaurantID
            JOIN Review ON Visit.VisitID = Review.VisitID
            GROUP BY City
            ORDER BY AvgRating DESC;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        # Display results in Streamlit
        st.subheader("Average Overall Rating by City")
        if results:
            df = pd.DataFrame(results)
            st.write(df)

            # Option to export results to CSV
            if st.button("Export to CSV", key="export_avg_rating_city"):
                export_csv(df, "average_rating_by_city.csv")
                st.success("Data exported to 'average_rating_by_city.csv'")
        else:
            st.warning("No data available to calculate averages.")

    except mysql.connector.Error as e:
        st.error(f"An error occurred: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()



### 9. Restaurants Above City Average
def restaurants_above_city_average():
    """
    Lists restaurants whose average rating is above the city average with Streamlit interface, and allows exporting to a CSV file.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)

        # SQL query for restaurants with above-city-average ratings
        query = """
            SELECT 
                Restaurant.RestaurantName, 
                Restaurant.City, 
                AVG(Review.OveralRating) AS AvgRestaurantRating
            FROM Restaurant
            JOIN Visit ON Restaurant.RestaurantID = Visit.RestaurantID
            JOIN Review ON Visit.VisitID = Review.VisitID
            GROUP BY Restaurant.RestaurantID, Restaurant.City
            HAVING AVG(Review.OveralRating) > (
                SELECT AVG(Rev.OveralRating)
                FROM Restaurant AS R
                JOIN Visit AS V ON R.RestaurantID = V.RestaurantID
                JOIN Review AS Rev ON V.VisitID = Rev.VisitID
                WHERE R.City = Restaurant.City
            );
        """

        cursor.execute(query)
        results = cursor.fetchall()

        st.subheader("Restaurants with Above-City-Average Ratings")
        
        if results:
            # Convert results to DataFrame for display and export
            df = pd.DataFrame(results)
            st.write(df)

            # Option to export results to CSV
            if st.button("Export to CSV", key="export_above_city_avg"):
                export_csv(df, "restaurants_above_city_average.csv")
                st.success("Data exported to 'restaurants_above_city_average.csv'")
        else:
            st.warning("No restaurants found with above-city-average ratings.")

    except mysql.connector.Error as e:
        st.error(f"An error occurred: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
