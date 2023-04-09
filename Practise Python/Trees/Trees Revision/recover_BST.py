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

# Inorder Traversal: Left, Root, Right
def print_inorder_tree(self):
    if self:
    # Left, Root, Right
        print_inorder_tree(self.left)
        print(self.data, end="  ")
        print_inorder_tree(self.right)


def inorder(self,first,middle,last,prev):
    if self is None:
        return
    
    inorder(self.left,first,middle,last,prev)
    
    # Main Logic sits here
    if prev[0] is not None and self.data < prev[0].data:
    # Two Cases:
        # 1. If this is the first violation and If first is None, then assign first and middle to prev and self
        if first[0] is None:
            first[0] = prev[0]
            middle[0] = self
        # 2. If this is the second violation and If first is not None, then assign last to self
        else:
            last[0] = self
    
    # Assign prev to self        
    prev[0] = self
    
    inorder(self.right,first,middle,last,prev)
            
    

def recover_BST(self):
    if self is None:
        return
    
    # Initialize first, middle, last and prev as None
    first, middle, last, prev = [None], [None], [None], [None]
    inorder(self,first,middle,last,prev)
        
        
    # If first and last are not None, then swap the data of first and last
    # If first is not None and last is None, then swap the data of first and middle
    if first[0] is not None:
        if last[0] is not None:
            print(f"\nSwapping {first[0].data} and {last[0].data}")
            first[0].data, last[0].data = last[0].data, first[0].data
        else:
            print(f"\nSwapping {first[0].data} and {middle[0].data}")
            first[0].data, middle[0].data = middle[0].data, first[0].data




root = Node(3)
root.right = Node(2)
root.left = Node(4)

# Printing the Tree Before Swapping
print_inorder_tree(root)
# Swapping the Nodes
recover_BST(root)
# Printing the Tree After Swapping
print_inorder_tree(root)
