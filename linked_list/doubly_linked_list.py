class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None 
        
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new_node
            new_node.prev=curr
    
    def prepend(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            self.head.prev=new_node        
            new_node.next=self.head
            self.head=new_node
    
    def add_after_node(self,key,data):
        curr=self.head
        while curr:
            if not curr.prev and curr.data==key:
                self.append(data) 
                return 
            elif curr.data==key:
                new_node=Node(data)
                nxt=curr.prev
                curr.prev=new_node
                new_node.prev=nxt
                new_node.prev=curr
                nxt.prev=new_node
            curr=curr.prev
                
    def add_before_node(self,key,data):
        curr=self.head
        while curr:
            if not curr.prev and curr.data==key:
                self.prepend(data)
                return
            elif curr.data==key:
                new_node=Node(data)
                prev=curr.prev
                curr.prev=new_node
                new_node.prev=prev
                prev.prev=new_node
                new_node.prev=curr
            curr=curr.prev
        
        
    def delete(self,key):
        curr=self.head
        while curr:
            if curr==self.head and curr.data==key:
#                 case -1 
                if not curr.prev:
                    self.head=None
                    curr=None
                    return
#                 case -2 
                else:
                    nxt=curr.prev
                    curr.prev=None
                    nxt.prev=None
                    self.head=nxt
                    return
            else:
                if curr.data==key:
                    if curr.prev:
                        nxt=curr.prev
                        prv=curr.prev
                        prv.prev=nxt
                        nxt.prev=prv
                        curr.prev=None
                        curr.prev=None
                        curr=None
                        return 
                    else:
                        prv=curr.prev
                        prv.prev=None
                        curr.prev=None
                        curr=None
                        return 
            curr=curr.prev
    
#     def reverse(self):
#         nxt=None
#         curr=self.head
#         while curr:
#             nxt=curr.prev
#             curr.prev=curr.prev
#             curr.prev=nxt
#             curr=curr.prev
#         self.head=nxt.prev

    def reverse(self):
        temp=None
        curr=self.head
        while curr:
            temp=curr.prev
            curr.prev=curr.next
            curr.next=temp
            curr=curr.prev
        self.head=temp.prev
            
    def print(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next
        
def print_list(list):
    temp=list.head
    while temp:
        print(temp.data)
        temp=temp.next
# dllist=DoublyLinkedList()
# dllist.append(1)
# dllist.append(2)
# dllist.append(3)
# dllist.prepend(4)
# dllist.reverse()
# dllist.print()
# dllist.print()
# dllist.reverse_()



