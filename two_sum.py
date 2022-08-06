'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
from typing import List


class Solution:
    def __init__(self, num: List[int]):
        self.nums = num

    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        mp, res = {}, []
        for i in range(len(nums)):
            find_element = target - nums[i]
            if find_element in mp:
                res.append(i)
                res.append(mp[find_element])
                break
            else:
                mp[nums[i]] = i
        return res

    def two_sum2(self, target: int) -> List[int]:
        for i in range(len(self.nums)):
            for j in range(len(self.nums)):
                if self.nums[i] + self.nums[j] == target and i != j:
                    return [i, j]


if __name__ == '__main__':
    test_data = [2, 7, 11, 15]
    class_ex = Solution(test_data)
    assert Solution.two_sum(test_data, 9) == [0, 1] or Solution.two_sum(test_data, 9) == [1, 0]
    assert class_ex.two_sum2(9) == [0, 1] or class_ex.two_sum2(9) == [1, 0]
