def rotate_list(lst, k):
    if not lst:
        return lst
    k=k%len(lst)
    lst=lst[-k:]+lst[:-k]
    return lst