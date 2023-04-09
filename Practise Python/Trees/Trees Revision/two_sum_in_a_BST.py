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

def inorder_tree(self,my_list):
    if self:
    # Left, Root, Right
        inorder_tree(self.left,my_list)
        my_list.append(self.data)
        inorder_tree(self.right,my_list)

def two_sum(self,target):
    # Creating an empty list
    my_list = []
    
    # Calling the inorder_tree function to get the sorted order of the tree
    inorder_tree(self,my_list)
    
    # Two pointer approach
    # Start pointer will point to the first index of the list
    # End pointer will point to the last index of the list
    start = 0
    end = len(my_list)-1
    
    # Looping through the list until start is less than end
    while(start < end):
        if my_list[start] + my_list[end] == target:
            print(f"Two Sum values are {my_list[start]} and {my_list[end]}")
            return True
        elif my_list[start] + my_list[end] < target:
            start += 1
        else:
            end -= 1
    return False


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

# Target Sum
target = 15

print(f"Does Two Sum exist in the tree for the given target? {two_sum(root,target)}")