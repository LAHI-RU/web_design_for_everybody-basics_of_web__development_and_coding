from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Data model for a student
class Student(BaseModel):
    id: int
    name: str
    email: str
    grade: float

# Sample student data
students = [
    Student(id=1, name="John Doe", email="john@example.com", grade=3.8),
    Student(id=2, name="Jane Smith", email="jane@example.com", grade=4.0),
    Student(id=3, name="Bob Johnson", email="bob@example.com", grade=3.2)
]

# Get all students
@app.get("/students", response_model=List[Student])
def get_students():
    return students

# Get a single student by ID
@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

# Create a new student
@app.post("/students", response_model=Student, status_code=201)
def create_student(student: Student):
    students.append(student)
    return student

# Update a student
@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: Student):
    for i, s in enumerate(students):
        if s.id == student_id:
            students[i] = student
            return student
    raise HTTPException(status_code=404, detail="Student not found")

# Delete a student
@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int):
    for i, s in enumerate(students):
        if s.id == student_id:
            del students[i]
            return
    raise HTTPException(status_code=404, detail="Student not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)