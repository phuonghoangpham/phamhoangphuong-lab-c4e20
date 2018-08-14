x=int(input("x = "))
operation=input("+,-,*,/: ")
y=int(input("y= "))

result=0

if operation=="+":
    result=x+y
elif operation=="-":
    result=x-y
elif operation=="*":
    result=x*y
elif operation=="/":
    result=x/y

#res=eval.calc(x,y,operation)

print("*" *40)
print("{} {} {} = {}".format(x, operation, y, result))
print("*" *40)
    

