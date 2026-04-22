import pygame
from frontend.constants import *

class TreeVisualizer:
    def __init__(self, surface, font):
        self.surface = surface
        self.font = font
        self.action_logs = []       
        self.current_action = None  
        self.action_timer = 0       
        self.step_counter = 0
        self.allow_target_update = True  
        

        self.visual_root = None 

    def clear(self):
        """Xóa sạch mọi dữ liệu hiển thị và đưa Visualizer về trạng thái rảnh rỗi"""
        self.visual_root = None
        self.action_logs = []
        self.current_action = None
        self.action_timer = 0
        self.step_counter = 0
        self.allow_target_update = True
        self.has_active_snapshot = False
 
        if hasattr(self, 'highlight_timer'):
            self.highlight_timer = 0

    def sync_tree_state(self, node):
        """Sao chép cấu trúc thật của Backend sang cấu trúc Ảo để Render"""
        if not node: return
        node.vis_left = node.left
        node.vis_right = node.right
        node.vis_val = node.val
        self.sync_tree_state(node.left)
        self.sync_tree_state(node.right)

    def process_animation_queue(self):
        self.allow_target_update = False 

        if self.action_timer > 0:
            self.action_timer -= 1
        elif self.action_logs:
            log_entry = self.action_logs.pop(0)
            node = log_entry[0]
            msg = log_entry[1]
            snapshot = log_entry[2] if len(log_entry) > 2 else None
            
            self.step_counter += 1
            self.current_action = {"node": node, "msg": msg}
            
            if snapshot:
                self.visual_root = snapshot["root"]
                for n, (l, r) in snapshot.get("edges", {}).items():
                    n.vis_left = l
                    n.vis_right = r
 
                if "vals" in snapshot:
                    for n, v in snapshot["vals"].items():
                        n.vis_val = v
                        
                self.has_active_snapshot = True
                self.allow_target_update = True  
            else:
                self.has_active_snapshot = False
                keywords = ["thêm", "Xoay", "Thay thế", "Hoán đổi", "Xóa", "xóa"]
                if any(k in msg for k in keywords):
                    self.allow_target_update = True
                
            if node and "thêm" in msg:
                node.is_hidden = False

            self.action_timer = 90 
            
        elif not self.action_logs and self.action_timer == 0:

            self.allow_target_update = True
            self.has_active_snapshot = False

    def update_targets(self, node, min_x, max_x, y):
        if not node: return
        
        x = (min_x + max_x) // 2
        node.target_x = x
        node.target_y = y
        
        if node.curr_x is None:
            node.curr_x = x
            node.curr_y = y

        # SỬ DỤNG CON TRỎ ẢO (vis_left, vis_right)
        self.update_targets(node.vis_left, min_x, x, y + Y_SPACING)
        self.update_targets(node.vis_right, x, max_x, y + Y_SPACING)

    def draw_tree(self, root):

        self.process_animation_queue() 
        

        if self.allow_target_update or self.visual_root is None:
            if not getattr(self, 'has_active_snapshot', False):
                self.visual_root = root
                self.sync_tree_state(self.visual_root)
            self.update_targets(self.visual_root, 0, WIDTH, START_Y + 50) 
            

        if self.visual_root:
            self.animate_nodes(self.visual_root)
            self._draw_edges(self.visual_root)
            self._draw_nodes(self.visual_root)


        if self.current_action:
            msg_text = f"Step {self.step_counter}: {self.current_action['msg']}"
            text_surface = self.font.render(msg_text, True, HIGHLIGHT_COLOR)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, 30))
            self.surface.blit(text_surface, text_rect)

    def animate_nodes(self, node):
        if not node: return
        
        if node.curr_x is not None and node.target_x is not None:
            lerp_speed = 0.03 
            node.curr_x += (node.target_x - node.curr_x) * lerp_speed
            node.curr_y += (node.target_y - node.curr_y) * lerp_speed
        
        self.animate_nodes(node.vis_left)
        self.animate_nodes(node.vis_right)

    def _draw_edges(self, node):
        if not node: return
        

        if node.vis_left and not getattr(node.vis_left, 'is_hidden', False):
            if node.curr_x is not None and node.vis_left.curr_x is not None:
                pygame.draw.line(self.surface, LINE_COLOR, (node.curr_x, node.curr_y), (node.vis_left.curr_x, node.vis_left.curr_y), LINE_WIDTH)
            self._draw_edges(node.vis_left)
            
        if node.vis_right and not getattr(node.vis_right, 'is_hidden', False):
            if node.curr_x is not None and node.vis_right.curr_x is not None:
                pygame.draw.line(self.surface, LINE_COLOR, (node.curr_x, node.curr_y), (node.vis_right.curr_x, node.vis_right.curr_y), LINE_WIDTH)
            self._draw_edges(node.vis_right)

    def _draw_nodes(self, node):
        if not node: return
        
        if getattr(node, 'is_hidden', False) or node.curr_x is None:
            self._draw_nodes(node.vis_left)
            self._draw_nodes(node.vis_right)
            return
            
        is_moving = abs(node.curr_x - node.target_x) > 1 or abs(node.curr_y - node.target_y) > 1
        is_active_step = self.current_action and self.current_action.get("node") == node

        if is_active_step or is_moving:
            pygame.draw.circle(self.surface, HIGHLIGHT_COLOR, (int(node.curr_x), int(node.curr_y)), GLOW_RADIUS)
            
        pygame.draw.circle(self.surface, NODE_COLOR, (int(node.curr_x), int(node.curr_y)), NODE_RADIUS)
        

        display_val = getattr(node, 'vis_val', node.val)
        text = self.font.render(str(display_val), True, TEXT_COLOR)
        self.surface.blit(text, text.get_rect(center=(int(node.curr_x), int(node.curr_y))))
        
        self._draw_nodes(node.vis_left)
        self._draw_nodes(node.vis_right)

    def _is_any_node_moving(self, node):
        if not node: return False
        
        if getattr(node, 'is_hidden', False):
            return self._is_any_node_moving(node.vis_left) or self._is_any_node_moving(node.vis_right)

        if node.curr_x is not None and node.target_x is not None:
            if abs(node.curr_x - node.target_x) > 1 or abs(node.curr_y - node.target_y) > 1:
                return True
                
        return self._is_any_node_moving(node.vis_left) or self._is_any_node_moving(node.vis_right)

    def is_idle(self, root):
        if self.action_logs or self.action_timer > 0:
            return False
  
        if self._is_any_node_moving(self.visual_root):
            return False
        return True
    
    def play_logs(self, logs):
        self.action_logs = list(logs)
        self.current_action = None
        self.step_counter = 0
        self.action_timer = 0