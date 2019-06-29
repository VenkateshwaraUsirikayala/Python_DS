l=[-2, -3, 4, -1, -2, 1, 5, -3]

def largest_contigous_sum(arr):
    max_so_far=0
    max_ending_here = 0
    start=0
    end=0
    for i in arr:
        max_ending_here+=i
        if max_ending_here<0:
            max_ending_here=0
            start=i
        if max_ending_here>max_so_far:
            max_so_far=max_ending_here
            end=i
            
    return max_so_far,start,end

print(largest_contigous_sum(l))