# Chapter 1
## 1.Create a directory where the project will live
```shell
mkdir microblog
cd micorblog
```
## 2.create and activate a virtual environment
Firstly, you need to run the venv package and let it create a virtual environment called "venv", which the last word writes as the following command line
> You can also change it to another name by replacing the last word

```shell
python3 -m venv venv
```

Now, you have to tell the system you wanna to use it, and you do that by activating it by using the following command:
```shell
source venv/bin/activate
(venv) $)_
```
If you are using a Microsoft Windows command prompt window, the command is diffrent:
```shell
venv\Scripts\activate
```
If you are on windows but are using PowerShell instead of the command prompt, then there is yet another activation command:
```shell
venv\Scripts\Activate.ps1
```
## 3.install Flask
```shell
pip install Flask
```
## 4.Flask Application
Firstly, we need to create a package called app, how can a dir change into a package that can be imported?

The answer is  as followed: If we add a file named __init__.py , and you will get it into a package.

So run the following code:
```shell
mkdir app
```
Then in app, you need to edit the __init__.py file as [this](Code/Chapter1/microblog/app/__init__.py)

As you could see, the last line in the code is:
```python
from app import routes
```
But it's obviously that there's not file called routes.py.

So we create [routes.py](Code/Chapter1/microblog/app/routes.py)
If you are not so clear about why, i suggest you to review my [python flask learning]([README.md](https://github.com/Fanlinfeng23/Python-Flask-learning/blob/main/README.md)https://github.com/Fanlinfeng23/Python-Flask-learning/blob/main/README.md)

Then to complete the app, you need a python script at the top-leval that defines the Flask app instance, so let's create this script called microblog.py, and define it as follows
```python
from app import app
```

## 5.Running it
Before running it, Flask needs to be told how to import it, so you need to run the following command:
```shell
export FLASK_APP=microblog.py
```
> if you are using Microsoft Windows, you need to replace export by set

## The sturcture of the app
[app](Code/Chapter1/microblog)
