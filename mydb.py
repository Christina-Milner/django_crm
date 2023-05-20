# Install Mysql on computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python
# create directory and go in
# python -m venv virt
# source virt/Scripts/activate
# pip install django
#  django-admin startproject <name>
# cd into it
# python manage.py startapp <name>
# Adjust settings.py

import mysql.connector
import config

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = config.root_pw,
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE crm_database")

print("All Done!")

# (Run this file in the terminal) - python mydb.py
# python manage.py migrate
# winpty python manage.py createsuperuser
# python manage.py runserver
# check localhost:8000