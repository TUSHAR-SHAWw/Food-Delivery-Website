# Food-Delivery-Website
Welcome to the Food Delivery Website repository! This project is aimed at creating a web platform for food delivery services.
Overview

The Food Delivery Website allows users to:

    Browse through a variety of restaurants
    View restaurant details including address, description, and rating
    Place orders from their favorite restaurants
    Track their orders in real-time
    Provide feedback and ratings for orders

Features

    Restaurant Listings: View a list of restaurants with details like name, address, description, and rating.
    Menu Viewing: Browse through menus offered by each restaurant.
    Order Placement: Place orders for food items from selected restaurants.
    Order Tracking: Track the status of placed orders in real-time.
    User Authentication: Sign up and log in to manage orders and access personalized features.
    Feedback System: Provide feedback and ratings for orders and restaurants.
    Admin Dashboard: Admins can manage restaurants, menus, orders, and user accounts through a dedicated dashboard.

Technologies Used

    Django: Backend framework for building the web application.
    HTML/CSS/JavaScript: Frontend development languages for creating the user interface.
    Bootstrap: Frontend framework for responsive and mobile-first design.
    PostgreSQL: Relational database management system for storing application data.
    Heroku/Vercel: Platforms for deploying and hosting the web application.

Setup Instructions

    Clone the repository: `git clone <repository-url>`
    Install dependencies: `pip install -r requirements.txt`
    Set up the database: `python manage.py migrate`
    Create a superuser (admin): `python manage.py createsuperuser`
    Run the development server: `python manage.py runserver`