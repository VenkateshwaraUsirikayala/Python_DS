a = [11, 13, 21, 3]


def is_empty(stack):
    return len(stack) == 0

def createStack(): 
    stack = [] 
    return stack 
  
def isEmpty(stack): 
    return len(stack) == 0
  
def push(stack, x): 
    stack.append(x) 
  
def pop(stack): 
    if isEmpty(stack): 
        print("Error : stack underflow") 
    else: 
        return stack.pop()

def printNGE(arr): 
    s = createStack() 
    element = 0
    next = 0
  
    # push the first element to stack 
    push(s, arr[0]) 
  
    # iterate for rest of the elements 
    for i in range(1, len(arr), 1): 
        next = arr[i] 
  
        if isEmpty(s) == False: 
  
            # if stack is not empty, then pop an element from stack 
            element = pop(s) 
  
            '''If the popped element is smaller than next, then 
                a) print the pair 
                b) keep popping while elements are smaller and 
                   stack is not empty '''
            while element < next : 
                print(str(element)+ " -- " + str(next)) 
                if isEmpty(s) == True : 
                    break
                element = pop(s) 
  
            '''If element is greater than next, then push 
               the element back '''
            if  element > next: 
                push(s, element) 
  
        '''push next to stack so that we can find 
           next greater for it '''
        push(s, next) 
  
    '''After iterating over the loop, the remaining 
       elements in stack do not have the next greater 
       element, so print -1 for them '''
  
    while isEmpty(s) == False: 
            element = pop(s) 
            next = -1
            print(str(element) + " -- " + str(next)) 



def print_next_greater(arr):
    stack = []
    n = len(arr)
    stack.append(arr[0])
    for i in range(1, n):
        next_ = arr[i]
        if not is_empty(stack):
            element = stack.pop()
            while element < next_:
                print(element, '-->', next_)
                if is_empty(stack):
                    break
                element = stack.pop()
            if element > next_:
                stack.append(element)
        stack.append(next_)
       
    while not is_empty(stack):
        element=stack.pop()
        print(element,'-->',-1)
        
def print_gre(arr):
    s=[]
    a.append(arr[0])
    n=len(arr)
    for i in range(n):
        next=arr[i]
        if len(s)!=0:
            element=s.pop()
            while element<next:
                print(element,' --> ',next)
                if len(s)==0:
                    break
                element=s.pop()
            if element>next:
                s.append(element)
        s.append(next)
    
# printNGE(a)
print_next_greater(a)
