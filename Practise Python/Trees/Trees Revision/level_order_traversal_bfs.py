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



# Level Order Traversal: BFS
def BFS(self) -> List[List[int]]:
    # If root is None, then return None
    if self is None:
        return []
    
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
        # size will store the length of number of nodes at a particular level
        size = len(queue)
        
        # While there are nodes at a particular level
        while(size > 0):
            # Pop the first node from the queue and store it in node
            node = queue.pop(0)
            # Append the data of the node to the level list
            level.append(node.data)
            # If the left child of the node is not None, then append it to the queue
            if node.left:
                queue.append(node.left)
            # If the right child of the node is not None, then append it to the queue
            if node.right:
                queue.append(node.right)
            
            # Decrement the size
            size -= 1
            
        # Append the level list to the ans list
        ans.append(level)
    
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

# Printing Level Order Traversal
#          1
#               6
#          2        10
#              3,8
#          4        7,9
#                         5
print("Level Order Traversal: BFS")
print(BFS(root))    

