def find_max_sum_of_two(arr):
    k=3
    n=len(arr)
    max_sum=window_sum=sum(arr[i] for i in range(k))
    for i in range(n-k):
        window_sum+=arr[i+k]-arr[i]
        max_sum=max(window_sum,max_sum)
#     avg=max_sum/k
#     return avg
    return max_sum
# l=[19,24,17]
l=[1,6,7,3,2,5,8]
print(find_max_sum_of_two(l))
