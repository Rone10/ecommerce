# Django E-Commerce Project

![Landing Page](static/Readme/home.png?raw=true "Optional Title")
![Product Detail](static/Readme/detailView.png?raw=true "Optional Title")
![Product Detail](static/Readme/login.png?raw=true "Optional Title")
![Product Detail](static/Readme/products.png?raw=true "Optional Title")

This is a basic e-commerce project I built using Django. I used Django's templating to serve the frontend. 

## Features

Like most e-commerce websites, you can:
  - as a user:
    1. View items 
    2. Add items to cart
    3. View cart
    4. Remove items from cart
    5. Order itmes
    6. View order history

  - as admin:
    1. Add products
    2. Set product price
    3. Remove products
    4. Grant admin access to staff

## Dependency Packages
 - Django
 - Pillow 
 - whitenoise 
 - gunicorn (for production)

## Install Dependencies
You'll need to have python 3.6+ on your system 

`pipenv install`

## Perform Database Migrations

`python manage.py migrate`

## Create Superuser
Use the command below to create a new user as an admin.

`python manage.py createsuperuser`

## Run Development Server
`python manage.py runserver`

### Production Environment
In production, I'm using docker to containerize the application and gunicorn as the server.
