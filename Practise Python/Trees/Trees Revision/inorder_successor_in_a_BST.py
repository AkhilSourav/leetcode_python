# Created a class Node with init function, 
# We can use this class to create a node with data and left and right child as None
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

# Inorder Successor in a BST
def inorder_successor(self, n, successor):
    if self is None:
        return
    # If n.data is greater than or equal to self.data, then the inorder successor of n.data lies in the right subtree
    if n.data >= self.data:
        inorder_successor(self.right, n, successor)
    else:
    # If n.data is less than self.data, then the inorder successor of n.data lies in the left subtree
    # Update the successor with self.data and then search for the inorder successor in the left subtree
        successor[0] = self.data
        inorder_successor(self.left, n, successor)
    # Return the successor
    return successor[0]


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

# Intialize the successor with None
successor = [None]
# Node whose inorder successor is to be found
n = Node(10)
print(f"Inorder Successor of {n.data} is: ", inorder_successor(root, n, successor))

        
    