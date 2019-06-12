# CRUD-app-with-Flask
Create, Read, Update and Delete from student databse

On Windows,

Create database using,

python
from app import db
db.create_all()

Open Postman and go to http://localhst:5000/student

Using POST, add the student details in fields ('id', 'name', 'age', 'address', 'phone', 'gender') in JSON format.
Retrieve using GET
Update with PUT and
Delete with DELETE
