# Created a class Node with init function, 
# We can use this class to create a node with data and left and right child as None
from typing import Union


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
# Inserting a node in the Binary Search tree
def insert(self,data):
    if self is None:
        return
    
    # If self.data is not None
    if self.data:
        # If data is less than self.data, then insert it in the left subtree
        if data < self.data:
            # If self.left is None, then create a new node and insert the data
            if self.left is None:
                self.left = Node(data)
                # If self.left is not None, then insert the data in the left subtree
            else:
                insert(self.left,data)
        # If data is greater than self.data, then insert it in the right subtree
        elif data > self.data:
            # If self.right is None, then create a new node and insert the data
            if self.right is None:
                self.right = Node(data)
                # If self.right is not None, then insert the data in the right subtree
            else:
                insert(self.right,data)

def LCA_in_a_BST(self,n1,n2) -> Union[int , None]:
    if self is None:
        return None
    
    cur = self.data
    
    if(cur > n1.data and cur > n2.data):
        return LCA_in_a_BST(self.left,n1,n2)
    if(cur < n1.data and cur < n2.data):
        return LCA_in_a_BST(self.right,n1,n2)
    return self.data
    

root = Node(1)
insert(root,6)
insert(root,2)
insert(root,3)
insert(root,10)
insert(root,8)
insert(root,4)
insert(root,5)
insert(root,9)
insert(root,7)
#          1
#             6
#      2            10
#       3         8
#         4     7   9
#           5
n1 = Node(7)
n2 = Node(5)
print(f"Lowest Common Ancestor of {n1.data} and {n2.data} is {LCA_in_a_BST(root,n1,n2)}")


