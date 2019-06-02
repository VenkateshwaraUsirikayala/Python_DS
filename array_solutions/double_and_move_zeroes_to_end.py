arr = [0, 2, 2, 2, 0, 6, 6, 0, 0, 8]

def double_element(arr):
    n=len(arr)-1
    for i in range(n):
        if arr[i]==arr[i+1]:
            arr[i]*=2
            arr[i+1]=0
    move_zeroes_to_end(arr)

def move_zeroes_to_end(arr):
    n=len(arr)
    j=-1
    for i in range(n):
        if arr[i]!=0:
            j+=1
            arr[i],arr[j]=arr[j],arr[i]
    
    print(arr)

double_element(arr)
            
