
# What is a Decorator in Python?
# A decorator in Python is a function that modifies the behavior of another function without changing its actual code. 
# It allows you to add extra functionality to functions dynamically.


# the decorator modefiy the funcation 
# def greet(fx):
#  def mfx():
#     print('good mornig')
#     fx()
#     print('thank you for using thhis funcation')
#     return mfx
# @greet
# def hello():
#     print("hello world")
# # def add(a,b):
#     # print(a+b)
# a=greet(fx)
# print(a.hello())
# print('helloworld')
# def my_decorator(func):
#     def wrapper():
#         print("This happens before the function runs.")
#         func()
#         print("This happens after the function runs.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()
# def my_anomiation(fun):
#     def simple():
#         print('before compilation')
#         fun()
#         print('after the compliation')
#     return simple

# @my_anomiation
# def hello():
#     print('hello world!')
    
# hello
 