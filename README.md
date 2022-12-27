# Softdesk

## Description

Softdesk is an API built in Django Rest framework. This works on website and mobile (ios & android).  

***
## Setup

Create a virtualenv for the project with Python 3.10.4  
And install the depencies.
    
```
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt 
```

## Run the server  

Server can be run by this command :
```
python manage.py runserver
```    
and open in browser this adress: [http:/127.0.0.1:8000/]()

***
## Postman documentation
Here the documentation of the Softdesk's API: [postman documentation](https://documenter.getpostman.com/view/23129255/2s8Z6u3ZVi)

***
## Pylint report
The file .pylintrc contents parameters for checking Pylint.  
It checks syntax, error, coding stadard of the code with this command:  
From the terminal into the root folder 'Softdesk'
```
pylint softdesk
```

## What I learned with this project is
I learn how to create an API with Django Rest Framework. 
How to protect with authenticated and peermission some action of the CRUD. 
I learn to use view class and a nested router url.   

 
