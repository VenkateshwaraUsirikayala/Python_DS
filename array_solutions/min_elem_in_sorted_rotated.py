def findMin(arr, low, high): 
    # This condition is needed to handle the case when array is not 
    # rotated at all 
    if high < low: 
        return arr[0] 
  
    # If there is only one element left 
    if high == low: 
        return arr[low] 
  
    # Find mid 
    mid = int((low + high)/2) 
  
    # Check if element (mid+1) is minimum element. Consider 
    # the cases like [3, 4, 5, 1, 2] 
    if mid < high and arr[mid+1] < arr[mid]: 
        return arr[mid+1] 
  
    # Check if mid itself is minimum element 
    if mid > low and arr[mid] < arr[mid - 1]: 
        return arr[mid] 
  
    # Decide whether we need to go to left half or right half 
    if arr[high] > arr[mid]: 
        return findMin(arr, mid+1, high)
    return findMin(arr, low, mid-1) 

l=[5, 6, 1, 2, 3, 4]
n=len(l)
print(findMin(l,0,n-1))