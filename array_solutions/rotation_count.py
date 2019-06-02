def rotation_count(arr):
    min_value = min(arr)
    n=len(arr)
    print('rotation count = ', n-arr.index(min_value))

rotation_count([15, 18, 2, 3, 6, 12])    
    