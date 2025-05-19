# # the create a simple funcation that 
# # def sum(a,b):
# #     c=a+b
# #     return c
# # print(sum(10,20))
# class student:
#     def __init__(self ,name):
#         self.name=name
#         self.marks={}
#     def add_marks(self,subject,score,grade):
#         if 0 < score <=100:
#             self.marks[subject]=score,grade
#             return self.marks
#         else:
#             print("the zero nos is not show ")
#     def calculate_average(self):
#         if len(self.marks)==0:
#             return 0
#         else:
#             return sum(self.marks.values())/len(self.marks)
        
#     def show_info(self):
        
#         print(f"show name:{self.name}")
#         for subject,score, in self.marks.items():
#             print(f"{subject}:{score}")
#         print(f"Average Score: {self.calculate_average():.2f}")
    
# s=student('ishfaq')
# s.add_marks('maths',97,'A')
# s.add_marks('CS',78,'D')
# s.add_marks('CSLCULAS',87,'B')
# s.show_info()