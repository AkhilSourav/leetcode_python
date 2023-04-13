# Created a class Node with init function, 
# We can use this class to create a node with data and left and right child as None


from typing import List


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


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
        # size will store the number of nodes at a particular level
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

def modified_preorder_traversal(root):
    if root is None:
        return

    if root.left and root.right:
        # If the root's data is greater than the sum of the left and right child data
        # Then we need to modify the left and right child data
        if root.data > root.left.data + root.right.data:
            root.left.data = root.right.data = root.data
        else:
            # If the sum of the left and right child data is greater than the root's data
            # Then we need to modify the root's data
            root.data = root.left.data + root.right.data
    
    modified_preorder_traversal(root.left)
    modified_preorder_traversal(root.right)
    
    # From here starts the backtracking part
    # Start modifying the root's data till the top of the tree
    tot = 0
    if(root.left):
        tot += root.left.data
    if(root.right):
        tot += root.right.data
    if(root.left or root.right):
        root.data = tot

# Function to return satisfied children sum property binary tree
def children_sum_property_satisfied(root):
    modified_preorder_traversal(root)
    print(f"Chidren Sum Property {BFS(root)}")

  
# Inserting a node in the Binary Search tree
root = Node(10)
root.left = Node(10)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.left = Node(30)
root.right.right = Node(5)

# Calling the function
children_sum_property_satisfied(root)