# UNBALANCED KD TREE

import sys

# Number of dimensions
k = 2

# A structure to represent node of kd tree
class Node:
	def __init__(self, point):
		self.point = point
		self.left = None
		self.right = None

    # A method to create a node of K D tree
    def newNode(point):
        return Node(point)

    # Inserts a new node and returns root of modified tree
    # The parameter depth is used to decide axis of comparison
    def insertRec(root, point, depth):
        # Tree is empty?
        if not root:
            return newNode(point)

        # Calculate current dimension (cd) of comparison
        cd = depth % k

        # Compare the new point with root on current dimension 'cd'
        # and decide the left or right subtree
        if point[cd] < root.point[cd]:
            root.left = insertRec(root.left, point, depth + 1)
        else:
            root.right = insertRec(root.right, point, depth + 1)

        return root

    # Function to insert a new point with given point in
    # KD Tree and return new root. It mainly uses above recursive
    # function "insertRec()"
    def insert(root, point):
        return insertRec(root, point, 0)

if __name__ == '__main__':
	root = None
	points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]

	n = len(points)

	for i in range(n):
		root = insert(root, points[i])