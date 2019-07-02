### Prerequisites

- flask package
- flask-wtf extension for flexible forms, rendering and validation library 
- flask SQLAlchemy ( To use single python code base for different SQL)

Install it using
'''
pip install flask
pip install flask-wtf
pip install flask-sqlalchemy
'''
-----
### Running Queries

**In terminal:**

Change to project directory and enter
> python

**Inside python interpreter :**

- Create an empty database
> from myApp import db

> db.create_all()

- Insert into database
> from myApp import User, Post

> user_1 = User(username='Sisira', email='s@xyz.com', password='password')

> db.session.add(user_1)

> db.session.commit()

- Retrieve all data from a Table Model
> User.query.all()





