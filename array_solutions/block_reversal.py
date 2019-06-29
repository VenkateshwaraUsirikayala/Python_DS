from array import array
def left_rotate(arr,d):
    n=len(arr)-1
    d=d%n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n)
    reverseArray(arr, 0, n)

def right_rotate(arr,d):
    n=len(arr)-1
    d=d%n
    reverseArray(arr, 0, n - 1); 
    reverseArray(arr, 0, d - 1); 
    reverseArray(arr, d, n - 1); 

def reverseArray(arr, low , high):
    while low<high:
        arr[low],arr[high]=arr[high],arr[low]
        low+=1
        high-=1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
left_rotate(arr, 15)
print(arr)
# right_rotate(arr, 3)
# print(arr)