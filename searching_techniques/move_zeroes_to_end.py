arr=[1, 2, 0, 4, 3, 0, 5, 0]

def move_zeroes_to_end(arr):
    n=len(arr)
    j=-1
    for i in range(0,n):
        if arr[i]!=0:
            j+=1
            arr[i],arr[j]=arr[j],arr[i]

move_zeroes_to_end(arr)
print(arr)