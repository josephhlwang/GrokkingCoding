"""
Problem Statement 
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, 
hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; 
and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

Example 1:

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]

Example 2:

Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]
"""


def ans(arr):
    i = z = 0
    t = len(arr) - 1

    while i <= t:
        num = arr[i]
        if num == 0:
            swap(arr, i, z)
            z += 1
            i += 1
        elif num == 2:
            swap(arr, i, t)
            t -= 1
        else:
            i += 1
    return arr


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# mycode
def dutch_flag_sort(arr):
    # TODO: Write your code here
    left, i = 0, 0
    right = len(arr) - 1

    while i <= right:
        if arr[i] == 0:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
            i += 1
        elif arr[i] == 2:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        else:
            i += 1

    return


def main():
    x = [1, 0, 2, 1, 0]
    y = [2, 2, 0, 1, 2, 0]
    print(ans(x))
    print("Sol:", [0, 0, 1, 1, 2])

    print(ans(y))
    print("Sol:", [0, 0, 1, 2, 2, 2])


main()

"""
Time complexity 
The time complexity of the above algorithm will be O(N) as we are iterating the input array only once.

Space complexity #
The algorithm runs in constant space O(1).
"""
