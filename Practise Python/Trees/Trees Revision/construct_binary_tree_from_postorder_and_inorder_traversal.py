from typing import List


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def BFS(self) -> List[List[int]]:
    if self is None:
        return []
    
    ans = []
    queue = []
    queue.append(self)
    
    while queue:
        level = []
        size = len(queue)
        
        while(size > 0):
            node = queue.pop(0)
            level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            size -= 1
            
        ans.append(level)
    
    return ans
        

def build_tree(inorder, in_start, in_end, postorder, post_start, post_end, in_map):
    # Base case : When post_start > post_end or in_start > in_end
    if(post_start > post_end or in_start > in_end):
        return None
    
    # Get the root node from postorder
    # Get the index of root node in inorder using in_map
    # Get the number of nodes in left subtree
    root = Node(postorder[post_end])
    in_root = in_map[postorder[post_end]]
    nums_left = in_root - in_map[inorder[in_start]]
    
    # Build the left subtree
    root.left = build_tree(
        inorder, in_start, in_root - 1, 
        postorder, post_start, post_start + nums_left - 1, 
        in_map
        )
    
    # Build the right subtree
    root.right = build_tree(
        inorder, in_root + 1, in_end, 
        postorder, post_start + nums_left, post_end - 1, 
        in_map
        )
    
    # Return the root node
    return root




def construct_tree(inorder, postorder):
    # Create a map to store the index of each node in inorder
    # This will help us to spot the root index and then 
    # find the number of nodes in left subtree in O(1) time
    in_map = {}
    for i in range(len(inorder)):
        in_map[inorder[i]] = i
    
    # Build the tree
    root = build_tree(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, in_map)
    
    # Calling level order traversal to verify the tree
    print(BFS(root))


inorder = [40, 20, 50, 10, 60, 30]
postorder = [40 ,50 ,20 ,60 ,30 ,10]

construct_tree(inorder, postorder)