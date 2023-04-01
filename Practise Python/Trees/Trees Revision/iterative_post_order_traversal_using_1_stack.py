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

# Iterative Post Order Traversal using 1 stack : Left, Right, Root
def iterative_post_order(self) -> List[int]:
    # ans is the list which will store the post order traversal
    ans = []
    # stack will store the nodes
    stack = []
    # cur will store the root node
    cur = self
    
    # While cur is not None or stack is not empty
    while cur is not None or len(stack) >  0:
        # If cur is not None, then append it to the stack and move to the left child
        if cur is not None:
            stack.append(cur)
            cur = cur.left
            
        # If cur is None, then pop the top element from the stack
        else:
            # If the top element from the stack has a right child, then move to the right child
            temp = stack[-1].right
            # If temp is None, then pop the top element from the stack and append it to the ans list
            if temp is None:
                temp = stack.pop()
                ans.append(temp.data)
                # If length of stack is greater than 0 and 
                # temp is equal to the right child of the top element from the stack, 
                # then pop the top element from the stack and append it to the ans list
                while(len(stack)>0 and temp == stack[-1].right):
                    temp = stack.pop()
                    ans.append(temp.data)
            # If temp is not None, then move to the right child
            else:
                cur = temp
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

print("Iterative Post Order Traversal using Stack : Left, Right, Root")
print(iterative_post_order(root))