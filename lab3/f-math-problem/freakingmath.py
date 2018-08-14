from random import choice, randint

def generate_quiz():
    x=randint(1,10)
    y=randint(1,10)
    op_list=["+","-","*","/"]
    operation=choice(op_list)
    error_list=[-1,0,0,0,1]
    error=choice(error_list)
    
    if operation=="+":
        result=x+y+error
    elif operation=="-":
        result=x-y+error
    elif operation=="*":
        result=x*y+error
    elif operation=="/":
        result=x/y+error

    return [x, y, operation, result]

def check_answer(x, y, operation, result, user_choice):
    true_res=calc(x,y,operation)
    if true_res==result:
        if user_choice==True:
            return True
        else:
            return False
    else:
        if user_choice==True:
            return False
        else:
            return True
