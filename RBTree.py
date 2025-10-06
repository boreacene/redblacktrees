class RBNode:
    def __init__(self, val):
        self.val = val
        self.red = False
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        colour = "Red" if self.red else "Black"
        parent_value = getattr(self.parent, "val", None)
        return f"RBNode(val: {self.val}, R/B: {colour}, parent: {parent_value})"

    @staticmethod
    def nil():
        nil_node = RBNode(None)
        nil_node.red = False
        nil_node.left = nil_node
        nil_node.right = nil_node
        nil_node.parent = nil_node
        return nil_node


class RBTree:
    def __init__(self):
        self.nil = RBNode.nil()
        self.root = self.nil
        self.root.parent = self.nil
        self.debug = False

    def _debug(self, msg):
        if not self.debug:
            return
        print(msg)

    def pretty_lines(self):
        lines = []

        def walk(node, level=0):
            if node is self.nil or node.val is None:
                return
            walk(node.right, level + 1)
            lines.append(
                " " * 4 * level
                + "> "
                + str(node.val)
                + (" [red]" if node.red else " [black]")
            )
            walk(node.left, level + 1)

        walk(self.root)
        return lines

    def pretty(self):
        s = "\n".join(self.pretty_lines())
        return s if s else "<empty>"

    def inorder(self):
        out = []

        def walk(node):
            if node is self.nil or node.val is None:
                return
            walk(node.left)
            out.append(node.val)
            walk(node.right)

        walk(self.root)
        return out

    def size(self):
        def count(node):
            if node is self.nil:
                return 0
            return 1 + count(node.left) + count(node.right)

        return count(self.root)

    def insert(self, val):
        new_node = RBNode(val)
        new_node.red = True
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.parent = self.nil

        parent = self.nil
        x = self.root
        while x is not self.nil:
            parent = x
            if val < x.val:
                x = x.left
            elif val > x.val:
                x = x.right
            else:
                return

        new_node.parent = parent
        if parent is self.nil:
            self.root = new_node
        elif val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.root.parent = self.nil
        self.root.red = False

        self._debug(f"insert {val}")
        self._debug(f"attached under {parent.val if parent is not self.nil else None}")

    def is_bst(self):
        def _ok(node, lo, hi):
            if node is self.nil:
                return True
            value = node.val
            if lo is not None and not (lo < value):
                return False
            if hi is not None and not (value < hi):
                return False
            return _ok(node.left, lo, value) and _ok(node.right, value, hi)

        return _ok(self.root, None, None)

    def rotate_left(self, x):
        if x.right is self.nil:
            return
        y = x.right
        B = y.left
        x.right = B
        if B is not self.nil:
            B.parent = x
        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        return

    def rotate_right(self, x):
        if x.left is self.nil:
            return
        y = x.left
        B = y.right
        x.left = B
        if B is not self.nil:
            B.parent = x
        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y
        return
