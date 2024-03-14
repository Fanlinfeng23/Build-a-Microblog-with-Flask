# User logins
## 1.Password Hashing
In chapter3 the user model was given a password_hash field, and this field is to hold a hash of the user's password. 

In this passage, we will use a easy tool to implement password hashing called Werkzeug.
> This package is inside your Flask module. So when you want to use it, just install it.

The following python session demonstrates how to hash a password with this package.
```python
>>>from werkzeug.security import generate_password_hash
>>>hash = generate_password_hash('Marveric')
>>>hash
输出:
'scrypt:32768:8:1$kV1CXK8BR4yTR62A$2b7f70c78c63ec34ba6854a82256cfce2fd8aa23a7ee158907791a5e8f5d5100b723b15ba9ecfa7fab2a0fef278076a154063d8fa74d4e9d1f85a990c345a247'

```

As we could see, the password 'Marveric' is transformed into a long encoded string. That means when some hackers got
 the password from your database, they may not able to use it to recover the orginal one.

The ***verification*** process is done with a second function from Werkzeug, as follows:
```python
>>>from werkzeug.security import check_password_hash
>>>check_password_hash(hash,'Marveric')
True
>>>check_password_hash(hash,'password')
False
```

The whole password hashing logic can be implemented as two new methods in the user model.
[models.py](https://github.com/Fanlinfeng23/Build-a-Microblog-with-Flask/blob/main/Code/Chapter4/models.py)

Here is a example usage of these new methods:
```python
from app.module import User
u=User(username='susan', email='susan@example.com')
u.set_password('susuanpassword')
u.check_password('susanpassword')
```


## 2.Introduction to Flask Login 
In this chapter, i will going to introduce you a very popular extension called Flask-Login.

By using this extension, the users can login and then navigate to different pages while the application 'remembers'
 the user is logged in. 

To be ready for this chapter, you can start by installing Flask-Login in your virtual environment.
```shell
pip install flask-login
```

As with this extension, Flask-Login needs to be created and initialized right after the application instance in app/__init__.py. 
```python
#...
from flask_login import LoginManager

app=Flask(__name__)
#...
login=LoginManager(app)

#...
``` 
