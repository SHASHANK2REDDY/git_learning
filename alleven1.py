n=int(input("enter number :"))
for i in range(0,n+1):
    if i%2==0:
        print(i,end=" ")
    else:
        continue
print("\n the loop is completed")