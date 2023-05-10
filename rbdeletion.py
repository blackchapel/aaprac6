class Node:
    def __init__(self, data=-1, left=None, right=None, color='R'):
        self.data = data
        self.left = left
        self.right = right
        self.color = color

def case0(root, val):
    if root.left.data == val and root.left.color == 'R':
        root.left = Node(-1, None, None, 'B')
    elif root.right.data == val and root.right.color == 'R':
        root.right = Node(-1, None, None, 'B')
    return root

def case1(root):
    if root.color == 'D':
        root.color = 'B'
    return root

def case2(root, val):
    double_black = root.left if root.left.color == 'D' else root.right
    sibling = root.right if double_black == root.left else root.left
    new_root = root
    if sibling.color == 'R':
        if sibling == root.left:
            new_root = right_rotate(root)
        else:
            new_root = left_rotate(root)
        root.color = 'R'
        sibling.color = 'B'
    return new_root

def case3(root, val):
    double_black = root.left if root.left.color == 'D' else root.right
    sibling = root.right if double_black == root.left else root.left
    new_root = root
    if (
        root.color == 'B' and sibling.color == 'B' and
        sibling.left is not None and sibling.left.color == 'B' and
        sibling.right is not None and sibling.right.color == 'B'
    ):
        root.color = 'D'
        sibling.color = 'R'
        double_black.color = 'B'
        return new_root

def case4(root, val):
    double_black = root.left if root.left.color == 'D' else root.right
    sibling = root.right if double_black == root.left else root.left
    new_root = root
    if (
        root.color == 'R' and sibling.color == 'B' and
        sibling.left is not None and sibling.left.color == 'B' and
        sibling.right is not None and sibling.right.color == 'B'
    ):
        root.color = 'B'
        sibling.color = 'R'
        double_black.color = 'B'
    return new_root

def case5(root, val):
    double_black = root.left if root.left.color == 'D' else root.right
    sibling = root.right if double_black == root.left else root.left
    inner = sibling.left if double_black == root.left else sibling.right
    outer = sibling.right if inner == sibling.left else sibling.left
    new_root = root
    if (
        root.color == 'B' and sibling.color == 'B' and
        inner.color == 'R' and outer.color == 'B'
    ):
        if inner == sibling.left:
            root.right = right_rotate(sibling)
        else:
            root.left = left_rotate(sibling)
        sibling.color = 'R'
        inner.color = 'B'
    return new_root

def case6(root, val):
    double_black = root.left if root.left.color == 'D' else root.right
    sibling = root.right if double_black == root.left else root.left
    inner = sibling.left if double_black == root.left else sibling.right
    outer = sibling.right if inner == sibling.left else sibling.left
    new_root = root
    if root.color == 'B' and outer.color == 'R':
        if inner == sibling.left:
            root.right = right_rotate(sibling)
        else:
            root.left = left_rotate(sibling)
        root.color = 'B'
        double_black.color = 'B'
        sibling.color = 'C'
        inner.color = 'C'
        outer.color = 'B'
    return new_root

def left_rotate(node):
    x = node.right
    y = x.left
    x.left = node
    node.right = y
    return x

def right_rotate(node):
    x = node.left
    y = x.right
    x.right = node
    node.left = y
    return x

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, node.color, end=' ')
    inorder(node.right)

if __name__ == '__main__':
    root = Node(
        10,
        Node(5, Node(-1, None, None, 'B'), Node(-1, None, None, 'B'), 'R'),
        Node(12, Node(-1, None, None, 'B'), Node(-1, None, None, 'B'), 'R'),
        'B'
    )
    print("case 0")
    print("before deletion:")
    inorder(root)
    root = case0(root, 12)
    print()
    print("case 1")
    print("after deletion:")
    inorder(root)
    root = Node(
        10,
        Node(5, Node(-1, None, None, 'B'), Node(-1, None, None, 'B'), 'R'),
        Node(12, Node(-1, None, None, 'B'), Node(-1, None, None, 'B'), 'D'),
        'D'
    )
    print("case 1: before deletion")
    inorder(root)
    root = case1(root)
    print("after deletion:")
    inorder(root)
    print("case 2")
    root = Node(
        20,
        Node(
            10,
            Node(-1, None, None, 'B'),
            Node(-1, None, None, 'B'),
            'B'
        ),
        Node(
            25,
            Node(-1, None, None, 'B'),
            Node(-1, None, None, 'B'),
            'R'
        ),
        'B'
    )
    print("before deletion")
    inorder(root)
    root = case2(root, 10)
    print("after deletion")
    inorder(root)
    print("case 3")
    root = Node(
        20,
        Node(
            10,
            Node(-1, None, None, 'B'),
            Node(-1, None, None, 'B'),
            'B'
        ),
        Node(
            25,
            Node(-1, None, None, 'B'),
            Node(-1, None, None, 'B'),
            'B'
        ),
        'B'
    )
    print("before deletion")
    inorder(root)
    root = case3(root, 10)
    print("after deletion")
    inorder(root)
    print("case 4")
    root = Node(
        20,
        Node(
            10,
            Node(-1, None, None, 'B'),
            Node(-1, None, None, 'B'),
            'B'
        ),
        Node(
            25,
            Node(-1, None, None, 'B'),
            Node(-1, None, None, 'B'),
            'R'
        ),
        'R'
    )
    print("before deletion")
    inorder(root)
    root = case4(root, 10)
    print("after deletion")
    inorder(root)
    print("case 5")
    root = Node(
        20,
        Node(
            10,
            Node(-1, None, None, 'B'),
            Node(-1, None, None, 'B'),
            'B'
        ),
        Node(
            25,
            None,
            None,
            'B'
        ),
        'B'
    )
    root.right.left = Node(21, Node(-1, None, None, 'B'), Node(-1, None, None, 'B'), 'R')
    root.right.right = Node(30, Node(-1, None, None, 'B'), Node(-1, None, None, 'B'), 'B')
    print("before deletion")
    inorder(root)
    root = case5(root, 10)
    print("after deletion")
    inorder(root)
    print("case 6")
    root = Node(
        20,
        Node(
            10,
            Node(-1, None, None, 'B'),
            Node(-1, None, None, 'B'),
            'C'
        ),
        Node(
            25,
            None,
            None,
            'B'
        ),
        'C'
    )
    root.right.left = Node(21, Node(-1, None, None, 'B'), Node(-1, None, None, 'B'), 'C')
    root.right.right = Node(30, Node(-1, None, None, 'B'), Node(-1, None, None, 'B'), 'R')
    print("before deletion")
    inorder(root)
    root = case6(root, 10)
    print("after deletion")
    inorder(root)
