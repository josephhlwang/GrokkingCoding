"""
Problem Statement 
Find the minimum depth of a binary tree. 
The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
"""

# mycode
from collections import deque


def ans(root):
    if not root:
        return None

    cur_level, next_level, depth = 1, 0, 1

    queue = deque([root])

    while queue:
        cur_node = queue.popleft()
        cur_level -= 1

        if not cur_node.left and not cur_node.right:
            return depth

        if cur_node.left:
            queue.append(cur_node.left)
            next_level += 1

        if cur_node.right:
            queue.append(cur_node.right)
            next_level += 1

        if cur_level == 0:
            cur_level, next_level = next_level, 0
            depth += 1

    return None


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    # TODO: Write your code here
    if not root:
        return 0

    queue = deque()
    queue.append(root)

    depth = 0

    while queue:
        depth += 1

        for i in range(len(queue)):
            current = queue.popleft()

            if current.left is None and current.right is None:
                return depth
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    print("Tree Minimum Depth(Me): " + str(ans(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    print("Tree Minimum Depth(Me): " + str(ans(root)))


main()


# answer
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    minimumTreeDepth = 0
    while queue:
        minimumTreeDepth += 1
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()

            # check if this is a leaf node
            if not currentNode.left and not currentNode.right:
                return minimumTreeDepth

            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()


"""
Time complexity 
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. 
This is due to the fact that we traverse each node once.

Space complexity 
The space complexity of the above algorithm will be O(N)O which is required for the queue. 
Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), 
therefore we will need O(N) space to store them in the queue.
"""

"""
Similar Problems 

Problem 1: Given a binary tree, find its maximum depth (or height).

Solution: We will follow a similar approach. Instead of returning as soon as we find a leaf node, 
we will keep traversing for all the levels, incrementing maximumDepth each time we complete a level. 
Here is what the code will look like:
"""


from collections import deque


def ans_max(root):

    if not root:
        return None

    queue = deque([root])
    cur_level, next_level, depth = 1, 0, 1
    max_level = 1

    while queue:

        cur_node = queue.popleft()
        cur_level -= 1

        if not cur_node.left and not cur_node.right:
            max_level = depth

        if cur_node.left:
            queue.append(cur_node.left)
            next_level += 1

        if cur_node.right:
            queue.append(cur_node.right)
            next_level += 1

        if cur_level == 0:
            cur_level, next_level = next_level, 0
            depth += 1

    return max_level


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_maximum_depth(root):
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    maximumTreeDepth = 0
    while queue:
        maximumTreeDepth += 1
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()

            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

    return maximumTreeDepth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Maximum Depth: " + str(find_maximum_depth(root)))
    print("Tree Maximum Depth(Me): " + str(ans_max(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Maximum Depth: " + str(find_maximum_depth(root)))
    print("Tree Maximum Depth(Me): " + str(ans_max(root)))


main()
