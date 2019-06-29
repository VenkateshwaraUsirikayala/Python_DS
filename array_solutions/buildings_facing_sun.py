def no_of_buildings_facing_sun(arr):
    sum=1
    n=len(arr)
    curr_max=arr[0]
    print(curr_max)
    for i in range(1,n):
        if arr[i]>curr_max:
            curr_max=arr[i]
            print(curr_max)
            sum+=1
    return sum

arr=[7, 4, 8, 2, 9]
print(no_of_buildings_facing_sun(arr))