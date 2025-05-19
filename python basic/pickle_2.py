import pickle
l=[]
while True:
    app_appliction_for_tolier=int(input('''
   1 sign user
   2 register
   3 your profile
   4 logout                         
                                
                '''))
    
    if app_appliction_for_tolier == 1:
        user_name=input('enter the name plz')
        user_emial=input('enter plz emialo or address')
        user_robotic=input('slove the problem 2+3')
        l.append(user_name)
        l.append(user_emial)
        l.append(user_robotic)
        print(l)
    elif app_appliction_for_tolier ==2:
        if len(l)==0:
            print('error plz check your network is ')
        else:
            print(l)
    elif app_appliction_for_tolier == 3:    
        if len(l)==0:
            print('error plz check your network is ')
        else:
            print("your profile has been created",l)
    elif app_appliction_for_tolier==4:
        del(l)
        print("your data is delte the data {l}")
    else:
        break
    
    
    
file_app=open("writedata_app.pkle","wb")
pickle.dump(app_appliction_for_tolier,file_app)
file_app.close()
            

    
        
    