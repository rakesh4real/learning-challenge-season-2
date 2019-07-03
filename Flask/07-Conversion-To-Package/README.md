## Conversion to Package

**Fact:** 

>Whenever Python imports something from a module, it runs the entire module; 
Not just the imported section(class) of the module!

This creates many problems when we try to import from modules as we will be needing import statements in 
a particular order. We can simply convert it into package to avoid problems.

Using package we make all of these imports more simple and allow us to separate things 
out in a better way which has been done till now(using modules).

**Note:** _We might have fixed problems with messy imports but we have to take care of circular imports. For example in routes.py module we are importing 'app' variable. We can't import the routes i.e '@app..' at the top of the file or else we will get into circular imports

- ```__init__.py``` file tells python that this is a package and also initializes and ties together everything that we need for our app.
- ```routes.py``` file contains all the logic for routes

---

## How to run 

In terminal enter
```
python run.py
```





