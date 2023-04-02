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


# Function to check if a binary tree is balanced or not
# This function returns the height of the tree if it is balanced
# If the tree is not balanced, then it returns -1
# A Binary tree is balanced if the difference between the height of the left subtree and the right subtree is not more than 1
def check_for_balanced_binary_tree(self):
    if self is None:
        return 0
    
    # Getting the height of the left subtree
    lh = check_for_balanced_binary_tree(self.left)
    # If the left subtree is not balanced, then return -1
    if lh == -1:
        return -1
    # Getting the height of the right subtree
    rh = check_for_balanced_binary_tree(self.right)
    # If the right subtree is not balanced, then return -1
    if rh == -1:
        return -1
    
    # If the difference between the height of the left subtree and the right subtree is more than 1, then return -1
    if abs(lh-rh) > 1:
        return -1
    
    # Returning the maximum depth of the binary tree
    return 1 + max(lh,rh)


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

print("Balanced Binary Tree") if check_for_balanced_binary_tree(root) != -1 else print("Not Balanced Binary Tree")
    