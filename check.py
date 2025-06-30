def check_unique(lst):
    # Your code goes here
    lst1=[]
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if(lst[i]==lst[j]):
                return False
    else:
        return True