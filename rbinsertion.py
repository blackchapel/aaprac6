class Node:
    def __init__(self, key, parent=None, color="Red"):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)

        if self.root is None:
            self.root = new_node
            self.root.color = "Black"
            return

        current = self.root
        while current:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self.insert_fixup(new_node)

    def insert_fixup(self, node):
        while node.parent and node.parent.color == "Red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == "Red":
                    node.parent.color = "Black"
                    uncle.color = "Black"
                    node.parent.parent.color = "Red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "Black"
                    node.parent.parent.color = "Red"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == "Red":
                    node.parent.color = "Black"
                    uncle.color = "Black"
                    node.parent.parent.color = "Red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "Black"
                    node.parent.parent.color = "Red"
                    self.left_rotate(node.parent.parent)

        self.root.color = "Black"

    def left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left:
            right_child.left.parent = node
        right_child.parent = node.parent
        if not node.parent:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right:
            left_child.right.parent = node
        left_child.parent = node.parent
        if not node.parent:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)


# Example usage
if __name__ == "__main__":
    rb_tree = RedBlackTree()

    keys = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13]
    for key in keys:
        rb_tree.insert(key)

    print("Inorder Traversal of the Red-Black Tree:")
    rb_tree.inorder_traversal(rb_tree.root)

