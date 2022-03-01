"""
Problem Challenge 1

Tree Diameter (medium)

Given a binary tree, find the length of its diameter. 
The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. 
The diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.
"""


def ans(root):
    max_diam = [0]
    find_diam(root, max_diam)
    return max_diam[0]


def find_diam(root, max_diam):
    if root == None:
        return

    left_height = find_height(root.left)
    right_height = find_height(root.right)

    diam = 1 + left_height + right_height
    max_diam[0] = max(diam, max_diam[0])

    find_diam(root.left, max_diam)
    find_diam(root.right, max_diam)


def find_height(root):
    if root == None:
        return 0

    return 1 + max(find_height(root.left), find_height(root.right))


# mycode
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:
    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):
        # TODO: Write your code here
        def depth(currentNode):
            if not currentNode:
                return 0

            left = depth(currentNode.left)
            right = depth(currentNode.right)

            self.treeDiameter = max(self.treeDiameter, left + right + 1)
            return 1 + max(left, right)

        depth(root)
        return self.treeDiameter


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(ans(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(ans(root)))


main()


# answer
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:
    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):
        self.calculate_height(root)
        return self.treeDiameter

    def calculate_height(self, currentNode):
        if currentNode is None:
            return 0

        leftTreeHeight = self.calculate_height(currentNode.left)
        rightTreeHeight = self.calculate_height(currentNode.right)

        # diameter at the current node will be equal to the height of left subtree +
        # the height of right sub-trees + '1' for the current node
        diameter = leftTreeHeight + rightTreeHeight + 1

        # update the global tree diameter
        self.treeDiameter = max(self.treeDiameter, diameter)

        # height of the current node will be equal to the maximum of the hights of
        # left or right subtrees plus '1' for the current node
        return max(leftTreeHeight, rightTreeHeight) + 1


def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()


"""
Time complexity 
The time complexity of the above algorithm is O(N)O(N), where ‘N’ is the total number of nodes in the tree. 
This is due to the fact that we traverse each node once.

Space complexity 
The space complexity of the above algorithm will be O(N) in the worst case. 
This space will be used to store the recursion stack. 
The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
"""
