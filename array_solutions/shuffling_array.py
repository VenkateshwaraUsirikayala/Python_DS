from random import randint
arr = [1, 2, 3, 4, 5, 6, 7, 8] 

def shuffle(arr):
    n=len(arr)
    for i in range(n):
        j=randint(i,n-1)
        arr[i],arr[j]=arr[j],arr[i]

shuffle(arr)
print(arr)