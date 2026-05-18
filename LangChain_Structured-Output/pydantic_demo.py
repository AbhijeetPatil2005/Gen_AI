from pydantic import BaseModel, EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str
    age:Optional[int] = None
    email:EmailStr
    cgpa:float =Field(gt=0 ,lt=10,default=5, description="CGPA must be between 0 and 10")
    

new_student = {"name":"Abhijeet", "email":"abhijeet@example.com", "cgpa":8.5}
student = Student(**new_student)

print(student)

student_dict =dict(student)
print(student_dict)