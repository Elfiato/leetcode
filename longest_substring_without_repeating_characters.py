'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string s, find the length of the longest substring without repeating characters.
Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''


class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        sub, max_sub = '', ''
        for i in s:
            if i not in sub:
                sub += i
            else:
                if len(sub) > len(max_sub):
                    max_sub = sub
                sub = sub[(len(sub) - (sub[::-1].index(i))):] + i
        if len(sub) > len(max_sub):
            max_sub = sub
        print(max_sub)
        return len(max_sub)


if __name__ == '__main__':
    assert Solution.length_of_longest_substring("abcabcbb") == 3
    assert Solution.length_of_longest_substring("bbbbb") == 1
    assert Solution.length_of_longest_substring("pwwkew") == 3
    assert Solution.length_of_longest_substring("") == 0
    assert Solution.length_of_longest_substring("asdfgh") == 6
    assert Solution.length_of_longest_substring("dvdf") == 3
