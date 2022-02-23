"""
Problem Statement 
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""

# answer
from collections import deque


def ans(root):
    queue = deque()
    queue.append(root)
    result = []
    cur_vals = []
    cur_level, next_level = 1, 0
    while len(queue):
        cur = queue.popleft()
        cur_vals.append(cur.val)
        cur_level -= 1
        if cur.left:
            queue.append(cur.left)
            next_level += 1
        if cur.right:
            queue.append(cur.right)
            next_level += 1
        if cur_level == 0:
            result.append(cur_vals)
            cur_vals = []
            cur_level, next_level = next_level, 0

    return result


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    # TODO: Write your code here
    if not root:
        return result
    stack = [root]
    value = [[root.val]]
    while stack:
        current = []
        current_val = []
        for i in stack:
            current_val.append(i.val)
            if i.left:
                current.append(i.left)
            if i.right:
                current.append(i.right)
        result.append(current_val)
        stack = current
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(ans(root)))


main()


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add the node to the current level
            currentLevel.append(currentNode.val)
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.append(currentLevel)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()


"""
Time complexity 
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. 
This is due to the fact that we traverse each node once.

Space complexity 
The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal. 
We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), 
therefore we will need O(N) space to store them in the queue.
"""
