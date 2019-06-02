from array import array
from numpy import empty
arr = array('i', [ 1, 2, 3, 4, 5, 6, 7 ]) 


def rearrangeArr(arr):
    n=len(arr)
    arr1=empty(n)
    even=int(n/2)
    odd=n-even
    j=odd-1
    for i in range(0,n,2):
        arr1[i]=arr[j]
        j-=1
    j=odd
    for i in range(1,n,2):
        arr1[i]=arr[j]
        j+=1
    
    print(arr1)
    

rearrangeArr(arr) 
