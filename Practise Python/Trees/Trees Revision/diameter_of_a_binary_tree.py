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


# Diameter of a Binary Tree means the maximum number of nodes between any two nodes
# It need not pass through the root node
def diameter_of_binary_tree(self):
    # Since Int is immutable in python, we need to pass it as a list with one element
    diameter=[0]
    find_max(self,diameter)
    # Return the diameter of the tree as the first element of the list
    return diameter[0]


# Function to find the maximum height of the tree
def find_max(self,maxi):
    if self is None:
        return 0
    
    # Find the maximum height of the left subtree
    left_height = find_max(self.left,maxi)
    # Find the maximum height of the right subtree
    right_height = find_max(self.right,maxi)
    
    # Find the maximum diameter of the tree
    # Diameter of a tree is the maximum of the following:
    # 1. Height of the left subtree
    # 2. Height of the right subtree
    maxi[0] = max( maxi[0] , left_height+right_height)
    
    return 1 + max( left_height , right_height)

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

# Diameter of a Binary Tree :
print(f"Diameter of the tree is {diameter_of_binary_tree(root)}")





            