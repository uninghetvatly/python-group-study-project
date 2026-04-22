import pygame
import pygame_gui
import sys
from frontend.constants import *
from backend.avl import AVLTree
from backend.bst import BinarySearchTree
from backend.splay import SplayTree
from frontend.visualizer import TreeVisualizer

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    manager = pygame_gui.UIManager((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("tahoma", 16)

    
    # 1. Dropdown chọn cây
    tree_dropdown = pygame_gui.elements.UIDropDownMenu(
        options_list=["AVL", "BST", "Splay"],
        starting_option="AVL",
        relative_rect=pygame.Rect((20, 710), (100, 30)),
        manager=manager
    )

    # 2. Nút Clear Tree
    clear_btn = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((130, 710), (80, 30)),
        text="Clear",
        manager=manager
    )

    # 3. Input Insert Array
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((220, 710), (90, 30)), text="Insert:", manager=manager)
    array_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((310, 710), (130, 30)), manager=manager)

    # 4. Input Delete
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((450, 710), (70, 30)), text="Delete:", manager=manager)
    delete_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((520, 710), (70, 30)), manager=manager)

    # 5. Input Find (Tìm kiếm)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((600, 710), (50, 30)), text="Find:", manager=manager)
    find_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((650, 710), (70, 30)), manager=manager)


    # ==========================================
    # --- KHỞI TẠO BACKEND VÀ FRONTEND ---
    # ==========================================
    current_tree = AVLTree()
    visualizer = TreeVisualizer(screen, font)
    pending_inserts = []
    
    # Hàm reset cây dùng chung cho nút Clear và Dropdown
    def reset_tree(tree_type):
        nonlocal current_tree
        
        # Ép kiểu về chuỗi (string) để chống lỗi của pygame_gui
        t_type = str(tree_type)
        
        # Dùng toán tử "in" thay vì "==" để bắt chữ cho chuẩn
        if "AVL" in t_type:
            current_tree = AVLTree()
        elif "BST" in t_type:
            current_tree = BinarySearchTree()
        elif "Splay" in t_type:
            current_tree = SplayTree()
        else:
            # Fallback: Nếu không đọc được dropdown, thì reset lại chính cây hiện tại
            if isinstance(current_tree, AVLTree): current_tree = AVLTree()
            elif isinstance(current_tree, SplayTree): current_tree = SplayTree()
            else: current_tree = BinarySearchTree()
            
        pending_inserts.clear()          
        visualizer.clear()

    # ==========================================
    # --- VÒNG LẶP CHÍNH (GAME LOOP) ---
    # ==========================================
    while True:
        time_delta = clock.tick(FPS)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            manager.process_events(event)
            
            # XỬ LÝ SỰ KIỆN NÚT BẤM (BUTTON)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == clear_btn:
                    reset_tree(tree_dropdown.selected_option)

            # XỬ LÝ SỰ KIỆN DROPDOWN
            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == tree_dropdown:
                    reset_tree(event.text)

            # XỬ LÝ SỰ KIỆN NHẬP TEXT XONG (NHẤN ENTER)
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                
                # Chèn mảng
                if event.ui_element == array_entry:
                    try:
                        vals = [int(x.strip()) for x in event.text.replace(',', ' ').split()]
                        pending_inserts.extend(vals)
                        array_entry.set_text("") 
                    except ValueError: pass

                # Xóa 1 Node
                if event.ui_element == delete_entry:
                    try:
                        val = int(event.text)
                        if hasattr(current_tree, 'remove'): 
                            current_tree.remove(val)
                            visualizer.play_logs(current_tree.logs)
                        delete_entry.set_text("")
                    except ValueError: pass
                    
                # Tìm kiếm (Find)
                if event.ui_element == find_entry:
                    try:
                        val = int(event.text)
                        if hasattr(current_tree, 'search'): 
                            current_tree.search(val)
                            visualizer.play_logs(current_tree.logs)
                        find_entry.set_text("")
                    except ValueError: pass

        # --- LOGIC ĐỒNG BỘ ANIMATION CHỜ ---
        current_root = current_tree.root if hasattr(current_tree, 'root') else None
        is_visualizer_idle = visualizer.is_idle(current_root)

        # Trích xuất số từ hàng đợi nếu màn hình đang rảnh
        if is_visualizer_idle and pending_inserts:
            next_val = pending_inserts.pop(0) 
            current_tree.insert(next_val)     
            visualizer.play_logs(current_tree.logs)

        # --- CẬP NHẬT GIAO DIỆN ---
        manager.update(time_delta)
        screen.fill(BACKGROUND_COLOR)
        
        visualizer.draw_tree(current_tree.root if hasattr(current_tree, 'root') else None)
        
        manager.draw_ui(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()