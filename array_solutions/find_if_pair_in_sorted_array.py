a=[10,20,35,50,75,80]

def find_pair_(arr, k):
    n=len(arr)
    s=set()
    for i in arr:
        s.add(i)
    for element in arr:
        if element-k in s:
            return True
    return False




def find_pair(arr,k):
    n=len(arr)
    i=0
    j=n-1
    while i<j:
        sum=arr[i]+arr[j]
        if sum==k:
            return True
        elif sum<k:
            i+=1
        elif sum>k:
            j-=1
    return False
print(find_pair_(a, 70))