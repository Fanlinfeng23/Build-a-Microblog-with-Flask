# Templates
As i see, just return some of the strings or values can never satisfy us, we need something more powerful like HTML,CSS... But how to add them?

change the route.py file as follows
[Answers](https://github.com/Fanlinfeng23/Build-a-Microblog-with-Flask/blob/main/Code/Chapter2/routes.py)

> I hope you agree with me that it is not a good solution, cause it is somewhat complicated to mix HTML and python together. But the good news is that: ***tempaltes**
> offered us a good way to solve that!

## 1. create directory
In Flask,templates are written as separate files, stored in templates folder that is inside the application package.

Make sure you are in the microblog dirctory, and run the command line:
```shell
mkdir app/templates
```
Then in templates, you could edit your HTML file like [this](https://github.com/Fanlinfeng23/Build-a-Microblog-with-Flask/blob/main/Code/Chapter2/index.html)

Also, you need to change the file routes.py like [this](https://github.com/Fanlinfeng23/Build-a-Microblog-with-Flask/blob/main/Code/Chapter2/routes.py)

Then flask run again and you will get what you want

 ## 2.Loops
 When we login, we will see others posts that were presented a few minutes ago. But the list of post can have any number of elements, it is up to the view function 
 to decide how many posts are going to be presented in the page. For this type of question, Jinja offers a 'for' control structure.

You need to change index.html into the [Example Code](https://github.com/Fanlinfeng23/Build-a-Microblog-with-Flask/blob/main/Code/Chapter2/advanced%20code/index2.html)

And since you have changed index.html, you need also to change routes.py to input some posts.

[Example Code](https://github.com/Fanlinfeng23/Build-a-Microblog-with-Flask/blob/main/Code/Chapter2/advanced%20code/routes.py)

## 3.Template Inheritance
Most web applications these days have a navigation bar at the top of the page with a few frequently used links. I can also easily add a navigation bar using tap <a>.

But I don't want to maintain seval copies on every of my HTML file, the solution is as followed.

Firstly, you need to define a base template called base.html that includes a simple navigation bar and also the title logic I implemented earlier.

You need to write it in templates.[base.html](https://github.com/Fanlinfeng23/Build-a-Microblog-with-Flask/blob/main/Code/Chapter2/Final/base.html)

And you also need to change your index.html, make it much simpler.[index.html](https://github.com/Fanlinfeng23/Build-a-Microblog-with-Flask/blob/main/Code/Chapter2/Final/index3.html)
