"""
Problem Statement 
Given a binary tree and a number āSā, 
find all paths in the tree such that the sum of all the node values of each path equals āSā. 
Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).
"""


def ans(root, sum, count=0):
    if not root:
        return 0

    new_sum = sum - root.val

    if new_sum == 0:
        count += 1

    count += (
        ans(root.left, new_sum, count)
        + ans(root.right, new_sum, count)
        + ans(root.left, sum, count)
        + ans(root.right, sum, count)
    )

    return count


# mycode
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    # TODO: Write your code here
    return find_current_count(root, S, 0)


def find_current_count(currentNode, S, count):
    if not currentNode:
        return 0

    if currentNode.val == S:
        count += 1

    return (
        count
        + find_current_count(currentNode.left, S, count)
        + find_current_count(currentNode.right, S, count)
        + find_current_count(currentNode.left, S - currentNode.val, count)
        + find_current_count(currentNode.right, S - currentNode.val, count)
    )


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(ans(root, 11)))


main()


# answer
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    return count_paths_recursive(root, S, [])


def count_paths_recursive(currentNode, S, currentPath):
    if currentNode is None:
        return 0

    # add the current node to the path
    currentPath.append(currentNode.val)
    pathCount, pathSum = 0, 0
    # find the sums of all sub-paths in the current path list
    for i in range(len(currentPath) - 1, -1, -1):
        pathSum += currentPath[i]
        # if the sum of any sub-path is equal to 'S' we increment our path count.
        if pathSum == S:
            pathCount += 1

    # traverse the left sub-tree
    pathCount += count_paths_recursive(currentNode.left, S, currentPath)
    # traverse the right sub-tree
    pathCount += count_paths_recursive(currentNode.right, S, currentPath)

    # remove the current node from the path to backtrack
    # we need to remove the current node while we are going up the recursive call stack
    del currentPath[-1]

    return pathCount


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()


"""
Time complexity 
The time complexity of the above algorithm is O(N^2) in the worst case, where āNā is the total number of nodes in the tree. 
This is due to the fact that we traverse each node once, but for every node, we iterate the current path. 
The current path, in the worst case, can be O(N) (in the case of a skewed tree). 
But, if the tree is balanced, then the current path will be equal to the height of the tree, i.e., O(logN). 
So the best case of our algorithm will be O(NlogN).

Space complexity 
The space complexity of the above algorithm will be O(N). This space will be used to store the recursion stack. 
The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
We also need O(N) space for storing the currentPath in the worst case.
Overall space complexity of our algorithm is O(N).
"""
