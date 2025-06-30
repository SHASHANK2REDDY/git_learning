list1=[int(i) for i in input("enter list of num").split(",")]
temp=0
print(list1)
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if(list1[i]>list1[j]):
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp
print(list1)