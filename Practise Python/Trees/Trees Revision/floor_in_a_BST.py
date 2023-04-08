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

# Find the floor of a given key in a BST
def find_floor(self, key):
    floor = -1
    
    while(self):
        # If key is equal to self.data, then return self.data
        if self.data == key:
            floor = self.data
            return floor
        
        # If key is less than self.data, then floor must be in the left subtree
        if key < self.data:
            self = self.left
        
        # If key is greater than self.data, then floor must be in the right subtree
        # Update the floor to self.data and then search in the right subtree
        else:
            floor = self.data
            self = self.right
    
    return floor

root = Node(60)
insert(root,40)
insert(root,80)
insert(root,20)
insert(root,50)
insert(root,70)
insert(root,90)

key = 39
# Print the floor of a given key in a BST
print(f"The floor of given key is {find_floor(root,key)}")