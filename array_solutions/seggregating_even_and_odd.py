arr=[1, 3, 2, 4, 7, 6, 9, 10 ]

def seggregate(arr):
    n=len(arr)
    j=-1
    for i in range(n):
        if arr[i]%2==0:
            j+=1
            arr[i],arr[j]=arr[j],arr[i]
seggregate(arr)
print(arr)