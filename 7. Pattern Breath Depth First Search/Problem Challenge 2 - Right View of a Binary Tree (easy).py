"""
Problem Challenge 2

Right View of a Binary Tree (easy)

Given a binary tree, return an array containing nodes in its right view. 
The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
"""


# mycode
from __future__ import print_function
from collections import deque


def ans(root):
    if not root:
        return []

    queue = deque([root])
    cur_count, next_count = 1, 0
    result = []

    while queue:
        cur_node = queue.pop()
        cur_count -= 1

        if cur_node.left:
            queue.appendleft(cur_node.left)
            next_count += 1

        if cur_node.right:
            queue.appendleft(cur_node.right)
            next_count += 1

        cur_node.next = None if not queue else queue[-1]

        if cur_count == 0:
            result.append(cur_node)
            cur_count, next_count = next_count, 0

    return result


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    result = []
    # TODO: Write your code here
    if not root:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        for i in range(len(queue)):

            current = queue.popleft()

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        result.append(current)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = ans(root)
    print("Tree right view: ", end="")
    for node in result:
        print(str(node.val) + " ", end="")


main()


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        for i in range(0, levelSize):
            currentNode = queue.popleft()
            # if it is the last node of this level, add it to the result
            if i == levelSize - 1:
                result.append(currentNode)
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end="")


main()


"""
Time complexity #
The time complexity of the above algorithm is O(N), where ???N??? is the total number of nodes in the tree. 
This is due to the fact that we traverse each node once.

Space complexity 
The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal. 
We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level 
(this could happen only at the lowest level), therefore we will need O(N) space to store them in the queue.
"""

"""
Similar Questions #
Problem 1: Given a binary tree, return an array containing nodes in its left view. 
The left view of a binary tree is the set of nodes visible when the tree is seen from the left side.

Solution: We will be following a similar approach, 
but instead of appending the last element of each level we will be appending the first element of each level to the output array.
"""
