### GALLERY
gallery is a photo web application that shows different image category
March 15th, 2019
By Richard Waweru
## Description
Gallery is a website application that shows different image. Users have to see photos and search the images based on the category and also user can copy the link of the images by right clicking on the prefered image.Admin uploads images,delete and update the images, is for the admin that have all right for the images seen by the users as he/she can delete/update and add pictures. 

## Specifications
1. user can view different images and she/he hover the prefered image,it automatically be zoomed,and when he/she click on preferded image it automatically shows the name,description,date_posted,the location of the image with the zoomed images.

2. when user type any category on a search button,it automatically display the image of that category.

3. user can click on copy link button and copy the link of the image.

## Set Up and Installations
* Prerequisites
* Ubuntu Software
* Python3.6
* Postgres
* python virtualenv
* django==1.11
* bootsrap

## Clone the Repo
* Run the following command on the terminal: git clone https://github.com/KAYITARES/gallery.git 
* type cd gallery on terminal

## Activate virtual environment
Activate virtual environment using python3.6 as default handler

virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
## Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

## Create the Database
* psql
* CREATE DATABASE galleryz;
<!-- .env file
Create .env file and paste paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = 'zoom'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
Run initial Migration
python3.6 manage.py makemigrations album
python3.6 manage.py migrate
Run the app
python3.6 manage.py runserver
Open terminal on localhost:8000

Known bugs
Copy functionality does not work

Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- JavaScript
- Heroku
- Postgresql
Support and contact details
Contact me on developer.waweru@gmail.com for any comments, reviews or advice.

License
Copyright (c) Richard Waweru  --> --> --> --> --> --> --> -->