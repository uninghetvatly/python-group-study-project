from backend.bst import BinarySearchTree

class AVLTree(BinarySearchTree):
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2

        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
            
        y.parent = x
        if T2: T2.parent = y

        self.update_height(y)
        self.update_height(x)
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
            
        x.parent = y
        if T2: T2.parent = x

        self.update_height(x)
        self.update_height(y)
        return y


    def insert(self, val):
        new_node = super().insert(val)
        if not new_node:
            return None

        curr = new_node.parent
        while curr:
            self.update_height(curr)
            balance = self.get_balance(curr)

            # --- SINGLE ROTATIONS ---
            if balance > 1 and val < curr.left.val:
                self.right_rotate(curr)
                self.logs.append((curr.parent, f"Mất cân bằng (Left-Left) tại {curr.val}. Xoay PHẢI.", self._get_snapshot()))
            elif balance < -1 and val > curr.right.val:
                self.left_rotate(curr)
                self.logs.append((curr.parent, f"Mất cân bằng (Right-Right) tại {curr.val}. Xoay TRÁI.", self._get_snapshot()))
            
            # --- DOUBLE ROTATIONS (ĐƯỢC TÁCH THÀNH 2 BƯỚC) ---
            elif balance > 1 and val > curr.left.val:
                self.left_rotate(curr.left)
                self.logs.append((curr.left, f"Mất cân bằng (Left-Right). BƯỚC 1: Xoay TRÁI nhánh con.", self._get_snapshot()))
                self.right_rotate(curr)
                self.logs.append((curr.parent, f"Xoay PHẢI nhánh cha để hoàn tất.", self._get_snapshot()))
            
            elif balance < -1 and val < curr.right.val:
                self.right_rotate(curr.right)
                self.logs.append((curr.right, f"Mất cân bằng (Right-Left). BƯỚC 1: Xoay PHẢI nhánh con.", self._get_snapshot()))
                self.left_rotate(curr)
                self.logs.append((curr.parent, f"Xoay TRÁI nhánh cha để hoàn tất.", self._get_snapshot()))
                
            curr = curr.parent
        return new_node
    
    def remove(self, val):
        self.logs = []
        self.root = self._delete_recursive(self.root, val)

    def _get_min_value_node(self, node):
        if node is None or node.left is None: return node
        return self._get_min_value_node(node.left)

    def _delete_recursive(self, root, val):
        if not root: return root
        
        self.logs.append((root, f"Kiểm tra node {root.val} để xóa/cân bằng", self._get_snapshot()))
        
        if val < root.val:
            self.logs.append((root, f"{val} < {root.val}, duyệt TRÁI", self._get_snapshot()))
            root.left = self._delete_recursive(root.left, val)
            if root.left: root.left.parent = root
        elif val > root.val:
            self.logs.append((root, f"{val} > {root.val}, duyệt PHẢI", self._get_snapshot()))
            root.right = self._delete_recursive(root.right, val)
            if root.right: root.right.parent = root
        else:
            self.logs.append((root, f"Đã tìm thấy {root.val}! Chuẩn bị xóa.", self._get_snapshot()))
            if root.left is None: 
                self.logs.append((root, f"Thay thế bằng con phải.", self._get_snapshot()))
                return root.right
            elif root.right is None: 
                self.logs.append((root, f"Thay thế bằng con trái.", self._get_snapshot()))
                return root.left
                
            temp = self._get_min_value_node(root.right)
            self.logs.append((temp, f"Successor là {temp.val}. Hoán đổi giá trị.", self._get_snapshot()))
            root.val = temp.val
            self.logs.append((root, f"Đã hoán đổi giá trị. Đi xóa Successor ở dưới.", self._get_snapshot()))
            root.right = self._delete_recursive(root.right, temp.val)
            if root.right: root.right.parent = root

        if root is None: return root

        self.update_height(root)
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            new_root = self.right_rotate(root)
            self.logs.append((new_root, f"Mất cân bằng (Left-Left) sau xóa. Xoay PHẢI.", self._get_snapshot()))
            return new_root
            
        if balance < -1 and self.get_balance(root.right) <= 0:
            new_root = self.left_rotate(root)
            self.logs.append((new_root, f"Mất cân bằng (Right-Right) sau xóa. Xoay TRÁI.", self._get_snapshot()))
            return new_root
            
        # DOUBLE ROTATION SAU KHI XÓA
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            self.logs.append((root.left, f"Mất cân bằng (Left-Right) sau xóa. BƯỚC 1: Xoay TRÁI nhánh con.", self._get_snapshot()))
            new_root = self.right_rotate(root)
            self.logs.append((new_root, f"Xoay PHẢI nhánh cha để hoàn tất.", self._get_snapshot()))
            return new_root
            
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            self.logs.append((root.right, f"Mất cân bằng (Right-Left) sau xóa. BƯỚC 1: Xoay PHẢI nhánh con.", self._get_snapshot()))
            new_root = self.left_rotate(root)
            self.logs.append((new_root, f"Xoay TRÁI nhánh cha để hoàn tất.", self._get_snapshot()))
            return new_root

        return root