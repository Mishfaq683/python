# class library:
#     def __init__(self):
#         self.libraries={}
    
#     def add_books(self,item,copies):
#         # self.item=iitem
#         self.libraries[item]=copies
#         self.libraries+=copies
#         return self.libraries
#     def barrow_boook(self,item):
#         self.item=item

#         if item == self.libraries:
#             self.libraries -=item
#             return "the book is find him in the library"
#     def show_fun(self):
#         print("the value is return :{item} ")
        
        
# obj=library()

# print(obj.add_books('python',5))
# print(obj.add_books('python',5))
# print(obj.add_books('java',5))
# print(obj.barrow_boook('python'))
# obj.show_fun()
# class library:
#     def __init__(self):
#         self.libraries={}
#     def add_book(self,item,copies):
#         if item in self.libraries:
#             self.libraries[item] +=copies
#         else:
#              self.libraries[item]=copies
#              return f"the value is return in {self.libraries}"
#     def barrow_book (self,item):
#         if item in self.libraries and self.libraries[item]>0:
#             self.libraries[item]-=item
#             return f"the book {self.item} the current book is  {self.libraries[item]}"
#         else:
#             print(f"the item is not availale for you thanks {item}")
#     def show_fun(self):
#         print("the show funcation of all item in")
#         for book ,copies in self.libraries.items():
#             print(f"the book and copies is avaliiable for {book}:{copies}")
        
        

# ob=library()
# print(ob.add_book('python',5))
# print(ob.add_book('java ',5))
# print(ob.add_book('python',5))
# print(ob.barrow_book('c++'))
# ob.show_fun()


