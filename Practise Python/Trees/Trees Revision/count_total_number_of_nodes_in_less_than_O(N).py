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

def count_total_nodes(self):
    if self is None:
        return 0
    # In the below get height function we have passed 0 for left and 1 for right
    # This is done to avoid duplication of code for getting the height of left and right subtree
    lh = get_height(self.left,0)
    rh = get_height(self.right,1)
    
    # If lh and rh are equal, then it is a complete binary tree
    # So, we can use the formula 2^h - 1 to get the total number of nodes
    # where h is the height of the tree
    if lh==rh:
        return (2**lh) - 1
    
    # If lh and rh are not equal, then it is not a complete binary tree
    # So, we will recursively call the function for left and right subtree
    return 1 + count_total_nodes(self.left) + count_total_nodes(self.right)


def get_height(self,flag):
    if self is None:
        return 0
    height = 0
    while(self):
        height += 1
        if flag ==0:
            self = self.left
        else:
            self = self.right
    return height



root = Node(6)
insert(root,5)
insert(root,7)
insert(root,4)
insert(root,8)
insert(root,3)
insert(root,9)

"""NOTE: This method only works for complete binary trees """
print(f"Total number of nodes in the tree is {count_total_nodes(root)}")