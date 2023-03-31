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
                    self.left.insert(data)
            # If data is greater than self.data, then insert it in the right subtree
            elif data > self.data:
                # If self.right is None, then create a new node and insert the data
                if self.right is None:
                    self.right = Node(data)
                    # If self.right is not None, then insert the data in the right subtree
                else:
                    self.right.insert(data)
        else:
        # If self.data is None, then insert the data
            self.data = data
    
    
    # Printing the node data
    def print_node_data(self):
        print(self.data, end="  ")
    
    # Inorder Traversal: Left, Root, Right
    def print_inorder_tree(self):
        # Inorder Traversal: Left, Root, Right
        if self.left:
            self.left.print_inorder_tree()
        if self.data:
            self.print_node_data()
        if self.right:
            self.right.print_inorder_tree()
    
    # Finding the Inorder Successor ( Smallest value in the right subtree )
    def get_inorder_successor(self):
        current = self
        while(current.left is not None):
            current = current.left
        return current
            
    def delete_node(self,data):
        # if self (root) is None, then return self
        if self is None:
            return self
        
        # If data is less than self.data, then delete the node from the left subtree
        if data < self.data and self.left is not None:
            self.left = self.left.delete_node(data)
        # If data is greater than self.data, then delete the node from the right subtree
        elif data > self.data and self.right is not None:
            self.right = self.right.delete_node(data)
        
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
            temp = self.right.get_inorder_successor()
            # Assign the inorder successor value to self.data
            self.data = temp.data
            # Delete the inorder successor node in the right subtree
            self.right = self.right.delete_node(temp.data)
        return self

# Different ways of printing the node value        
root = Node(60)
# 1 way of printing node value
root.print_node_data()
# 2 way of printing node value
print(root.data)
# 3 way of printing node value after updating the node value
root.data = 70
print(root.data)



# Inserting values in the tree
root.insert(50)
root.insert(40)
root.insert(70)
root.insert(80)

# Printing the Inorder tree Traversal
root.print_inorder_tree()
print("Before deleting a node")

# Deleting a node from the tree
root.delete_node(80)
root.print_inorder_tree()
print("After deleting a node")


