'''
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
'''


class Solution:
    @staticmethod
    def convert(s: str, num_rows: int) -> str:
        res_matrix = []
        counter = 0
        is_row_flag = True
        pointer = num_rows - 2
        while counter < len(s):
            if is_row_flag or pointer <= 0:
                res_matrix.append([i for i in s[counter:counter+num_rows]])
                counter += num_rows
                pointer = num_rows - 2
                is_row_flag = False
            else:
                res_matrix.append([''] * num_rows)
                res_matrix[-1][pointer] += s[counter]
                counter += 1
                pointer -= 1
                if pointer == 0:
                    is_row_flag = True
        counter = 0
        res = ''
        while counter < num_rows:
            for st in res_matrix:
                try:
                    res += st[counter]
                except IndexError:
                    res += ''
            counter += 1
        return res

if __name__ == '__main__':
    tasks = [('ABCD', 2), ('PAYPALISHIRING', 3), ('PAYPALISHIRING', 1), ('PAYPALISHIRING', 4), ('a', 1), ('', 0), ('', 4)]
    ans = ['ACBD', 'PAHNAPLSIIGYIR', 'PAYPALISHIRING', 'PINALSIGYAHRPI', 'a', '', '']
    for i in range(len(tasks)):
        res = Solution.convert(*tasks[i])
        assert res == ans[i], f'В задании ({tasks[i]}, ожидается овтет {ans[i]}, но получен {res})'
