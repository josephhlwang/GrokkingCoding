"""
Problem Statement 
Given a binary tree, populate an array to represent the averages of all of its levels.
"""

# mycode
from collections import deque


def ans(root):

    if not root:
        return []

    cur_level, next_level, cur_sum, cur_total = 1, 0, 0, 1

    result = []
    queue = deque([root])

    while queue:
        cur_node = queue.popleft()
        cur_sum += cur_node.val
        cur_level -= 1

        if cur_node.left:
            queue.append(cur_node.left)
            next_level += 1

        if cur_node.right:
            queue.append(cur_node.right)
            next_level += 1

        if cur_level == 0:
            result.append(cur_sum / cur_total)
            cur_level, next_level, cur_sum, cur_total = next_level, 0, 0, next_level

    return result


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    # TODO: Write your code here
    if not root:
        return result
    queue = deque()
    queue.append(root)

    while queue:
        value = 0
        n = len(queue)
        for i in range(n):
            current = queue.popleft()
            value += current.val

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        result.append(value / n)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(ans(root)))


main()


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        levelSum = 0.0
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add the node's value to the running sum
            levelSum += currentNode.val
            # insert the children of current node to the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        # append the current level's average to the result array
        result.append(levelSum / levelSize)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


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
