from typing import TypedDict 

class Person(TypedDict):
    name : str
    age : int 

new_person: Person = {'name': "sumiti", 'age': 43}
print(new_person)