str1=input("enter the string :")
str2=str1[::-1]
print(str2)
str3=[]
for i in range(len(str2)-1,-1,-1):
    str3.append(str2[i])
result="".join(str3)
print(result,type(result))
if(result==str1):
    print("palidrom")
else:
    print("not palidrom")