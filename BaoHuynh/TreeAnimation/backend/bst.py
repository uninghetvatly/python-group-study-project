from backend.node import TreeNode

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.logs = []
    def _get_snapshot(self):
        """Chụp lại cấu trúc các cạnh nối của cây tại một thời điểm cụ thể"""
        edges = {}
        vals = {}
        def traverse(n):
            if n:
                edges[n] = (n.left, n.right)
                vals[n] = n.val
                traverse(n.left)
                traverse(n.right)
        traverse(self.root)
        return {"root": self.root, "edges": edges, "vals": vals}
    def insert(self, val):
        self.logs = [] 
        if not self.root:
            self.root = TreeNode(val)
            self.logs.append((self.root, f"Cây rỗng. Đã thêm {val} làm Root.", self._get_snapshot()))
            return self.root
        
        curr = self.root
        while True:
            self.logs.append((curr, f"So sánh {val} với {curr.val}"))
            if val < curr.val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    curr.left.parent = curr
                    curr.left.is_hidden = True 
                    # THÊM SNAPSHOT
                    self.logs.append((curr.left, f"Đã thêm {val} làm con trái của {curr.val}", self._get_snapshot()))
                    return curr.left
                self.logs.append((curr, f"{val} < {curr.val}, duyệt sang TRÁI"))
                curr = curr.left
            elif val > curr.val:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    curr.right.parent = curr
                    curr.right.is_hidden = True
                    # THÊM SNAPSHOT
                    self.logs.append((curr.right, f"Đã thêm {val} làm con phải của {curr.val}", self._get_snapshot()))
                    return curr.right
                self.logs.append((curr, f"{val} > {curr.val}, duyệt sang PHẢI"))
                curr = curr.right
            else:
                self.logs.append((curr, f"Giá trị {val} đã tồn tại!"))
                return None

    def search(self, val):
        self.logs = [] 
        curr = self.root
        while curr:
            self.logs.append((curr, f"Đang kiểm tra node {curr.val}"))
            if val == curr.val:
                self.logs.append((curr, f"Đã tìm thấy giá trị {val}!"))
                return curr
            elif val < curr.val:
                self.logs.append((curr, f"{val} < {curr.val}, duyệt sang TRÁI"))
                curr = curr.left
            else:
                self.logs.append((curr, f"{val} > {curr.val}, duyệt sang PHẢI"))
                curr = curr.right
        self.logs.append((None, f"Không tìm thấy giá trị {val} trong cây."))
        return None
    
    def remove(self, val):
        self.logs = []
        self.root, _ = self._remove_node(self.root, val)

    def _remove_node(self, node, val):
        if not node:
            self.logs.append((None, f"Không tìm thấy giá trị {val} để xóa!", self._get_snapshot()))
            return None, False
            
        self.logs.append((node, f"Kiểm tra node {node.val}", self._get_snapshot()))
        
        if val < node.val:
            self.logs.append((node, f"{val} < {node.val}, duyệt TRÁI tìm node xóa", self._get_snapshot()))
            node.left, deleted = self._remove_node(node.left, val)
            if node.left: node.left.parent = node
            return node, deleted
            
        elif val > node.val:
            self.logs.append((node, f"{val} > {node.val}, duyệt PHẢI tìm node xóa", self._get_snapshot()))
            node.right, deleted = self._remove_node(node.right, val)
            if node.right: node.right.parent = node
            return node, deleted
            
        else:
            self.logs.append((node, f"Đã tìm thấy {val}! Bắt đầu quá trình xóa.", self._get_snapshot()))
            if not node.left:
                self.logs.append((node, f"Node không có con trái. Thay thế bằng con phải.", self._get_snapshot()))
                return node.right, True
            elif not node.right:
                self.logs.append((node, f"Node không có con phải. Thay thế bằng con trái.", self._get_snapshot()))
                return node.left, True
                
            self.logs.append((node, f"Node có 2 con. Đi tìm Successor (nhỏ nhất bên phải)...", self._get_snapshot()))
            temp = node.right
            
            # --- MỚI: Log tiến trình trượt xuống tìm Successor ---
            self.logs.append((temp, f"Bắt đầu từ con phải: {temp.val}", self._get_snapshot()))
            while temp.left:
                temp = temp.left
                self.logs.append((temp, f"Duyệt trái tìm node nhỏ nhất: {temp.val}", self._get_snapshot()))
            # -----------------------------------------------------
            
            self.logs.append((temp, f"Tìm thấy Successor: {temp.val}. Tiến hành hoán đổi.", self._get_snapshot()))
            
            # Backend thực hiện hoán đổi
            node.val = temp.val
            
            # Log ghi nhận việc hoán đổi (Lúc này hàm _get_snapshot đã thu thập giá trị MỚI nhờ bản sửa lỗi ở trên)
            self.logs.append((node, f"Đã cập nhật giá trị thành {temp.val}. Đi xóa Successor cũ.", self._get_snapshot()))
            
            node.right, _ = self._remove_node(node.right, temp.val)
            if node.right: node.right.parent = node
            return node, True