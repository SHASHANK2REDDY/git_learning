n=int(input("enter number :"))
skip=int(input("enter skip value:"))
for i in range(0,n):
    if i==skip:
        continue
    else:
        print(i,end=" ")
print("\n the loop is completed")