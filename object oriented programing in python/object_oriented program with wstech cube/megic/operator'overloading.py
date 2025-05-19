
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # Overloading the `+` operator
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

# # Creating two Point objects
# p1 = Point(2, 3)
# p2 = Point(4, 5)

# # Using the overloaded `+` operator
# p3 = p1 + p2  # Calls p1.__add__(p2)
# print(f"Result: ({p3.x}, {p3.y})")  # Output: (6, 8)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Overloading `==` operator
#     def __eq__(self, other):
#         return self.age == other.age  # Compares ages

# p1 = Person("Alice", 25)
# p2 = Person("Bob", 25)
# p3 = Person("Charlie", 30)

# print(p1 == p2)  # Output: True (Both have age 25)
# print(p1 == p3)  # Output: False (Different ages)


# class Box:
#     def __init__(self, weight):
#         self.weight = weight

#     # Overloading `<` operator
#     def __lt__(self, other):
#         return self.weight < other.weight

# b1 = Box(10)
# b2 = Box(20)

# print(b1 < b2)  # Output: True
# # the user define operators 
# class math:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,other):
#         return math(self.x+other.x, self.y+other.y)
# cl=math(23,44)
# cl1=math(23,44)
# cl2=cl+cl1
# print(f"the value of x {cl2.x} and y {cl2.y}  with respect to the ")