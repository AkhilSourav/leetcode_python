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


# Function to check if the Binary Search Tree is valid or not
def isBSTValid(self, lt_min , rt_max) -> bool:
    # If self is None, it means we have reached the end of the tree, and the tree is valid
    if self is None:
        return True
    # If the data is less than the minimum value or greater than the maximum value, then return False
    if self.data < lt_min[0] or self.data > rt_max[0]:
        return False
    
    # While traversing the left subtree, the maximum value is the current node's data
    # While traversing the right subtree, the minimum value is the current node's data
    # If the left subtree is valid and the right subtree is valid, then the tree is valid
    return isBSTValid(self.left, lt_min, [self.data]) and isBSTValid(self.right, [self.data], rt_max)



root = Node(6)
root.left = Node(3)
# Faulty Case below added to test the code
root.left.right = Node(2)
root.left.left = Node(1)

min = float('-inf')
lt_min = [min]
max = float('inf')
rt_max = [max]

print(f"Is the Binary Search Tree valid? {isBSTValid(root, lt_min, rt_max)}")

