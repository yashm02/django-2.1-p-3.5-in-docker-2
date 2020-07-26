# cj-app
Django 2.1 - Python 3.5

IMPORTANT NOTES:

    1. If the backend require any database please use any IN-MEMORY or SQLLite database Unless mentioned in Questions Otherwise .
    3. Make sure you follow the steps mentioned under "PROJECT START STEPS" and ensure that the steps execute successfully. 
    4. Make sure you follow the steps mentioned under "DOCKER START STEPS" and ensure that the steps execute successfully. 

PROJECT START STEPS:

    Pre-requisites:
    1. Install need python and pip to be installed in your system.


    Steps:
    1. To run this application, do the following:
        1.a. Go to the project root directory.
        1.b. Run the following commands to install dependencies of the app:
        	- pip install -r requirements.txt
        1.c. Run the following command(s) in the terminal/command line to run the app:    
            - python manage.py runserver 0.0.0.0:8080
    
    2. Go to http://localhost:8080 in your browser to view it.
    
DATABASE PROPERTIES FOR SUBMISSION:

    Replace your DATABASES section in settings.py to connect to MYSQL database for submission:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': config.get('mysql', 'NAME'),
            'USER': config.get('mysql', 'USER'),
            'PASSWORD': config.get('mysql', 'PASSWORD'),
            'HOST': config.get('mysql', 'HOST'),
            'PORT': config.get('mysql', 'PORT'),
        }
    }
    Or get your mysql database properties in settings.py like:
    database_name = config.get('mysql', 'NAME')
    user_name = config.get('mysql', 'USER')
    user_pass = config.get('mysql', 'PASSWORD')
    database_host = config.get('mysql', 'HOST')
    database_port = config.get('mysql', 'PORT')

    Get your mongodb database properties in settings.py for submission like:
    database_name = config.get('mongodb', 'NAME')
    user_name = config.get('mongodb', 'USER')
    user_pass = config.get('mongodb', 'PASSWORD')
    database_host = config.get('mongodb', 'HOST')
    database_port = config.get('mongodb', 'PORT')