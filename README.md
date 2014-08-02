An project template for creating a web project using Flask, Angular, and SQL Alchemy

Heavily influenced by [Overholt](https://github.com/mattupstate/overholt) with a couple of changes. I moved the models and services into a resources package and moved the api and frontend packages into a package named web. 
Mainly for organizational purposes. Also, using Click instead of Flask-Script because Click will be used in Flask 1.0. Not using Flask-Security and instead using Flask-JWT for authentication and Flask-Bouncer for authorization. 
I'm using postgres, but you can use any database that SQLAlchemy supports

The db commands for interacting with alembic are modified commands from [Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate) updated to work with Click


### Instructions

#### 1. Clone the project:

    $ git clone git@github.com:surgeforward/flask_angular_template.git
    $ cd flask_angular_template

#### 2. Create and initialize virtualenv for the project:

    $ mkvirtualenv flask_angular_template
    $ pip install -r requirements.txt
    
#### 3. Upgrade the database:

    $ python manage.py db upgrade
    
#### 4. Seed the database:

    $ python manage.py db seed
    
#### 5. Run the development server:

    $ python manage.py runserver
    
#### 6. In another console run the Celery app:

    $ celery -A project.tasks worker


#### Management Commands

Management commands can be listed with the following command:

    $ python manage.py

These can sometimes be useful to manipulate data while debugging in the browser.    


#### Database Migrations

To create a database migration, run the following command:

    $ python manage.py db migrate
    
Then run the upgrade command

    $ python manage.py db upgrade


#### Tests

To run the tests use the following command:

    $ nosetests
