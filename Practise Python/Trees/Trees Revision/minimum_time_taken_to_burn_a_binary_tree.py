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

def bfs(self, parent):
    if self is None:
        return 
    
    queue = []
    queue.append(self)
    
    while(len(queue)>0):
        cur = queue.pop(0)
        
        if cur.left:
            # Storing in the form of [node, parent]
            parent[cur.left] = cur
            queue.append(cur.left)
        
        if cur.right:
            # Storing in the form of [node, parent]
            parent[cur.right] = cur
            queue.append(cur.right)
    
    return parent

def pre_order(self, my_target):
    if self:
        if self.data == my_target[0]:
            # We will remove the first element from the list and append the current node
            # This we are doing bcoz we don't want to use another list to output the target node
            # We will use the same list to store the target node
            my_target.pop(0)
            my_target.append(self)
            return
        pre_order(self.left, my_target)
        pre_order(self.right, my_target)


def minimum_time_taken_to_burn_a_binary_tree(self, target):
    # At first we need to find the parent of each of nodes
    # We will use BFS to find the parent of each node 
    # since left and right child are known things but for the parent we need to traverse the tree
    parent = {}
    # Storing in the form of [node, parent]
    # Marking the parent of root as None
    parent[self] = None
    bfs(self, parent)
    
    # Now we need to find the target node
    # We will use pre-order traversal to find the target node
    # We can use any other traversal method as well
    # We will store the target node in a list
    my_target = [target]
    pre_order(self, my_target)
   
    # Created a set to store the visited nodes
    visited = set([])
    queue = []
    visited.add(my_target[0])
    queue.append(my_target[0])
    
    # We will use a variable to store the time taken to burn the tree
    time_taken = 0
    # We will use a variable to check if the tree is burning or not
    # Burn will be true if the tree is burning i.e 
    # if the current node has a left or right child or parent which is not visited
    burn = False
    
    # We will traverse the tree till we reach the level k
    # Below code is same as level_order_traversal_bfs.py
    while queue:
        size = len(queue)
        while(size > 0):
            cur = queue.pop(0)
            if cur.left and cur.left not in visited:
                queue.append(cur.left)
                visited.add(cur.left)
                burn = True
            if cur.right and cur.right not in visited:
                queue.append(cur.right)
                visited.add(cur.right)
                burn = True
            if parent.get(cur) and parent.get(cur) not in visited:
                queue.append(parent.get(cur))
                visited.add(parent.get(cur))
                burn = True
            size -= 1
        # If burn is true, then we will increment the time_taken by 1
        # and make burn as false
        if burn:
            time_taken += 1
            burn = False
            
    return time_taken


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

#                     1
#                             6
#               2             |        10
#                   3         |    8
#                       4     |7       9
#                           5 |

"""Note: Using the same logic from print_all_nodes_at_a_distance_K_in_a_binary_tree.py"""
target = 5
print(f"Minimum time taken to burn the tree from target {target} is {minimum_time_taken_to_burn_a_binary_tree(root, target)}")