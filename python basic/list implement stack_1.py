l=[]
while True:
    c= int(input('''
    1 push
    2 pop
    3 peek
    4 display
    5 exit
        '''))
    if c == 1:
        n=int(input("enter th value is  :"))
        l.append(n)
        print(l)
        
    elif c == 2:
        if len(l)==0:
            print("empty set is :")
        else:
            l.pop()
            print(l)
            
    elif c == 3:
        print("the value of peek is",l[-1])
    elif c == 4:
        print(l)
    elif c == 5:
        break
    else:
        print("invalid input")        