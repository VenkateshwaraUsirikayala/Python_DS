def total_water(arr):
    n=len(arr)
    ans=0
    l=0
    r=n-1
    left_max=0
    right_max=0
    while l<r:
        if arr[l]<arr[r]:
            if arr[l]>left_max:
                left_max=arr[l]
            ans+=left_max-arr[l]
            l+=1
        else:
            if arr[r]>right_max:
                right_max=arr[r]
            ans+=right_max-arr[r]
            r-=1
            
    return ans

arr=[3, 0, 5, 2, 0, 4]
print(total_water(arr))