def multiple_rotate(arr, k):
    n=len(arr)
    arr1=[]
    j=0
    for i in range(k,k+n):
        arr1.append(arr[i%n])
    print(arr1)
     
multiple_rotate( [1, 3, 5, 7, 9] , 3)
