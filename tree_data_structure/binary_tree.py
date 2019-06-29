from queue import Queue
from sys import maxsize
from linked_list.doubly_linked_list import print_list

class Queue:

    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return False
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].data
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __len__(self):
        return len(self.items)


class Stack:

    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(object)
    
    def len(self):
        return len(self.items)
        
    def is_empty(self):
        return True if len(self.items) == 0 else False
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()


class Dist_Node:

    def __init__(self, node, distance):
        self.node = node
        self.distance = distance


class  Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.data)

        
class BinaryTree:

    def __init__(self, root):
        self.root = Node(root)
    
    def pre_order_traversal(self, root):
        if root:
            print(root.data)
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(root.data)
            self.in_order_traversal(root.right)
            
    def post_order_traversal(self, root):
        if root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.data)
    
    def max(self,root):
        if not root:
            return 0
        if root.left==None and root.right==None:
            return root.data
        l=self.max(root.left)
        r=self.max(root.right)
        return max(root.data, max(l,r))
    
    def min(self,root):
        if not root:
            return maxsize
        if root.left==None and root.right==None:
            return root.data
        l=self.min(root.left)
        r=self.min(root.right)
        return min(root.data, min(l,r))
    
    def get_level(self, data):
        return self.get_level_(self.root, data, 1)
    
    def get_level_(self, node, data, level):
        if not node:
            return 0
        if node.data == data:
            return level
        downlevel = self.get_level_(node.left, data, level + 1)
        if downlevel != 0:
            return downlevel
        downlevel = self.get_level_(node.right, data, level + 1)
        return downlevel
    
    def nodes_at_given_level(self, level):
        if not self.root:
            return
        return 
    
    def nodes_at_given_level_(self, node, level):
        if level == 0:
            print(self.root.data)
        else:
            self.nodes_at_given_level_(node.left, level - 1)
            self.nodes_at_given_level_(node.right, level - 1)
        
    def in_order_traversal_iterative(self, root):
        curr_node = root
        stack = []
        while True:
            if curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            elif stack:
                curr_node = stack.pop() 
                print(curr_node.data)
                curr_node = curr_node.right
            else:
                break
    
    def pre_order_traversal_iterative(self, root):
        curr_node = root
        stack = []
        while True:
            if curr_node:
                print(curr_node.data)
                stack.append(curr_node)
                curr_node = curr_node.left
            elif stack:
                curr_node = stack.pop()
                curr_node = curr_node.right
            else:
                break
            
    def post_order_traversal_iterative(self, root):
        curr_node = root
        stack1 = []
        stack2 = []
        while True:
            if curr_node:
                stack2.append(curr_node.data)
                stack1.append(curr_node)
                curr_node = curr_node.right
            elif stack1:
                curr_node = stack1.pop()
                curr_node = curr_node.left
            else:
                break
        while stack2:
            print(stack2.pop())
        
    def reverse_pre_order_traversal_iterative(self, root):
        curr_node = root
        stack = []
        while True:
            if curr_node:
                print(curr_node.data)
                stack.append(curr_node)
                curr_node = curr_node.right
            elif stack:
                curr_node = stack.pop()
                curr_node = curr_node.left
            else:
                break
     
    def level_order_traversal(self, root):
        if root:
            queue = Queue()
            queue.enqueue(root)
            traversal = ""
            while len(queue) > 0:
                traversal += str(queue.peek()) + "-"
                node = queue.dequeue()
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            return traversal
                
    def reverseLevelOrder(self, root): 
        if root:
            another_queue = Queue() 
            queue = Queue() 
            queue.enqueue(root) 
          
            while(len(queue) > 0): 
          
                root = queue.dequeue() 
                another_queue.append(root) 
          
                if (root.right): 
                    queue.append(root.right) 
          
                if (root.left): 
                    queue.append(root.left) 
          
            while(len(another_queue) > 0): 
                root = another_queue.pop() 
                print(root.data),
    
    def left_view(self, root):
        if root:
            queue = []
            queue.append(root)
            while queue:
                count = len(queue)
                queueCount = len(queue)
                while count > 0:
                    element = queue.pop()
                    if count == queueCount:
                        print(element.data)
                    if element.left:
                        queue.insert(0, element.left)
                    if element.right:
                        queue.insert(0, element.right)
                    count -= 1
    
    def right_view(self, root):
        if root:
            queue = []
            queue.append(root)
            while queue:
                count = len(queue)
                while count > 0:
                    element = queue.pop()
                    if count == 1:
                        print(element.data)
                    if element.left:
                        queue.insert(0, element.left)
                    if element.right:
                        queue.insert(0, element.right)
                    count -= 1
    
    def bottom_view(self, root):
        if root:
            queue = []    
            distMap = {}
            queue.insert(0, Dist_Node(root, 0))
            while queue:
                element = queue.pop()
                distMap[element.distance] = element.node.data
                if element.node.left:
                    queue.insert(0, Dist_Node(element.node.left, element.distance - 1))
                if element.node.right:
                    queue.insert(0, Dist_Node(element.node.right, element.distance + 1))
            for index in sorted(distMap):
                print(distMap[index])
    
    def top_view(self, root):
        if root:
            queue = []
            distMap = {}
            queue.append(Dist_Node(root, 0))
            while queue:
                element = queue.pop()
                if not element.distance in distMap:
                    distMap[element.distance] = element.node.data
                if element.node.left:
                    queue.append(Dist_Node(element.node.left, element.distance - 1))
                if element.node.right:
                    queue.append(Dist_Node(element.node.right, element.distance + 1))
            
            for index in sorted(distMap):
                print(distMap[index])
    
    def vertical_order_traversal(self, root):
        if root:
            distMap = {}
            queue = []
            queue.append(Dist_Node(root, 0))
            while queue:
                dist_node = queue.pop()
                if dist_node.distance in distMap:
                    distMap[dist_node.distance].append(dist_node.node)
                else:
                    distMap[dist_node.distance] = [dist_node.node]
                if dist_node.node.left:
                    queue.append(Dist_Node(dist_node.node.left, dist_node.distance - 1))
                if dist_node.node.right:
                    queue.append(Dist_Node(dist_node.node.right, dist_node.distance + 1))
            
            for key in sorted(distMap):
                val = distMap[key]
                for value in val:
                    print(value)
                print()
#             for key,value in sorted(distMap).items():
#                 for i in value:
#                     print(i)
#                 print()

    def right_diagonal_traversal(self, root):    
        if root:
            queue = []
            map = {}
            queue.insert(0, Dist_Node(root, 0))
            while queue:
                element = queue.pop()
                if element.distance in map:
                    map[element.distance].append(element.node.data)
                else:
                    map[element.distance] = [element.node.data]
                if element.node.left:
                    queue.insert(0, Dist_Node(element.node.left, element.distance + 1))
                if element.node.right:
                    queue.insert(0, Dist_Node(element.node.right, element.distance))
            for index in sorted(map):
                print(map[index])
            
    def left_diagonal_traversal(self, root):
        if root:
            queue = []
            map = {}
            queue.insert(0, Dist_Node(root, 0))
            while queue:
                element = queue.pop()
                if element.distance in map:
                    map[element.distance].append(element.node.data)
                else:
                    map[element.distance] = [element.node.data]
                if element.node.left:
                    queue.insert(0, Dist_Node(element.node.left, element.distance))
                if element.node.right:
                    queue.insert(0, Dist_Node(element.node.right, element.distance + 1))
            for index in sorted(map):
                print(map[index])
            
    def height(self, root):
        if root is None:
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height, right_height)
            
    def height_(self, root):
        if not root:
            return 0
        return max(self.height_(root.left), self.height_(root.right)) + 1
    
    def size_recursive(self, root):
        if root is None:
            return 0
        left_size = self.size_recursive(root.left)
        right_size = self.size_recursive(root.right)
        return 1 + left_size + right_size
        
    def size_iterative(self):
        if self.root is None:
            return 0
        queue = Queue()
        queue.enqueue(self.root)
        size = 0
        while len(queue) > 0:
            node = queue.dequeue()
            size += 1
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return size
    
    def number_of_leaf_nodes(self, root):
        if root:
            count = 0
            queue = []
            queue.insert(0, root)
            while queue:
                element = queue.pop()
                if not element.left and not element.right:
                    count += 1
                if element.left:
                    queue.insert(0, element.left)
                if element.right:
                    queue.insert(0, element.right)
            return count
    
    def print_leaf_nodes(self, root):
        if root:
            queue = []
            queue.insert(0, root)
            while queue:
                element = queue.pop()
                if element.left == None and element.right == None:
                    print(element.data)
                if element.left:
                    queue.insert(0, element.left)
                if element.right:
                    queue.insert(0, element.right)
                    
    def print_left_except_leaf(self, root):
        if not root:
            return
        if root.left == None and root.right == None:
            return
        print(root.data)
        self.print_left_except_leaf(root.left)
        
    def print_right_except_leaf_reverse(self, root):
        if not root:
            return
        if root.left == None and root.right == None:
            return
        self.print_right_except_leaf_reverse(root.right)
        print(root.data)
        
    def sum_of_all_nodes_in_tree(self, root):
        if root:
            queue = []
            queue.insert(0, root)
            sum = 0
            while queue:
                element = queue.pop()
                sum += element.data
                if element.left:
                    queue.insert(0, element.left)
                if element.right:
                    queue.insert(0, element.right)
            return sum
            
    def sprial_order_traversal(self, root):   
        if not root:
            return
        s1 = []
        s2 = []
        s1.append(root)
        while s1 or s2:
            while s1:
                elem = s1.pop()
                print(elem.data)
                if elem.left:
                    s2.append(elem.left)
                if elem.right:
                    s2.append(elem.right)
            
            while s2:
                elem = s2.pop()
                print(elem.data)
                if elem.right:
                    s1.append(elem.right)
                if elem.left:
                    s1.append(elem.left)
                    
    def boundary_traversal(self, root):
        self.print_left_except_leaf(root)
        self.print_leaf_nodes_(root)
        self.print_right_except_leaf_reverse(root.right)
    
    def print_leaf_nodes_(self, root):
        if not root:
            return
        if root.left == None and root.right == None:
            print(root.data)
            return
        self.print_leaf_nodes_(root.left)
        self.print_leaf_nodes_(root.right)
                    
    def mirror(self, root):
        if not root:
            return
        self.mirror(root.left)
        self.mirror(root.right)
        root.left, root.right = root.right, root.left
        
    def root_to_leaf_with_given_sum(self, root, sum , list):
        if not root:
            return
        if root.left == None and root.right == None:
            if root.data == sum:
                list.append(root.data)
                return True
            else:
                return False
        if self.root_to_leaf_with_given_sum(root.left, sum - root.data, list):
            list.append(root.data)
            return True, list
        if self.root_to_leaf_with_given_sum(root.right, sum - root.data, list):
            list.append(root.data)
            return True, list
        return False
    
    def print_all_paths_from_root_to_leaf(self, root, list):
        if not root:
            return
        list.append(root)
        self.print_all_paths_from_root_to_leaf(root.left, list)
        for element in list:
            print(element.data)
        print("==============")
        self.print_all_paths_from_root_to_leaf(root.right, list)
        list.pop()
        
    def is_identical(self, root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and root2:
            if root1.data == root2.data and self.is_identical(root1.left, root2.left) and self.is_identical(root1.right, root2.right):
                return True
        return False
    
    def is_mirror(self, root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and root2:
            if root1.data == root2.data and self.is_mirror(root1.left, root2.right) and self.is_mirror(root1.right, root2.left):
                return True
        return False
    
    def to_doubly_linked_list(self,root):
        if not root:
            return
        queue=[]
        queue.insert(0, root)
        head=prev=None
        while queue:
            element=queue.pop()
            
            curr=Node(element)
            if not prev:
                head=curr
            else:
                curr.left=prev
                prev.right=curr
            prev=curr
            
            if element.left:
                queue.insert(0, element.left)
            if element.right:
                queue.insert(0, element.right)
        
        return head
    def max_sum(self, root):
        if not root:
            return 0
#         if root.left==None and root.right==None:
#             return root.data
        l = self.max_sum(root.left)
        r = self.max_sum(root.right)
        return max(l, r) + root.data
    
    def isMirror(self, root1 , root2): 
        # If both trees are empty, then they are mirror images 
        if root1 is None and root2 is None: 
            return True 
          
        """ For two trees to be mirror images, the following three 
            conditions must be true 
            1 - Their root node's key must be same 
            2 - left subtree of left tree and right subtree 
              of the right tree have to be mirror images 
            3 - right subtree of left tree and left subtree 
               of right tree have to be mirror images 
        """
        if (root1 is not None and root2 is not None): 
                if  root1.data == root2.data: 
                    return (self.isMirror(root1.left, root2.right)and
                    self.isMirror(root1.right, root2.left)) 
        return False


    def is_symmetric(self,root):
        if not root:
            return True
        return self.isMirror(root,root)
    
    def search(self, root, value):
        if not root:
            return False
        if root.data==value:
            return True
        if self.search(root.left, value):
            return True
        if self.search(root.right, value):
            return True
        return False
    
    def delete_all_nodes(self,root):
        if not root:
            return
        self.delete_all_nodes(root.left)
        self.delete_all_nodes(root.right)
        root=None
    
   


class BinarySearchTree:

    def __init__(self):
        self.root = None
    
    def insert (self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_(data, self.root)
    
    def insert_(self, data, curr_node):
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self.insert_(data, curr_node.left)
        
        elif data > curr_node.data:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self.insert_(data, curr_node.right)
        else:
            print('data already exist in the tree')
    
    def find(self, data):
        if self.root:
            found = self.find_(data, self.root)
            return True if found else False
    
    def find_(self, data, curr_node):
        if curr_node.data == data:
            return True
        if data < curr_node.data and curr_node.left:
            return self.find_(data, curr_node.left)
        if data > curr_node.data and curr_node.right:
            return self.find_(data, curr_node.right)
    
    def inorder_traversal(self, root, list_):
        if root:
            self.inorder_traversal(root.left, list_)
            list_.append(root.data)
            self.inorder_traversal(root.right, list_)
        return list_
    
    def inorder_predecessor(self, root, main_root, key):
        if not root:
            return
        if root.data==key:
            if root.left:
                temp=root.left
                while temp.right!=None:
                    temp=temp.right
                print(temp.data)
            else:
                store=main_root
                while root.data!=main_root.data:
                    if root.data>main_root.data:
                        store=main_root
                        main_root=main_root.right
                    else:
                        main_root=main_root.left
                print(store.data)
                        
        elif key<root.data:
            self.inorder_predecessor(root.left, main_root, key)
        else:
            self.inorder_predecessor(root.right, main_root, key)
    
    def inorder_successor(self, root, main_root, key):
        if not root:
            return
        if root.data==key:
            if root.right:
                temp=root.right
                while temp.left!=None:
                    temp=temp.left
                print(temp.data)
            else:
                store=main_root
                while root.data!=main_root.data:
                    if root.data<main_root.data:
                        store=main_root
                        main_root=main_root.left
                    else:
                        main_root=main_root.right
                print(store.data)
        elif key<root.data:
            self.inorder_successor(root.left, main_root, key)
        else:
            self.inorder_successor(root.right, main_root, key)
    

# bst=BinarySearchTree()
# bst.insert(4)
# bst.insert(2)
# bst.insert(5)
# bst.insert(8)
# bst.insert(10)
# bst.inorder_predecessor(bst.root, 4)
# bst.inorder_predecessor(bst.root,bst.root,10)
# bst.inorder_successor(bst.root, bst.root, 2)
# print(bst.find(11))
# print(bst.inorder_traversal(bst.root, []))
tree=BinaryTree(1)
tree.root.left = Node(2) 
tree.root.right = Node(3) 
tree.root.left.left = Node(4) 
tree.root.left.right = Node(5) 
tree.root.right.left = Node(6) 
# tree.root.right.left.right = Node(8) 
tree.root.right.right = Node(7) 
tree.post_order_traversal(tree.root)
tree.delete_all_nodes(tree.root)
print("=====================")
tree.post_order_traversal(tree.root)

# linkedlist=tree.to_doubly_linked_list(tree.root)
# print_list(linkedlist)
# print(tree.max(tree.root))
# print(tree.min(tree.root))


# tree=BinaryTree(1)
# tree.root.left=Node(2)
# tree.root.right=Node(3)
# tree.root.left.right=Node(4)
# print(tree.min(tree.root))
# print(tree.findMax(tree.root))
# print(tree.search(tree.root, 2))

# tree = BinaryTree(1)
# tree.left = Node(2)
# tree.right = Node(2)
# tree.left.left = Node(3)
# tree.left.right = Node(4)
# tree.right.left = Node(4)
# tree.right.right = Node(5)
# print(tree.is_symmetric(tree.root))

# 
# tree1=BinaryTree(1)
# tree1.root.left = Node(2) 
# tree1.root.right = Node(3) 
# tree1.root.left.left = Node(4) 
# tree1.root.left.right = Node(5) 
# tree1.root.right.left = Node(6) 
# tree1.root.right.left.right = Node(8) 
# tree1.root.right.right = Node(7) 

# print(tree.max_sum(tree.root))
# tree.print_all_paths_from_root_to_leaf(tree.root, [])
# print(tree.is_identical(tree.root, tree1.root))

# tree=BinaryTree(10)
# tree.root.left = Node(-2) 
# tree.root.right = Node(7) 
# tree.root.left.left = Node(8) 
# tree.root.left.right = Node(-4) 
# print(tree.max_sum(tree.root))

# print(tree.root_to_leaf_with_given_sum(tree.root, 18, []))
# print(tree.sum_of_all_nodes_in_tree(tree.root))
# tree.in_order_traversal(tree.root)
# tree.mirror(tree.root)
# print("===================")
# tree.sprial_order_traversal(tree.root)
# tree.in_order_traversal(tree.root)

# tree.boundary_traversal(tree.root)
# tree.print_right_except_leaf_reverse(tree.root)
# tree.right_diagonal_traversal(tree.root)
# print("===================")
# tree.left_diagonal_traversal(tree.root)
# print(tree.size_iterative())
# tree.print_leaf_nodes(tree.root)
# tree.print_leaf_nodes_(tree.root)
# print(tree.number_of_leaf_nodes(tree.root))
# print(tree.size_recursive(tree.root))
# print(tree.get_level(7))
# tree.vertical_order_traversal(tree.root)
# tree.top_view(tree.root)
# tree.bottom_view(tree.root)
# tree.left_view(tree.root)
# tree.right_view(tree.root)
# tree.root.right.left.right = Node(8) 
# tree.root.right.right.right = Node(9) 
# tree.in_order_traversal_iterative(tree.root)
# tree.pre_order_traversal_iterative(tree.root)
# tree=BinaryTree(1)
# tree.root.left=Node(2)
# tree.root.right=Node(3)
# tree.reverse_pre_order_traversal_iterative(tree.root)
# tree.post_order_traversal_iterative(tree.root)

# # print(tree.size_recursive(tree.root))
# print(tree.size_iterative())
# tree.print_vertical_order(tree.root)
# print(tree.height(tree.root))
            
# tree=BinaryTree(1)
# tree.root.left      = Node(2) 
# tree.root.right     = Node(3) 
# tree.root.left.left  = Node(4) 
# tree.root.left.right  = Node(5)
# # tree.post_order_traversal(tree.root)
# # print(tree.level_order_traversal(tree.root))
# tree.reverseLevelOrder(tree.root)
# 
# tree=BinaryTree(1)
# tree.root.left=Node(2)
# tree.root.right=Node(3)
# tree.root.left.left=Node(4)
# tree.root.left.right=Node(5)
# tree.root.right.left=Node(6)
# tree.root.right.right=Node(7)
# tree.root.right.right.right=Node(8)
# tree.pre_order_traversal(tree.root)
# print("=================")
# tree.in_order_traversal(tree.root)
# print("=================")
# tree.post_order_traversal(tree.root)
