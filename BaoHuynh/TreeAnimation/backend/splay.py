from backend.bst import BinarySearchTree

class SplayTree(BinarySearchTree):
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left: y.left.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right: y.right.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.right: x.parent.right = y
        else: x.parent.left = y
        y.right = x
        x.parent = y

    def _splay(self, node):
        while node.parent:
            if not node.parent.parent:
                # Zig step (Chỉ xoay 1 lần)
                if node == node.parent.left:
                    self._right_rotate(node.parent)
                    self.logs.append((node, f"Splay (Zig): Xoay PHẢI đẩy {node.val} lên.", self._get_snapshot()))
                else:
                    self._left_rotate(node.parent)
                    self.logs.append((node, f"Splay (Zag): Xoay TRÁI đẩy {node.val} lên.", self._get_snapshot()))
            elif node == node.parent.left and node.parent == node.parent.parent.left:
                # Zig-Zig step (Xoay ông nội rồi xoay cha)
                self._right_rotate(node.parent.parent)
                self.logs.append((node.parent, f"Splay (Zig-Zig) Bước 1: Xoay PHẢI ông nội.", self._get_snapshot()))
                self._right_rotate(node.parent)
                self.logs.append((node, f"Splay (Zig-Zig) Bước 2: Xoay PHẢI cha.", self._get_snapshot()))
            elif node == node.parent.right and node.parent == node.parent.parent.right:
                # Zag-Zag step
                self._left_rotate(node.parent.parent)
                self.logs.append((node.parent, f"Splay (Zag-Zag) Bước 1: Xoay TRÁI ông nội.", self._get_snapshot()))
                self._left_rotate(node.parent)
                self.logs.append((node, f"Splay (Zag-Zag) Bước 2: Xoay TRÁI cha.", self._get_snapshot()))
            else:
                # Zig-Zag step (Xoay con rồi xoay cha)
                if node == node.parent.left:
                    self._right_rotate(node.parent)
                    self.logs.append((node, f"Splay (Zig-Zag) Bước 1: Xoay PHẢI cha.", self._get_snapshot()))
                    self._left_rotate(node.parent)
                    self.logs.append((node, f"Splay (Zig-Zag) Bước 2: Xoay TRÁI ông nội.", self._get_snapshot()))
                else:
                    self._left_rotate(node.parent)
                    self.logs.append((node, f"Splay (Zag-Zig) Bước 1: Xoay TRÁI cha.", self._get_snapshot()))
                    self._right_rotate(node.parent)
                    self.logs.append((node, f"Splay (Zag-Zig) Bước 2: Xoay PHẢI ông nội.", self._get_snapshot()))

    def insert(self, val):
        new_node = super().insert(val)
        if new_node:
            self.logs.append((new_node, f"Bắt đầu Splay node {new_node.val} lên Root.", self._get_snapshot()))
            self._splay(new_node)
            self.logs.append((new_node, f"Hoàn tất! {new_node.val} hiện là Root.", self._get_snapshot()))
        return new_node

    def search(self, val):
        node = super().search(val)
        if node:
            self.logs.append((node, f"Tìm thấy {node.val}, chuẩn bị Splay lên Root.", self._get_snapshot()))
            self._splay(node)
            self.logs.append((node, f"Hoàn tất Splay sau khi tìm kiếm.", self._get_snapshot()))
        return node
    
    def remove(self, val):
        if not self.root:
            return
            
        node = self.search(val)
        if not node or node.val != val:
            return  # Value not found

        # Nhờ hàm search ở trên, node cần xóa đã splay lên Root rồi
        self.logs.append((self.root, f"Chuẩn bị cắt Root {val} khỏi cây...", self._get_snapshot()))
        
        left_tree = self.root.left
        right_tree = self.root.right

        if left_tree: left_tree.parent = None
        if right_tree: right_tree.parent = None

        if not left_tree:
            self.root = right_tree
            self.logs.append((self.root, f"Cây con trái rỗng. Cây con phải thành Root mới.", self._get_snapshot()))
        else:
            self.root = left_tree
            self.logs.append((self.root, f"Tách cây trái. Đi tìm Max của cây trái...", self._get_snapshot()))
            
            # Đi tìm Max ở cây bên trái
            curr = left_tree
            self.logs.append((curr, f"Bắt đầu từ: {curr.val}", self._get_snapshot()))
            while curr.right:
                curr = curr.right
                self.logs.append((curr, f"Duyệt phải tìm Max: {curr.val}", self._get_snapshot()))
                
            self.logs.append((curr, f"Max là {curr.val}. Splay lên làm Root mới...", self._get_snapshot()))
            self._splay(curr)
            
            # Root mới giờ là `curr`. Gắn nhánh phải vào.
            self.root = curr
            self.root.right = right_tree
            if right_tree:
                right_tree.parent = self.root
            self.logs.append((self.root, f"Gắn nhánh phải cũ vào Root mới. Xóa hoàn tất!", self._get_snapshot()))