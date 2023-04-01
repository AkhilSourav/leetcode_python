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


# Iterative In Order Traversal using Stack : Left, Root, Right
# This is similar to recursive in order traversal, there we have an auxillary space stack
# But here we have explicitly created a stack to store the nodes
def iterative_in_order(self) -> List[int]:
    # If self is None, then return
    if self is None:
        return
    
    # Create an empty list to store the result
    ans = []
    # Create an empty stack
    stack = []
    # Initialize current node as root
    current = self
    
    # Loop while current is not None or stack is not empty
    while(1):
        # If current is not None, push it to the stack and set current to its left child
        if current:
            stack.append(current)
            current  = current.left
        # If current is None and stack is not empty, pop an item from the stack, 
        # add it to the ans list and set current to its right child
        elif current is None and stack:
            current = stack.pop()
            ans.append(current.data)
            current = current.right
        # If current is None and stack is empty, then break
        else:
            break    
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

print("Iterative In Order Traversal using Stack : Left, Root, Right")
print(iterative_in_order(root))

                    