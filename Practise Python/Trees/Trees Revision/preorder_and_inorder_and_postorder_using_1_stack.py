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

# Printing the preorder, inorder and postorder traversal of the tree using 1 stack
def preorder_and_inorder_postorder_using_1_stack(self) -> List[List[int]]:
    if self is None:
        return
    
    # Creating 3 lists to store the preorder, inorder and postorder traversal of the tree
    pre_order = []
    in_order = []
    post_order = []
    
    # Creating a list to store the final answer
    final_answer = []
    
    # Creating a pair of node and num
    node = self
    num = 1
    pair = [node,num]
    
    # Creating a stack and pushing the pair of node and num in the stack
    # Stack will be [[node,num]]
    stack = []
    stack.append(pair)
    
    # While the stack is not empty
    while len(stack) > 0:
        # If num is 1, then append the data of the node in the pre_order list
        # Increment the num by 1
        # If the left child of the node is not None, then create a pair of left child and num
        # Push the pair in the stack
        if stack[-1][1] == 1:
            pre_order.append(stack[-1][0].data)
            stack[-1][1] += 1
            if stack[-1][0].left:
                pair = [stack[-1][0].left,1]
                stack.append(pair)
        
        # If num is 2, then append the data of the node in the in_order list
        # Increment the num by 1
        # If the right child of the node is not None, then create a pair of right child and num
        # Push the pair in the stack
        elif stack[-1][1] == 2:
            in_order.append(stack[-1][0].data)
            stack[-1][1] += 1
            if stack[-1][0].right:
                pair = [stack[-1][0].right,1]
                stack.append(pair)
        
        # If num is 3, then append the data of the node in the post_order list
        # Pop the pair from the stack
        # Note: We are not incrementing the num here and we are not pushing any pair in the stack 
        # We are just popping the pair from the stack        
        elif stack[-1][1] == 3:
            post_order.append(stack[-1][0].data)
            stack.pop()

    # Appending the pre_order, in_order and post_order list in the final_answer list
    final_answer.append(pre_order)
    final_answer.append(in_order)
    final_answer.append(post_order)
    
    # Returning the final_answer list which is a list of lists
    return final_answer


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

# Printing the preorder, inorder and postorder traversal of the tree using 1 stack
# The output is a list of lists
print("The preorder, inorder and postorder traversal of the tree using 1 stack is: ")
print(preorder_and_inorder_postorder_using_1_stack(root))