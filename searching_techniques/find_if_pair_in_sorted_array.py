a=[10,20,35,50,75,80]


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
print(find_pair(a, 70))