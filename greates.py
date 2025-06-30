#find the greatest of three numbers
a=int(input("enter a value:"))
b=int(input("enter b vlaue:"))
c=int(input("enter c value:"))
if(a>b and a>c):
    print("a is greater",a)
elif(b>a and b>c):
    print("b is greater",b)
else:
    print("c is greater",c)
    