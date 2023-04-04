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

# Function to check if two trees are identical
def check_identical_trees(self,root) -> bool:
    # If any of the trees is None, then check the equality of the trees
    # If both the trees are None, then return True
    # Else return False if the equality of the trees is not satisfied
    if self is None or root is None:
        return self==root
    
    # If tree1 and tree2 are not None, then check if the data of the root nodes are equal
    # and check if the left and right subtrees are identical
    # If all the conditions are satisfied, then return True
    # Else return False
    return (self.data==root.data and 
            check_identical_trees(self.left,root.left) and 
            check_identical_trees(self.right,root.right))

    
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

root1 = Node(1)
insert(root1,6)
insert(root1,2)
# insert(root1,3)
# insert(root1,10)
insert(root1,8)
insert(root1,4)
insert(root1,5)
insert(root1,9)
insert(root1,7)

# Check if the trees are identical :
print(f"Are the trees identical? {check_identical_trees(root,root1)}")