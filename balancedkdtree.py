# KD TREE BALANCED
import math

class Node:
    def _init_(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

class KDTree:
    def _init_(self, points=None):
        self.root = None
        if points:
            self.root = self._build_balanced(points)

    def _build_balanced(self, points, depth=0):
        if not points:
            return None

        k = len(points[0])
        axis = depth % k

        sorted_points = sorted(points, key=lambda p: p[axis])
        median_idx = len(sorted_points) // 2
        median = sorted_points[median_idx]

        left_points = sorted_points[:median_idx]
        right_points = sorted_points[median_idx+1:]

        return Node(
            median,
            self._build_balanced(left_points, depth + 1),
            self._build_balanced(right_points, depth + 1)
        )

# Example usage
if _name_ == "_main_":
    points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]

    kdtree = KDTree(points)
    
    print("____")
    # Print the tree structure (inorder traversal)
    def print_tree(node):
        if node is None:
            return
        print_tree(node.left)
        print(node.point)
        print_tree(node.right)

    print("Tree structure:")
    print_tree(kdtree.root)