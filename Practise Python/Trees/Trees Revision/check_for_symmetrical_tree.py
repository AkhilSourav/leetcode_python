# Created a class Node with init function, 
# We can use this class to create a node with data and left and right child as None
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
# Check for Symmetrical Tree (Mirror Image)
# We can check for symmetrical tree by checking if 
# the left child of the left subtree is equal to the right child of the right subtree
# and the right child of the left subtree is equal to the left child of the right subtree
def check_for_symmetrical_tree(left, right):
    # Check for symmmetry when either of the left or right child is None 
    if left is None or right is None:
        return left == right
    # If the data of the left child is not equal to the data of the right child, return False
    if left.data != right.data:
        return False
    # If the data of the left child is equal to the data of the right child,
    else:
        # Check for symmetry of the left subtree and right subtree
        return check_for_symmetrical_tree(left.left, right.right) and check_for_symmetrical_tree(left.right, right.left)

# Check for Symmetry of the tree
def check_for_symmetry(self):
    # If the root is None, return True
    if self is None:
        return True
    return check_for_symmetrical_tree(root.left, root.right)



root = Node(1)
root.left = Node(2)
root.left.right = Node(3)
root.right = Node(2)
root.right.left = Node(3)


print(f"Is the tree symmetrical? {check_for_symmetry(root)}")