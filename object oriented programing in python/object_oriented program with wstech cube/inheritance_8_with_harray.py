# class student:
#     def __init__(self,name):
#         self.name=name
#         self.marks={}
#     def add_marks(self,subject,score,grade):
#             if 0<score<=100:
#                 self.marks[subject]=score,grade
#                 return self.marks
#             else:
#                 print("the invalide nos is :")
#     def calculate_average(self):
#         if len(self.marks)==0:
#             return 0
#         else:
#             return sum(self.marks.values())/len(self.marks)
#     def show_info(self):
#         print(f"the value of name{self.name}")
#         for subject,score,grade in self.marks.items(): 
#             print(f"{subject}:{score}:{grade}")
#         print(f"Average Score: {self.calculate_average():.2f}")
        
        
# s=student('ahmad')
# print(s.name)
# s.add_marks('math',97,'A')
# s.add_marks('calculuse',96,'B')
# s.add_marks('data_stucture',89,'C')
# s.show_info()
# s.calculate_average()