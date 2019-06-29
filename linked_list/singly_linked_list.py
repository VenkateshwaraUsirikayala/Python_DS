from linked_list.Node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head=None
    
    def append(self,data):
        new_node=Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next = new_node
    
    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next=self.head
        self.head = new_node
        
    def insertAfter(self,previous,data):
        new_node=Node(data)
        new_node.next=previous.next
        previous.next = new_node
    
    def swap_nodes(self,x,y):
        if x==y:
            return
        prevX=None
        currX=self.head
        while currX and currX.data!=x:
            prevX=currX
            currX=currX.next
        
        prevY=None
        currY=self.head
        while currY and currY.data!=y:
            prevY=currY
            currY=currY.next
        
        if prevX:
            prevX.next=currY
        else:
            self.head=currY
        
        if prevY:
            prevY.next=currX
        else:
            self.head=currX
        
        temp=currX.next
        currX.next=currY.next
        currY.next=temp
    
    def print_(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev
    
    def merge(self,anotherlist):
        p=self.head
        q=anotherlist.head
        s=None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s=q
                q=s.next
            new_head=s
        while p and q:
            if p.data<=q.data:
                s.next=p
                s=p
                p=s.next
            else:
                s.next=q
                s=q
                q=s.next
        if not p:
            s.next=q
        if not q:
            s.next=p
        return new_head;
    
    def remove_duplicates(self):
        curr=self.head
        prev=None
        dup_values={}
        while curr:
            if curr.data in dup_values:
                prev.next=curr.next
                curr=None
            else:
                dup_values[curr.data]=1
                prev=curr
                
            curr=prev.next
            
    def length(self):
        curr=self.head
        count=0
        while curr:
            count+=1
            curr=curr.next
        return count
        
            
    def print_nth_from_last(self,n):
#         method - 1
#         total_len=self.length()
#         node_count=total_len-n
#         curr=self.head
#         i=0
#         while i<node_count:
#             curr=curr.next
#             i+=1
#         return curr.data
#         method-2
        p=self.head
        q=self.head
        count =0
        while q and count<n:
            q=q.next
            count+=1
        if not q:
            return 'no node found'
        while p and q:
            p=p.next
            q=q.next
        return p.data
    
    def count(self,n):
        count=0
        curr=self.head
        while curr:
            if curr.data==n:
                count+=1
            curr=curr.next
        return count

        
    def left_rotate(self,k):
        p=self.head
        q=self.head
        count=0
        prev=None
        while p and count<k:
            prev=p
            p=p.next
            q=q.next
            count+=1
        p=prev
        while q:
            prev=q
            q=q.next
        q=prev
        q.next=self.head
        self.head=p.next
        p.next=None
        
    def right_rotate(self,k):
        p=self.head
        q=self.head
        r=self.head
        count=0
        prev=None
        while q.next:
            q=q.next
        while r and count<k:
            prev=r
            r=r.next
            count+=1
        r=prev
        self.head=r.next            
        r.next=None
        q.next=p
        
    def is_palindrome(self):
        s=[]
        p=self.head
        while p:
            s.append(p.data)
            p=p.next
        p=self.head
        while p:
            if p.data!=s.pop():
                return False
            p=p.next
        return True
#     
#     def move_tail_to_head(self):
#         last_node=self.head
#         second_last_node=None
#         while last_node.next:
#             second_last_node=last_node
#             last_node=last_node.next
#         last_node.next=self.head
#         self.head=last_node
#         second_last_node.next=None
    
    def move_tail_to_head_(self):
        curr=self.head
        prev=None
        while curr.next:
            prev=curr
            curr=curr.next
        curr.next=self.head
        self.head=curr
        prev.next=None
        
    def sum_two_lists(self,another_list):
        p=self.head
        q=another_list.head
        carry=0
        sum_llist=SinglyLinkedList()
        while p or q:
            if not p:
                i=0
            else:
                i=p.data
            if not q:
                j=0
            else:
                j=q.data
            sum_=i+j+carry
            if sum_>=10:
                carry=1
                remainder=sum_%10
                sum_llist.append(remainder)
            else:
                carry=0
                sum_llist.append(sum_)
#             if p:
            p=p.next
#             if q:
            q=q.next
            
        sum_llist.print()
            
    def middle(self):
        p=self.head
        q=self.head
        while q and q.next:
            p=p.next
            q=q.next.next
        print(p.data)
    
    def check_loop(self):
        p=self.head
        q=self.head
        while p and q and q.next:
            p=p.next
            q=q.next.next
            if p==q:
                return p
        return False
    
    def start_of_loop(self,p):
        q=self.head
        while p!=q:
            p=p.next
            q=q.next
        print(p.data)
        return p
    
    def intersect(self, other):
        p=self.head
        q=other.head
        r=SinglyLinkedList()
        while p and q:
            if p.data==q.data:
                r.append(p.data)
                p=p.next
                q=q.next
            elif p.data<q.data:
                p=p.next
            else:
                q=q.next
        return r
    
    def intersection_point(self, other):
        len1=self.length()
        len2=other.length()
        count=0
        p=self.head
        q=other.head
        if len1>len2:
            while p and count<abs(len1-len2):
                p=p.next
        if len2>len1:
            while q and count<abs(len1-len2):
                q=q.next
        while p and q and p!=q:
            p=p.next
            q=q.next
        return p.data
    
    def seggregate_odd_even(self):
        curr=self.head
        new_list=SinglyLinkedList()
        prev=None
        while curr:
            if curr.data%2==0:
                new_list.append(curr.data)
                prev.next=curr.next
            prev=curr
            curr=curr.next
        self.append_list(new_list)
    
    def append_list(self,other):
        p=self.head
        q=other.head
        while p.next:
            p=p.next
        p.next=q
        other.head=None
        
llist=SinglyLinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)
llist.append(7)
llist.append(8)

llist.seggregate_odd_even()
llist.print_()

# llist1=SinglyLinkedList()
# llist1.append(2)
# llist1.append(4)
# llist1.append(6)
# llist1.append(8)
# 
# llist.append_list(llist1)
# llist.print_()
# llist.seggregate_odd_even()

# llist1=SinglyLinkedList()

# 
# intersected=llist.intersect(llist1)
# intersected.print_()
# llist.swap_nodes(2, 4)
# llist.print_()



# llist.append(2) 
# llist.append(3) 
# llist.append(1) 
# llist.append(2) 
# llist.append(1)
# llist.head.next.next.next = llist.head 
# llist.start_of_loop(llist.check_loop())