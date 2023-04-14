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
    
    while(len(queue) > 0):
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
        

def build_tree(inorder, in_start, in_end, preorder, pre_start, pre_end, in_map):
    # Base case : When pre_start > pre_end or in_start > in_end
    if(pre_start > pre_end or in_start > in_end):
        return None
    
    # Get the root node from preorder
    # Get the index of root node in inorder using in_map
    # Get the number of nodes in left subtree
    root = Node(preorder[pre_start])
    in_root = in_map[preorder[pre_start]]
    nums_left = in_root - in_map[inorder[in_start]]
    
    # Build the left subtree
    root.left = build_tree(
        inorder, in_start, in_root - 1, 
        preorder, pre_start + 1, pre_start + nums_left, 
        in_map
        )
    
    # Build the right subtree
    root.right = build_tree(
        inorder, in_root + 1, in_end, 
        preorder, pre_start + nums_left + 1, pre_end, 
        in_map
        )
    
    # Return the root node
    return root




def construct_tree(inorder, preorder):
    # Create a map to store the index of each node in inorder
    # This will help us to spot the root index and then 
    # find the number of nodes in left subtree in O(1) time
    in_map = {}
    for i in range(len(inorder)):
        in_map[inorder[i]] = i
    
    # Build the tree
    root = build_tree(inorder, 0, len(inorder) - 1, preorder, 0, len(preorder) - 1, in_map)
    
    # Calling level order traversal to verify the tree
    print(BFS(root))






inorder = [9,3,15,20,7]
preorder = [3,9,20,15,7]

construct_tree(inorder, preorder)