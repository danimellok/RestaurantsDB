import streamlit as st
import pandas as pd
import mysql.connector
from DB_operations_streamline import export_csv, view_all_restaurants, filter_restaurants, fetch_reviews, add_restaurant_visit, create_user, delete_or_update_restaurant, delete_review, michelin_star_restaurants, filter_by_overall_rating, average_rating_by_city, restaurants_above_city_average, home_page




# Main Streamlit App
#Menu V1
def main():
    st.title("Daniel's Restaurant Management System")

    menu = [
        "Home",
        "View All Restaurants and Visits",
        "Filter Restaurants",
        "View Reviews",
        "Add New Restaurant Visit",
        "Delete or Update",
        "Michelin Star Restaurants",
        "Filter by Overall Rating",
        "Average Rating by City",
        "Restaurants Above City Average",
    ]
    choice = st.sidebar.selectbox("Menu", menu)

    

### CHOICE FOR VIEW ALL RESTAURANTS AND VISITS
    if choice == "Home":
        home_page()
    
    elif choice == "View All Restaurants and Visits":
        st.subheader("All Restaurants and Visits")
        view_all_restaurants()

### CHOICE FOR FILTER RESTAURANTS BY CUSTOMIZE FILTERS
    elif choice == "Filter Restaurants":
        st.subheader("Filter Restaurants")
                # Streamlit input fields for filtering
        country = st.text_input("Enter country to filter by (optional):")
        city = st.text_input("Enter city to filter by (optional):")
        cuisine = st.text_input("Enter cuisine to filter by (optional):")
        overall_rating = st.selectbox("Select Overall Rating (1-3):", [None, 1, 2, 3])
        michelin_only = st.checkbox("Show only Michelin-rated restaurants")

        if st.button("Filter"):
            with st.spinner("Fetching data..."):
                try:
                    results = filter_restaurants(
                        country=country,
                        city=city,
                        cuisine=cuisine,
                        overall_rating=overall_rating,
                        michelin_only=michelin_only
                    )
                    if results:
                        df = pd.DataFrame(results)
                        st.dataframe(df)

                        # Export to CSV option
                        csv = df.to_csv(index=False)
                        st.download_button(
                            label="Download CSV",
                            data=csv,
                            file_name="filtered_restaurants.csv",
                            mime="text/csv"
                        )
                    else:
                        st.write("No restaurants match your criteria.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")


### VIEW REVIEWS FUNCTION
    elif choice == "View Reviews":
        st.subheader("View Reviews")
                # Filter options
        filter_choice = st.radio("How would you like to view reviews?", 
                                 ["All", "By Country", "By City", "By Cuisine"], 
                                 key="filter_choice_radio")

        filter_type = None
        filter_value = None

        if filter_choice == "By Country":
            filter_type = "Country"
            filter_value = st.text_input("Enter country to filter by:", key="filter_country")

        elif filter_choice == "By City":
            filter_type = "City"
            filter_value = st.text_input("Enter city to filter by:", key="filter_city")

        elif filter_choice == "By Cuisine":
            filter_type = "Cuisine"
            filter_value = st.text_input("Enter cuisine to filter by:", key="filter_cuisine")

        if st.button("View Reviews", key="view_reviews_button"):
            with st.spinner("Fetching reviews..."):
                try:
                    reviews = fetch_reviews(filter_type=filter_type, filter_value=filter_value)
                    if reviews:
                        # Display reviews in a DataFrame
                        df = pd.DataFrame(reviews)
                        st.dataframe(df)

                        # Export reviews to CSV
                        csv = df.to_csv(index=False)
                        st.download_button(
                            label="Download CSV",
                            data=csv,
                            file_name="reviews_report.csv",
                            mime="text/csv",
                            key="download_reviews_csv"
                        )
                    else:
                        st.write("No reviews match the selected filters.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")


### ADD RESTAURANTS VISIT
    elif choice == "Add New Restaurant Visit":
        st.subheader("Add New Restaurant Visit")
                # User details
        # Username Handling
        username = st.text_input("Enter your username:")
        if username:
            # Check if user exists or create new user
            user_choice = st.radio("Do you have an account?", ["Yes", "No"], key="user_choice_radio")
            if user_choice == "No":
                join_date = st.date_input("Enter join date (YYYY-MM-DD):")
                email = st.text_input("Enter your email:")
                if st.button("Create User", key="create_user_button"):
                    result = create_user(username, join_date, email)
                    st.success(result)

        # Restaurant Details
        restaurant_name = st.text_input("Enter restaurant name:")
        country = st.text_input("Enter country:")
        city = st.text_input("Enter city:")
        cuisine = st.text_input("Enter cuisine:")
        michelin_rating = st.number_input("Enter Michelin rating (or 0 if none):", min_value=0, step=1)
    
        price = st.number_input("Enter average price rating:", min_value=0, step=1)

        # Visit Details
        visit_date = st.date_input("Enter visit date (YYYY-MM-DD):")
        visit_price = st.number_input("Enter visit price:", min_value=0.0, step=0.01)
        reservation = st.selectbox("Reservation made?", ["yes", "no"])

        # Review Details
        overall_rating = st.slider("Enter overall rating (1-3):", 1, 3)
        food_rating = st.slider("Enter food rating (1-5):", 1, 5)
        service_rating = st.slider("Enter service rating (1-5):", 1, 5)

        # Menu Items
        menu_items = []
        if st.checkbox("Add menu items"):
            dish_name = st.text_input("Enter dish name:")
            dish_rating = st.slider("Enter dish rating (1-5):", 1, 5)
            notes = st.text_area("Enter any notes about the dish:")
            if st.button("Add Menu Item", key="add_menu_item_button"):
                menu_items.append({"dish_name": dish_name, "dish_rating": dish_rating, "notes": notes})
                st.success(f"Menu item '{dish_name}' added.")

        # Submit
        if st.button("Submit Visit", key="submit_visit_button"):
            result = add_restaurant_visit(
                username, restaurant_name, country, city, cuisine, michelin_rating, price,
                visit_date, visit_price, reservation, overall_rating, food_rating, service_rating, menu_items
            )
            st.success(result)

## DELETE OR UPDATE RESTAURANTS/REVIEWS
    elif choice == "Delete or Update":
        st.subheader("Delete or Update Options")
        # Ensure radio button is rendered properly
        delete_update_choice = st.radio("Choose an action:", ["Delete/Update Restaurant", "Delete Review"], key="delete_update_choice")

        # Check the value of the radio button and call the appropriate function
        if delete_update_choice == "Delete/Update Restaurant":
            delete_or_update_restaurant()
        elif delete_update_choice == "Delete Review":
            delete_review()

## MICHELIN STAR RESTAURANTS MENU SECTION
    elif choice == "Michelin Star Restaurants":
        michelin_star_restaurants()

    elif choice == "Filter by Overall Rating":
        filter_by_overall_rating()

    elif choice == "Average Rating by City":
        average_rating_by_city()

    elif choice == "Restaurants Above City Average":
        restaurants_above_city_average()
        

if __name__ == "__main__":
    main()
