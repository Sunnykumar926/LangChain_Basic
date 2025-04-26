from pydantic import BaseModel, EmailStr,Field
from typing import Optional

# class Student(BaseModel):

#     name : str 

# new_student = {'name': 8745}

# student = Student(**new_student)
# print(student)

# ================== Default =======================================

class Student(BaseModel):

    name: str='sunny'
    age : Optional[int] = None 
    email:EmailStr
    cgpa : float=Field(gt=0, lt=10, default=5, description='A decimal value represeneting the cgpa of the student')

new_student = {'age': 23}
new_student = {'age': '4785'} # => pydantic is smart enough for type coercing (means when we age as string instead of int it automatically convert that string into int)

new_student = {'age': 32, 'email': 'abc@gmail.com', 'cgpa': 1}
student = Student(**new_student)

student_dict = dict(student)
# print(student_dict['name']) 

student_json = student.model_dump_json()
# print(student_json['name'])