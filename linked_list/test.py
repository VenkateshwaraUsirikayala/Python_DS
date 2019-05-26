from _functools import reduce
l=[0,1,2,3,4,5]
lam = lambda x,y:x+y
print(reduce(lam,l))
