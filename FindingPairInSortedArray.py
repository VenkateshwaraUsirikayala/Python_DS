def findPair(a,n):
    a=sorted(a)
    i=0
    j=len(a)-1
    while i<j:
        if a[i]+a[j]==n:
            return True
        elif a[i]+a[j]>n:
            j-=1
        elif a[i]+a[j]<n:
            i+=1
    return False
A = [1,4,45,6,10,-8] 
n = 16
print(findPair(A, n))
