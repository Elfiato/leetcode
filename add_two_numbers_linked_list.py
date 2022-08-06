'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return f'{self.val} -> {self.next}'


class Solution:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num, l2_num = '', ''
        for i in l1:
            l1_num += str(i)
        l1_num = int(l1_num[::-1])
        for i in l2:
            l2_num += str(i)
        l2_num = int(l2_num[::-1])
        res = []
        sum_num = str(l1_num+l2_num)[::-1]
        for i in range(len(sum_num)):
            try:
                res.append(ListNode(int(sum_num[i]), int(sum_num[i+1])))
            except IndexError:
                res.append(ListNode(int(sum_num[i]), None))
        return res






if __name__ == '__main__':
    test_l1 = ListNode(2, ListNode(4, ListNode(3)))
    test_l2 = ListNode(5, ListNode(6, ListNode(4)))
    print(test_l1.val, test_l1.next, sep='>')
    test_l1 = test_l1.next
    print(test_l1.val, test_l1.next, sep='>')
    test_l1 = test_l1.next
    print(test_l1.val, test_l1.next, sep='>')
    # print(Solution.addTwoNumbers(test_l1, test_l2))
