# CRUD-app-with-Flask
Create, Read, Update and Delete from student databse

On Windows,

Create database using,

python
from app import db
db.create_all()

Open Postman and go to http://localhst:5000/student

Using POST, add the student details in fields ('id', 'name', 'age', 'address', 'phone', 'gender') in JSON format.
Retrieve using GET --->  http://localhst:5000/student
Update with PUT and --->  http://localhst:5000/student/<id>
Delete with DELETE --->  http://localhst:5000/student/<id>


Go to http://localhst:5000/getstudents to view all the students in a tabular format from the database

Go to http://localhst:5000 to visit the signup page and enroll the student
