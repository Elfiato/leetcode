'''
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val} -> {self.next}'

    def __repr__(self):
        return f'{self.val} -> {self.next}'

    def __eq__(self, other):
        current_val_1, current_val_2 = self, other
        while current_val_1 is not None and current_val_2 is not None:
            if current_val_1.val != current_val_2.val:
                return False
            current_val_1 = current_val_1.next
            current_val_2 = current_val_2.next
        return True


class Solution:
    @staticmethod
    def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_val_1, current_val_2 = l1, l2
        l1_nums, l2_nums = '', ''
        while current_val_1 is not None or current_val_2 is not None:
            if current_val_1 is not None:
                l1_nums += str(current_val_1.val)
                current_val_1 = current_val_1.next
            if current_val_2 is not None:
                l2_nums += str(current_val_2.val)
                current_val_2 = current_val_2.next
        linked_list_sum = None
        for i in str(int(l1_nums[::-1]) + int(l2_nums[::-1])):
            linked_list_sum = ListNode(int(i), linked_list_sum)
        return linked_list_sum


if __name__ == '__main__':
    f_l = [ListNode(2, ListNode(4, ListNode(3))), ListNode(0),
           ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))]
    s_l = [ListNode(5, ListNode(6, ListNode(4))), ListNode(0), ListNode(9, ListNode(9, ListNode(9, ListNode(9))))]
    res = [ListNode(7, ListNode(0, ListNode(8))), ListNode(0),
           ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))]
    for i in range(len(res)):
        assert Solution.add_two_numbers(f_l[i], s_l[i]) == res[i], f'{f_l[i]} + {s_l[i]} = {res[i]}'
