import logging, sys
logging.basicConfig(filename='log.txt')
logger = logging.getLogger()
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20] 
k = 4

def window_sliding_technique(arr, k):
    max_sum = -sys.maxsize-1
    n = len(arr)
    if n < k:
        logger.error('invalid')
        return -1
    
    window_sum = sum(arr[i] for i in range(k))
    
    for i in range(n - k):
        window_sum = window_sum + arr[i + k] - arr[i] 
        max_sum = max(window_sum, max_sum)
        
    return max_sum
    
print(window_sliding_technique(arr, 3))

