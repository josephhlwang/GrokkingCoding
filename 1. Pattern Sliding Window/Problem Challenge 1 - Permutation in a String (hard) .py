"""
Problem Challenge 1

Permutation in a String (hard) 
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""


def ans(str, pattern):
    left = match = 0
    char_freq = {}

    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1

    for right in range(len(str)):
        right_char = str[right]
        if right_char in char_freq:

            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                match += 1

        if match == len(char_freq):
            return True

        if right >= len(pattern) - 1:
            print(left, right)
            left_char = str[left]
            left += 1
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    match -= 1
                char_freq[left_char] += 1

    return False


# mycode
def find_permutation(str, pattern):
    # TODO: Write your code here
    p_dict = {}
    s_dict = {}
    for p in pattern:
        if p not in p_dict:
            p_dict[p] = 1
        else:
            p_dict[p] += 1

    for s in range(len(str)):
        if s < len(pattern):
            if str[s] not in s_dict:
                s_dict[str[s]] = 1
            else:
                s_dict[str[s]] += 1

        else:
            if s_dict[str[s - len(pattern)]] == 1:
                del s_dict[str[s - len(pattern)]]
            else:
                s_dict[str[s - len(pattern)]] -= 1

            if str[s] not in s_dict:
                s_dict[str[s]] = 1
            else:
                s_dict[str[s]] += 1

        if s_dict == p_dict:
            return True
    return False


# answer
def find_permutation(str, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # our goal is to match all the characters from the 'char_frequency' with the current window
    # try to extend the range [window_start, window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
            # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

        # shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False


def main():
    print("Permutation exist: " + str(ans("oidbcaf", "abc")))
    print("Permutation exist: " + str(ans("odicf", "dc")))
    print("Permutation exist: " + str(ans("bcdxabcdy", "bcdyabcdx")))
    print("Permutation exist: " + str(ans("aaacb", "abc")))


main()


# Time Complexity #
# The time complexity of the above algorithm will be O(N + M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

# Space Complexity #
# The space complexity of the algorithm is O(M) since in the worst case,
# the whole pattern can have distinct characters which will go into the HashMap.
