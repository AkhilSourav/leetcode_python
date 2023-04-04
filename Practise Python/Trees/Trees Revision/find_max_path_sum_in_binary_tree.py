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


# Find the maximum path sum in a binary tree
# The path need not pass through the root node
# The path can start and end at any node in the tree
# Every node can appear only once in the path
def find_max_path_sum(self):
    max_path = [0]
    find_max(self,max_path)
    return max_path[0]


# Function to find the maximum path in a Binary Tree
def find_max(self,maxi):
    if self is None:
        return 0
    
    # Find the maximum path in the left subtree
    # If the maximum path is negative, then we can ignore it
    lh = max(0,find_max(self.left,maxi))
    
    # Find the maximum path in the right subtree
    # If the maximum path is negative, then we can ignore it
    rh = max(0,find_max(self.right,maxi))
    
    # Update the maximum path sum with the largest value in the entire tree
    maxi[0] = max(maxi[0],lh+rh+self.data)
    
    # Return the maximum path sum in the subtree
    return self.data + max(lh,rh)
    
    
    
    
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


# Print the maximum path sum in the tree :
print(f"Maximum path sum is {find_max_path_sum(root)}")