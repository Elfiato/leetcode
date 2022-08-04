'''
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
'''


class Solution:
    @staticmethod
    def longest_palindrome(s: str) -> str:
        res = ''
        shift, i = 0, -1
        if len(s) < 2:
            return s
        while i + 1 < len(s):
            i += 1
            same_letters_start_index, same_letters_stop_index = -1, -1
            pointer = 0
            shift = 0
            same_letters = ''
            while True:
                if i + pointer + 1 < len(s) and s[i + pointer] == s[i + pointer + 1]:
                    if same_letters_start_index < 0:
                        same_letters_start_index = i + pointer
                    same_letters_stop_index = i + pointer + 1
                    same_letters = s[same_letters_start_index:same_letters_stop_index + 1]
                else:
                    if same_letters:
                        shift = same_letters_stop_index - same_letters_start_index
                        if len(same_letters) > len(res):
                            res = same_letters
                    pointer = 1
                    break
                pointer += 1
            while i - pointer > -1 and i + pointer + shift < len(s):
                if s[i - pointer] == s[i + shift + pointer]:
                    palindrome = s[i - pointer:i + shift + pointer + 1]
                    if len(palindrome) > len(res):
                        res = palindrome
                else:
                    break
                pointer += 1
            if same_letters and len(same_letters) > len(res):
                res = same_letters
        return res or s[0]


if __name__ == '__main__':
    tasks = ['abbbbbbac', 'babad', 'cbbd', 'a', 'ac', 'bb', 'abcba', 'aacabdkacaa', 'xaabacxcabaaxcabaax']
    ans = ['abbbbbba', 'bab', 'bb', 'a', 'a', 'bb', 'abcba', 'aca', 'xaabacxcabaax']
    for i in range(len(tasks)):
        cur_ans = Solution.longest_palindrome(tasks[i])
        assert cur_ans == ans[i], f'Longest palindrome of {tasks[i]}, must be {ans[i]}, but get {cur_ans}'
