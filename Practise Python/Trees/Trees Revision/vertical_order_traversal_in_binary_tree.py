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

def vertical_order_traversal(self):
    # If root is None, then return None
    if self is None:
        return []
    
    # ans is for storing the list of levels
    ans = []
    # queue is a list of nodes
    queue = []
    # h_level is for storing the horizontal level of the node
    h_level = 0
    # v_level is for storing the vertical level of the node
    v_level = 0
    # Append the root node to the queue {node, horizontal_distance, vertical_distance}
    queue.append([self,h_level,v_level])
    
    # While the queue is not empty
    while(len(queue) > 0):
        # level will store all the nodes at a particular level
        level = []
        # size will store the length of number of nodes at a particular level
        size = len(queue)
        
        # While there are nodes at a particular level
        while(size > 0):
            # Pop the first node from the queue and store it in node
            data_pack = queue.pop(0)
            # Data pack is a list of [node, horizontal_distance, vertical_distance]
            node = data_pack[0]
            h_level = data_pack[1]
            v_level = data_pack[2]
            # Append the data of the node to the level list
            level.append([node.data,h_level,v_level])
            
            # If the left child of the node is not None, then append it to the queue
            if node.left:
                h_left = h_level + 1
                v_left = v_level - 1
                data_keeper = [node.left,h_left,v_left]
                queue.append(data_keeper)
            # If the right child of the node is not None, then append it to the queue
            if node.right:
                h_right = h_level + 1
                v_right = v_level + 1
                data_keeper = [node.right,h_right,v_right]
                queue.append(data_keeper)
                
            
            # Decrement the size
            size -= 1
            
        # Append the level list to the ans list
        ans.extend(level)
    
    # Return the ans list with all the nodes at each level
    return ans

def get_vertical_order(self):
    answer = vertical_order_traversal(self)
    # print(answer)
    
    # my_dict is a dictionary with key as vertical level and value as list of nodes at that level
    my_dict = {}
    for ans in answer:
        # pop always takes last element
        key = ans.pop()
        my_dict.setdefault(key, [])
        # pop(0) always take first element
        my_dict[key].append(ans.pop(0))
    
    # print(my_dict)
    
    ans_list = []
    for value in my_dict:
    # extend is used here because we want to merge two values [value1,value2]
    # If we would have used append then output is [{value1},{value2}]
        ans_list.extend(my_dict[value])
    
    return ans_list


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

print(f"Vertical Order Traversal: {get_vertical_order(root)}")
  