# Trong backend/node.py
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1
        
        self.curr_x = None
        self.curr_y = None
        self.target_x = None
        self.target_y = None
        self.is_hidden = False 
        

        self.vis_left = None
        self.vis_right = None