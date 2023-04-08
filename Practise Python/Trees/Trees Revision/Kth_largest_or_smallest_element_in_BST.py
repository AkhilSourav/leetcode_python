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

# Since Inorder Traversal is always sorted, we can find the Kth smallest element in the BST
def KthSmallestUtil(self, c, k):
     
    # Base cases, the second condition
    # is important to avoid unnecessary
    # recursive calls later on in the code
    if self == None or c[0] >= k:
        return
    
    # Recur for left subtree
    KthSmallestUtil(self.left, c, k)
    
    # Increment count of visited nodes
    c[0] += 1
    
    # If c becomes k now, then this is
    # the k'th smallest
    if c[0] == k:
        print("Kth Smallest element is",self.data)
        return
    
    # Recur for right subtree 
    KthSmallestUtil(self.right, c, k)

# Since Inorder Traversal is always sorted, we can find the Kth largest element in the BST
# By doing a reverse inorder traversal i.e Right, Root, Left
def KthLargestUtil(self, c, k):
    # Base cases, the second condition
    # is important to avoid unnecessary
    # recursive calls later on in the code
    if self == None or c[0] >= k:
        return
    
    # Recur for right subtree 
    KthLargestUtil(self.right, c, k)
    
    # Increment count of visited nodes
    c[0] += 1
    
    # If c becomes k now, then this is
    # the k'th largest
    if c[0] == k:
        print("Kth Largest element is", self.data)
        return
    
    # Recur for left subtree
    KthLargestUtil(self.left, c, k)
    
    
    
def find_Kth_smallest_element(self,k):
    if self is None:
        return
    
    count = [0]
    
    # Driver code
    KthSmallestUtil(self,count,k)
    
def find_Kth_largest_element(self,k):
    if self is None:
        return
    
    count = [0]
    # Driver code
    KthLargestUtil(self,count,k)
    

root = Node(60)
insert(root,40)
insert(root,80)
insert(root,20)
insert(root,50)
insert(root,70)
insert(root,90)

# Kth element in BST
K = 2

# Print the Kth smallest element
find_Kth_smallest_element(root,K)

# Print the Kth largest element
# Note: We can find the Kth largest element by finding the (n-k+1)th smallest element 
find_Kth_largest_element(root,K)


# Note: We can reduce the space complexity from O(N to O(1) by using Morris Traversal