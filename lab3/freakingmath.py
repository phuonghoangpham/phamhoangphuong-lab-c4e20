from random import randint, choice
#from eval import calc
#import eval
playing=True
count=0
while playing:
    x=randint(1,10)
    y=randint(1,10)
    op_list=["+","-","*","/"]
    operation=choice(op_list)
    error_list=[-1,0,0,0,1]
    error=choice(error_list)

    if operation=="+":
        ans=x+y+error
    elif operation=="-":
        ans=x-y+error
    elif operation=="*":
        ans=x*y+error
    elif operation=="/":
        ans=x/y+error

    print("*" *40)
    print("{} {} {} = {}".format(x, operation, y, ans))
    print("*" *40)

    choose=input("Y/N? ").upper()
    if choose=="Y" and error==0:
        print("Yay")
    elif choose=="N" and error==0:
        print("You are wrong")
    elif choose=="Y" and error!=0:
        print("You are wrong")
    elif choose=="N" and error!=0:
        print("Yay")
    count+=1
    if count==3:
        print("Out of turn")
        break

    bit.ly/tk-fmath
        





