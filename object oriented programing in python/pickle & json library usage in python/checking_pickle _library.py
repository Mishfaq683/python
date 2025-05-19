import pickle
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Alice", 22)

# Save the object
with open("student.pkl", "wb") as o:
    pickle.dump(student, file)
    

# Load the object
# with open("student.pkl", "rb") as file:
    # loaded_student = pickle.load(file)

# print(loaded_student.name, loaded_student.age)
