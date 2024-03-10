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

