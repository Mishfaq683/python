# import time
# def using_while():
#     i=0
#     while i<5000:
#         i=i+1
#         print(i)
# def using_for():
#     for i in range(5000):
#         i=i+1
#         print(i)
        
        
# init=time.time()
# using_while()
# t1=time.time()
# print("the value of the while loop",t1-init)
# init=time.time()
# using_for()
# t2=time.time()
# print("the value of for loop",t2-init)


import time

def using_while():
    i = 0
    while i < 5000:
        i += 1
        print(i)

def using_for():
    for i in range(5000):  # Fixing the for loop
        print(i + 1)  # To match the output of while loop

# Measuring time for using_while()
init = time.time()
using_while()
t1 = time.time()

print("Time taken by while loop:", t1 - init)

# Measuring time for using_for()
init = time.time()
using_for()
t2 = time.time()

print("Time taken by for loop:", t2 - init)
