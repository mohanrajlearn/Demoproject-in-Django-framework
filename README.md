Django Installation:

pip install Django 
django-admin startproject projectname
cd projectname
python manage.py startapp appname
python manage.py runserver


MongoDB Installation:

pip install djongo
pip install pymongo==3.12.3

Create database in MongoDB

Add below code in settings.py

DATABASES = {
    'default': {
    'ENGINE': 'djongo',
    'NAME': 'your_databasename',
    'CLIENT': {
        'host': 'localhost',
        'port': 27017,
        # 'username': 'your_username',
        # 'password': 'your_password',
        # 'authSource': 'admin',  # Or your authentication database
    },
}

}

python manage.py makemigrations
python manage.py migrate

one file will be created in database by model.py


