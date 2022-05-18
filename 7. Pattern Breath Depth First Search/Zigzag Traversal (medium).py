"""
Problem Statement 
Given a binary tree, populate an array to represent its zigzag level order traversal. 
You should populate the values of all nodes of the first level from left to right, 
then right to left for the next level and keep alternating in the same manner for the following levels.
"""


# mycode
from collections import deque
from pickle import TRUE


def ans(root):
    if not root:
        return []

    result = []
    cur_level = []
    queue = deque([root])
    cur_count, next_count = 1, 0
    l2r = True

    while queue:
        cur_node = queue.pop()
        cur_level.append(cur_node.val)
        cur_count -= 1

        if cur_node.left:
            queue.appendleft(cur_node.left)
            next_count += 1
        
        if cur_node.right:
            queue.appendleft(cur_node.right)
            next_count += 1

        if cur_count == 0:
            cur_count, next_count = next_count, 0
            l2r = not l2r
            if l2r:
                cur_level.reverse()
            result.append(cur_level)
            cur_level = []
    
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

    queue = deque()
    queue.append(root)

    flag = False
    while queue:
        current = []

        if flag:
            temp = deque()
            for i in range(len(queue)):
                current_node = queue.popleft()
                current.append(current_node.val)

                if current_node.right:
                    temp.appendleft(current_node.right)
                if current_node.left:
                    temp.appendleft(current_node.left)

            queue.extend(temp)
            flag = False

        else:
            for i in range(len(queue)):
                current_node = queue.popleft()
                current.append(current_node.val)

                if current_node.right:
                    queue.append(current_node.right)
                if current_node.left:
                    queue.append(current_node.left)
            flag = True

        result.append(current)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(ans(root)))


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
    leftToRight = True
    while queue:
        levelSize = len(queue)
        currentLevel = deque()
        for _ in range(levelSize):
            currentNode = queue.popleft()

            # add the node to the current level based on the traverse direction
            if leftToRight:
                currentLevel.append(currentNode.val)
            else:
                currentLevel.appendleft(currentNode.val)

            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.append(list(currentLevel))
        # reverse the traversal direction
        leftToRight = not leftToRight

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


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
