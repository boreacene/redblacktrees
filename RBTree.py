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
