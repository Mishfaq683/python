import random
l=['rock','paper','scissor']
'''
paper vs rock --> win paper
scissor vs rock --> win rock
scissor vs paper --> win scissor
'''
while True:
    uc=int(input('''
  game start......
  1 = yes
  2 = no|exit          
             '''))
    if uc == 1:
       for a in range(1,6):
           user_input=int(input('''
                                
  1 rock
  2 scissor
  3 paper                           
  '''))
           
           if user_input==1:
               u_choice=('rock')
           elif user_input==2:
               u_choice=('paper')
           elif user_input ==3:
               u_choice=('scissor')
               c_choice=random.choice(l)
               print(u_choice)
               print(c_choice)
