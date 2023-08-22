"""
 * 给你一个链表的头 head ，每个结点包含一个整数值。
 * 在相邻结点之间，请你插入一个新的结点，结点值为这两个相邻结点值的 最大公约数 。
 * 请你返回插入之后的链表。
 * 两个数的 最大公约数 是可以被两个数字整除的最大正整数。
 * 提示：
 * 1、链表中结点数目在 [1, 5000] 之间。
 * 2、1 <= Node.val <= 1000
 * 链接：https://leetcode.cn/problems/insert-greatest-common-divisors-in-linked-list/
"""
from math import gcd

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        pre, p = head, head.next
        while p:
            node = ListNode(gcd(pre.val, p.val), p)
            pre.next = node
            pre = p
            p = p.next
        return head


if __name__ == '__main__':
    # [18,6,6,2,10,1,3]
    print(Solution().insertGreatestCommonDivisors(stringToListNode('[18,6,10,3]')))
    # [7]
    print(Solution().insertGreatestCommonDivisors(stringToListNode('[7]')))