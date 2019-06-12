from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

'''
@app.route('/',methods=['GET'])
def get():
    return jsonify({'msg':'hello world'})
'''

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#Init db
db = SQLAlchemy(app)
#Init ma
ma = Marshmallow(app)

# Student Class/Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    age = db.Column(db.Integer)
    address = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    gender = db.Column(db.String(6))

    def __init__(self, name, age, address, phone, gender):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.gender = gender

# Product Schema
class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'age', 'address', 'phone', 'gender')

# Init schema
student_schema = StudentSchema(strict=True)
students_schema = StudentSchema(many=True, strict=True)

# Create a Student
@app.route('/student', methods=['POST'])
def add_student():
    name = request.json['name']
    age = request.json['age']
    address = request.json['address']
    phone = request.json['phone']
    gender = request.json['gender']

    new_student = Student(name, age, address, phone, gender)

    db.session.add(new_student)
    db.session.commit()

    return student_schema.jsonify(new_student)

# Get All Students
@app.route('/student', methods=['GET'])
def get_students():
    all_students = Student.query.all()
    result = students_schema.dump(all_students)
    return jsonify(result.data)

# Update a Student
@app.route('/student/<id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)
    name = request.json['name']
    age = request.json['age']
    address = request.json['address']
    phone = request.json['phone']
    gender = request.json['gender']

    student.name = name
    student.age = age
    student.address = address
    student.phone = phone
    student.gender = gender

    db.session.commit()

    return student_schema.jsonify(student)

# Delete Student
@app.route('/student/<id>', methods=['DELETE'])
def delete_student(id):
  student = Student.query.get(id)
  db.session.delete(student)
  db.session.commit()

  return student_schema.jsonify(student)


#Run Server
if __name__ == '__main__':
    app.run(debug=True)
