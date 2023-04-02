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
    
# Finding the Inorder Successor ( Smallest value in the right subtree )
def get_inorder_successor(self):
    current = self
    while(current.left is not None):
        current = current.left
    return current

# Finding the Inorder Predecessor ( Largest value in the left subtree )
def get_inorder_predecessor(self):
    current = self
    while current.right is not None:
        current = current.right
    return current


# Deleting a node from the Binary Search Tree
def delete_node(self,data):
    # if self (root) is None, then return self
    if self is None:
        return
    
    # If data is less than self.data, then delete the node from the left subtree
    # We are assigning back to self.left because after deleting the node, the left subtree will be changed
    if data < self.data and self.left is not None:
        self.left = delete_node(self.left,data)
        
    # If data is greater than self.data, then delete the node from the right subtree
    # We are assigning back to self.right because after deleting the node, the right subtree will be changed
    elif data > self.data and self.right is not None:
        self.right = delete_node(self.right,data)
    
    # If data is equal to self.data, then delete the node    
    else:
        # Case for when node has 0 or 1 child
        if self.left is None:
            temp = self.right
            self = None
            return temp
        if self.right is None:
            temp = self.left
            self = None
            return temp
        
        # Case for when node has 2 children
        # Get the ( left most node ) inorder successor in the right subtree
        # We can also do, get the ( right most node ) inorder predecessor in the left subtree
        temp = get_inorder_successor(self.right)
        """temp = get_inorder_predecessor(self.left)"""
        # Assign the inorder successor value to self.data
        # Note: We are just replacing the value of the node to be deleted with the inorder successor value and not the node itself
        # Because if we do so, then we will lose the connections with the left and right subtree 
        self.data = temp.data
        # So once job is done, we have to delete the inorder successor node from the right subtree
        # We are assigning back to self.right because after deleting the node, the right subtree will be changed
        self.right = delete_node(self.right,temp.data)
        """self.left = delete_node(self.left,temp.data)"""
    
    # Return self(root) once all the operations are done
    return self




# Creating a root node with data 60     
root = Node(60)

# Inserting values in the tree
insert(root,40)
insert(root,80)
insert(root,20)
insert(root,50)
insert(root,70)
insert(root,90)

# Printing the Inorder tree Traversal
print_inorder_tree(root)
print("Before deleting a node")

# Deleting a node from the tree
root = delete_node(root,40)
print_inorder_tree(root)
print(" After deleting a node")


