"""
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""

# mycode
def ans(str, k):
    left = max_len = 0

    char_count = {}
    for right in range(len(str)):
        right_char = str[right]

        if right_char not in char_count:
            char_count[right_char] = 0
        char_count[right_char] += 1

        while len(char_count) > k:
            left_char = str[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                char_count.pop(left_char)
            left += 1

        max_len = max(right - left + 1, max_len)

    return max_len


# another sol


def ans2(str, k):
    left_index = longest_so_far = 0

    char_count = {}
    for right_index in range(len(str)):
        right_char = str[right_index]
        if right_char not in char_count:
            char_count[right_char] = 0
        char_count[right_char] += 1

        while len(char_count) > k:
            left_char = str[left_index]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                char_count.pop(left_char)
            left_index += 1

        longest_so_far = max(longest_so_far, 1 + right_index - left_index)

    return longest_so_far


# answer
def longest_substring_with_k_distinct(str, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    # in the following loop we'll try to extend the range [window_start, window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
        while len(char_frequency) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1  # shrink the window
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(
        "Length of the longest substring: "
        + str(longest_substring_with_k_distinct("araaci", 2))
    )
    print(
        "Length of the longest substring: "
        + str(longest_substring_with_k_distinct("araaci", 1))
    )
    print(
        "Length of the longest substring: "
        + str(longest_substring_with_k_distinct("cbbebi", 3))
    )


main()


"""
Time Complexity 
The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input string. 
The outer for loop runs for all characters and the inner while loop processes each character only once, therefore the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N).

Space Complexity 
The space complexity of the algorithm is O(K), as we will be storing a maximum of ‘K+1’ characters in the HashMap.
"""
