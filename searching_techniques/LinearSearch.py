def linearsearch(arr,n):
    for e in arr:
        if e==n:
            return True;
    return False;

print(linearsearch([4,8,6,5,9], 9))