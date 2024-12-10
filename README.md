CPSC 408 - Final Project
Daniel Mello

*references in the bottom of the README
*For security reasons, the user and password for the connection to MySQL is removed. The user will have to provide its own.
*Github link: https://github.com/danimellok/RestaurantsDB

# Restaurant Management System

## Overview
This program manages a database of restaurants, reviews, and visits. It features an interactive Streamlit-based user interface and MySQL-backed database for storing and querying data. Users can view, filter, update, and analyze restaurant data with ease.

---

## Setup Instructions

### 1. Database Setup
To ensure the database is correctly configured, you have two options:

#### Option 1: Use the Provided MySQL Dump
If you already have the MySQL `.sql` file:
1. Open your terminal or command prompt.
2. Navigate to the directory containing the `.sql` file.
3. Run the following command to import the database:
   ```
   mysql -u root -p RestaurantsDB < /path/to/RestaurantsDB_dump.sql
   ```
   Replace `/path/to/RestaurantsDB_dump.sql` with the actual path to the `.sql` file.

#### Option 2: Populate the Database Manually
If the MySQL database is not set up, follow these steps:
1. Ensure you have the `RestaurantDB_Excel.xlsx` file in the same directory as `populateMySQL.py`.
2. Run the `populateMySQL.py` script:
   ```
   python3 populateMySQL.py
   ```
3. This will create and populate the database with the initial data from the Excel file.

---

### 2. Code Structure
This project is divided into two main Python scripts:
- **`DB_operations_streamline.py`**: Contains all the menu functions and database queries.
- **`app_streamline.py`**: Holds the Streamlit interface and menu structure for user interaction.

---

### 3. Running the Application
To launch the Streamlit interface:
1. Open your terminal or command prompt.
2. Navigate to the directory containing `app_streamline.py`.
3. Run the following command:
   ```
   streamlit run app_streamline.py
   ```
4. This will open the Streamlit application in your default web browser.

---

## Features
The application provides the following features:
1. **View All Restaurants and Visits**: Displays a list of all restaurants and visits in the database.
2. **Filter Restaurants**: Allows filtering based on country, city, cuisine, or ratings.
3. **View Reviews**: Displays detailed reviews with filter options.
4. **Add New Restaurant Visit**: Adds a new restaurant, visit, and review to the database.
5. **Delete or Update**: Allows deletion or updates of restaurant data.
6. **Michelin Star Restaurants**: Filters and displays Michelin-rated restaurants.
7. **Filter by Overall Rating**: Filters restaurants based on their overall rating.
8. **Average Rating by City**: Shows average ratings grouped by city.
9. **Restaurants Above City Average**: Displays restaurants with ratings above the city average.

---

## Additional Notes
- **MySQL Configuration**: Ensure your MySQL server is running and configured to allow connections.
- **Environment Setup**: Install the necessary dependencies using:
  ```
  pip install -r requirements.txt
  ```
  Ensure `mysql-connector-python` and `streamlit` are included in your environment.

---

## Troubleshooting
- If you encounter errors while connecting to MySQL, ensure that your `DATABASE_CONFIG` in `DB_operations_streamline.py` is correctly set up with your MySQL credentials.
- Verify that the `RestaurantDB_Excel.xlsx` file is correctly formatted if you’re populating the database manually.

---

Enjoy exploring the Restaurant Management System! If you have any questions or issues, feel free to reach out.


*** REFERENCES ***
This was a big project, and I have used LLMs to help in most parts of the project. Setting up the MySQL and setting up functions. I mostly used after I was done with the project, and then decided to implement the streamlit interface, which means that I had to change my whole code. LLMs helped me a lot with that, and ensuring I was able to run Streamlit smoothly. I also used to help me creating the queries and functions of the program.
