def sort(nums):
    n=len(nums)-1
    for i in range(n):
        minpos=i
        for j in range(i,n+1):
            if nums[j]<nums[minpos]:
                minpos=j
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp
        
nums=[56,4,2,58,96,47,23]
sort(nums)
print(nums)