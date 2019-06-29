from linked_list.Node import Node
from linked_list.singly_linked_list import SinglyLinkedList

class CircularLinkedList:    
    def __init__(self):
        self.head=None
    
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            new_node.next=new_node
        else:
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next
            curr.next=new_node
            new_node.next=self.head
    
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        if not self.head:
            self.head=new_node
        else:
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next
            curr.next=new_node    
            self.head=new_node
            
    def remove(self, data):
        if self.head.data==data:
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next
            curr.next=self.head.next
            self.head=self.head.next
        else:
            curr=self.head
            prev=None
            while curr.next!=self.head and curr.data!=data:
                prev=curr
                curr=curr.next
            prev.next=curr.next
            curr=None
    
    def remove_node(self, node):
        if self.head==node:
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next
            curr.next=self.head.next
            self.head=self.head.next
        else:
            curr=self.head
            prev=None
            while curr.next!=self.head and curr!=node:
                prev=curr
                curr=curr.next
            prev.next=curr.next
            curr=None
    
    def __len__(self):
        curr=self.head
        count = 0
        while curr:
            count+=1
            curr=curr.next
            if curr==self.head:
                break
        return count
        
    def split_list(self):
        size=len(self)
        count =0
        mid=size//2
        curr=self.head
        prev=None
        while curr and count<mid:
            prev=curr
            curr=curr.next
            count+=1
        prev.next=self.head
        clist_new=CircularLinkedList()
        while curr.next!=self.head:
            clist_new.append(curr.data)
            curr=curr.next
        clist_new.append(curr.data)
        
        self.print()
        print('##################')
        clist_new.print()
        
    def print(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next
            if curr==self.head:
                break
            
    def josephus_circle(self,step):
        curr=self.head
        while len(self)>1:
            count=1
            while count!=step:
                curr=curr.next
                count+=1
            self.remove_node(curr)
            curr=curr.next
    
    def is_circular(self,another_list):
        curr=another_list.head
        while curr and curr.next:
            curr=curr.next
            if curr.next==another_list.head:
                return True
        return False
    

clist=CircularLinkedList()
clist.append(1)
clist.append(2)
clist.append(3)
clist.append(4)

llist=SinglyLinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
print(clist.is_circular(llist))
