from typing import List

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


# Same as level_order_traversal_bfs.py but with a slight change
# We need to create a flag and update it whenever a new level is encountered
# If the flag is 0, then append the level list to the ans list
# If the flag is 1, then append the reversed level list to the ans list                
def zig_zag_traversal(self) -> List[List[int]]:
    # If root is None, then return None
    if self is None:
        return []
    
    # flag is for keeping track of the level whenever it changes
    # If flag is 0, then append the level list to the ans list
    # If flag is 1, then append the reversed level list to the ans list
    flag = 0
    # ans is for storing the list of levels
    ans = []
    # queue is a list of nodes
    queue = []
    # Append the root node to the queue
    queue.append(self)
    
    # While the queue is not empty
    while(len(queue) > 0):
        # level will store all the nodes at a particular level
        level = []
        # size will store the number of nodes at a particular level
        size = len(queue)
        
        # While there are nodes at a particular level
        while(size > 0):
            # Pop the first node from the queue and store it in node
            node = queue.pop(0)
            # If the left child of the node is not None, then append it to the queue
            if node.left:
                queue.append(node.left)
            # If the right child of the node is not None, then append it to the queue
            if node.right:
                queue.append(node.right)
            # Append the data of the node to the level list
            level.append(node.data)
            # Decrement the size
            size -= 1
            
        # Append the level list to the ans list based on the flag
        if flag == 0:
            ans.append(level)
            flag = 1
        else:
            # If the flag is 1, then append the reversed level list to the ans list
            # [::-1] is used to reverse elements in the list
            ans.append(level[::-1])
            flag = 0
    
    # Return the ans list with all the nodes at each level
    return ans

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

# Print the zig zag traversal of the binary tree
print(zig_zag_traversal(root))