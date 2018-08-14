
#define the function
#argument: 
def calc(x,y,operation):
    
    if operation=="+":
        result=x+y
    elif operation=="-":
        result=x-y
    elif operation=="*":
        result=x*y
    elif operation=="/":
        result=x/y

#     return result #function stops here, similar to 'break'
# #call (to use the function)
# res = calc(4,5,'*')
# print(res)