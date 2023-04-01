from typing import List

# Created a class Node with init function, 
# We can use this class to create a node with data and left and right child as None
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
# Inserting a node in the tree
def insert(self,data):
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
    else:
    # If self.data is None, then insert the data
        self.data = data

# Iterative Preorder Traversal using Stack : Root, Left, Right
def iterative_pre_order(self) -> List[int]:
    if self is None:
        return
    
    # Create an empty list to store the result
    ans = []
    # Create an empty stack and push root to it
    stack = []
    stack.append(self)
    
    # Loop while stack is not empty
    while(len(stack) > 0):
        # Pop an item from stack and add it to the list
        # For stack, we are using pop() function but for queue, we are using popleft() or pop(0)
        node = stack.pop()
        ans.append(node.data)
        # Push right and left child of the popped node to the stack
        # Note that right child is pushed first so that left is processed first
        # This is because we are using a stack and we want to process the left subtree first
        # Since the Stack is LIFO, we want to process the left subtree first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    # Return the ans list   
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


print("\nPrinting Pre Order Traversal using Iterative Method:")
print(iterative_pre_order(root))