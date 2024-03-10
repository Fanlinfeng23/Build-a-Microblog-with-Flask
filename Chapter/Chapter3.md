# Database
## Database in Flask
We will use the most convenient database called SQLAlchemy.

To install Flask-SQLAlchemy in your virtual environment, make sure you have activated it, and then run:
```shell
pip install flask-sqlalchemy
```
## Database Migration
We need to address the problem of making updates to an existing database as the application change or grow.This is hard 
because relational databases are centered around structured data, so whenn the structure changes the data that is already 
in the database needs to be ***migrated*** to the modified structure.

The installation process for Flask-Migrate is similar to other extensions you have seen:
```shell
pip install flask-migrate
```
During development, I'm going to use a SQLite database. SQLite databases are the most convenient choice for developing small applications, sometimes even not so small ones, as each database is stored in a single file on disk and there is no need to run a database server like MySQL and PostgreSQL.
## 1.Add a new configuration item
[code](https://github.com/Fanlinfeng23/Build-a-Microblog-with-Flask/blob/main/Code/Chapter3/config.py)
## 2.chage the __init__.py
[code](https://github.com/Fanlinfeng23/Build-a-Microblog-with-Flask/blob/main/Code/Chapter3/__init__.py)
## 3.write models.py as models
[code](https://github.com/Fanlinfeng23/Build-a-Microblog-with-Flask/blob/main/Code/Chapter3/models.py)
