from Node import Node
from django.db.transaction import non_atomic_requests

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
        new_node=Node()
        new_node.next=previous.next
        previous.next = new_node
        
    def delete_node(self, key):
        curr_node = self.head
        if curr_node and curr_node.data==key:
            self.head=curr_node.next
            curr_node=None
            return
        
        prev_node=None
        while curr_node and curr_node.data!=key:
            prev_node=curr_node
            curr_node=curr_node.next
        if curr_node is None:
            return
        prev_node.next=curr_node.next
        curr_node=None
    
    
    def delete_node_at(self,position):
        curr_node=self.head
        i=0
        prev_node=None
        while i<position and curr_node and curr_node.next!=None:
            prev_node=curr_node
            curr_node=curr_node.next
            i+=1
        if curr_node is None:
            return
        prev_node.next=curr_node.next 
        curr_node=None
            
    def print(self):
        curr_node=self.head
        while curr_node:
            print(curr_node.data)
            curr_node=curr_node.next
    
    def length(self):
        curr_node=self.head
        count=0
        while curr_node:
            count+=1
            curr_node=curr_node.next
        return count
    
    def swap_nodes(self, key1,key2):
        if key1==key2:
            return
        
        prev_1=None
        curr_node_1=self.head
        while curr_node_1 and curr_node_1.data!=key1:
            prev_1=curr_node_1
            curr_node_1=curr_node_1.next
        
        prev_2=None
        curr_node_2=self.head
        while curr_node_2 and curr_node_2.data!=key2:
            prev_2=curr_node_2
            curr_node_2=curr_node_2.next
        
        if not curr_node_1 or not curr_node_2:
            return
        
#         if not prev_1
        
        prev_1.next=curr_node_2.next
        prev_2.next=curr_node_1.next
                

llist=SinglyLinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.prepend(5)
print('======================================')
llist.print()
llist.delete_node(4)
print('======================================')
llist.print()
print('======================================')
llist.delete_node_at(1)
llist.print()
print('======================================')
print(llist.length())