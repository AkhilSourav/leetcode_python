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

# Checks if the node is a binary node or not
# A binary node is a node which has both left and right child
def is_binary_node(self) -> bool:
    if self.left is not None and self.right is not None:
        return True
    else :
        return False

# Checks if the node is a leaf node or not
# A leaf node is a node which has both left and right child as None
def is_leaf(self) -> bool:
    if self is None:
        return False
    if self.left is None and self.right is None:
        return True
    return False

# Left Boundary Traversal
# This function will traverse the left boundary of the tree
# The left boundary of the tree is the left most path of the tree
# Starting from the root's left till the node before the leaf node
def left_boundary(self,res):
    
    if is_leaf(self) == True or self is None:
        return 
    
    else:
        res.append(self.data)
        if self.left: 
            left_boundary(self.left,res)
        else:
            left_boundary(self.right,res)


# Basic Inorder Traversal
# This function will store all the leaf nodes in the res list
# We can also use preorder or postorder traversal
def in_order(self,res):
    if self is None:
        return 
    
    in_order(self.left,res)
    if is_leaf(self) == True:
        res.append(self.data)
    in_order(self.right,res)

# Right Boundary Traversal
# This function will traverse the right boundary of the tree
# The right boundary of the tree is the right most path of the tree
# Starting from the root's right till the node before the leaf node
# We are traversing the right boundary in reverse order in order to complete the boundary traversal
def right_boundary(self,res):
    if is_leaf(self) == True or self is None:
        return
    
    else:
        res.append(self.data)
        if self.right:
            right_boundary(self.right,res)
        else:
            right_boundary(self.left,res)

# Complete Boundary Traversal
# This function will traverse the boundary of the tree
# The boundary of the tree is the left boundary, leaf nodes and right boundary
def boundary_traversal(self):
    if self is None:
        return
    
    ans = []
    
    # Below while loop is for getting the first binary node of the tree
    # We are storing the data of the nodes in the ans list till we get the first binary node
    while is_binary_node(self) == False:
        ans.append(self.data)
        if self.left:
            self = self.left
        else:
            self = self.right
    
    if self is None:
        return
            
    
    # If the node is a binary node, then we will append the node's data to the ans list
    if is_leaf(self) == False:
        ans.append(self.data)
    
    # If self.left is not None, then we will traverse the left boundary of the tree
    # We are checking this condition bcoz what if the tree is a linear or skewed tree
    # In that case, we will not have any left subtree
    if self.left:
        left_boundary(self.left,ans)
        
    # We will traverse the leaf nodes of the tree
    in_order(self,ans)
        
    # If self.right is not None, then we will traverse the right boundary of the tree
    # We are checking this condition bcoz what if the tree is a linear or skewed tree
    # In that case, we will not have any right subtree
    if self.right:
        right_ans = []
        right_boundary(self.right,right_ans)
        ans.extend(right_ans[::-1])
        
    print(ans)

    
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


boundary_traversal(root)

