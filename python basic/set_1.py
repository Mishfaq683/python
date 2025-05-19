# s={10,20,30,40,50}
# print(type(s))
# s={10,20,30,40,50}

# print(type(s))
# m=list(s)
# print(type(m))
# print(m)
# s={10,20,30,40,50,50,50,60,60}
# print(s)
# s.add(78)
# print(s)
# print(s.pop()) #thats mean that pop is first one is  value deltion not specific is 
# print(s)
# s.remove(78)
# print(s)
# s.discard(0)
# print(s)
# s.clear()
# print(s)
# s={10,20,40,30}
# s.remove(40)
# s.discard(60)

# print(s)
# l=[80,70,45,23,50]
# # s.update(l)
# fruits = {"apple", "banana", "cherry"}
# if 'banana' in fruits:
#     print('the are avialble for your choice is create:')
# if  'orange' not in fruits:
#     print("bachy ghalata shah dy khowakha karr dy")
# number={10,20,30,40}
# if 40 is number:
#     print("your numer is  correct:")
# if 50 is not number:
#     print('your number is incoorect is :') # NOTE    is used for the int value and in for the str value
    

# find the union of the value and intersection of the value 
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set_of_union=set1.union(set2)
# set_of_intersection=set1.intersection(set2)
# print(set_of_union)
# print(set_of_intersection)
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# defference=A.difference(B)
# print(defference)
# symmetric=A.symmetric_difference(B)
# print(symmetric)
# numbers = [1, 2, 2, 3, 4, 4, 5]
# print(numbers)
# n=set(numbers)
# print(n)
# colors = {"red", "green", "blue", "yellow"}
# print(len(colors))
# A = {10, 20, 30}
# B = {30, 40, 50}
# add_up=A.union(B)
# print(add_up)
# add_up.clear()
# print(add_up)
# setX = {1, 2, 3}
# setY = {1, 2, 3, 4, 5}
# sub_set=setX.issubset (setY) 
# print(sub_set)
# sub_set=setY.issubset (setX) 
# print(sub_set)
# super_set=setY.issuperset(setX)
# print(super_set)
# set1 = {1, 2, 3}
# set2 = {3, 2, 1,5}
# comparsion_set=set1==set2
# print(comparsion_set)
# Create a frozen set
frozen_set = frozenset({1, 2, 3})

# Print the frozen set
print("Frozen set:", frozen_set)

# Attempt to add an element to the frozen set
try:
    frozen_set.add(4)  # This will raise an AttributeError
except AttributeError as e:
    print("Error:", e)
    # the forzen is immutable 
