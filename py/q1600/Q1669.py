"""
 * 给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。
 * 请你将 list1 中下标从 a 到 b 的全部节点都删除，并将list2 接在被删除节点的位置。
 * 下图中蓝色边和节点展示了操作后的结果：
 * 请你返回结果链表的头指针。
 * 提示：
 * 1、3 <= list1.length <= 10^4
 * 2、1 <= a <= b < list1.length - 1
 * 3、1 <= list2.length <= 10^4
 * 链接：https://leetcode.cn/problems/merge-in-between-linked-lists/
"""

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, list1)
        l = r = head
        i, p = 0, list2
        while i < a and l:
            l = l.next
            i += 1
        r = l.next
        while i <= b and r:
            r = r.next
            i += 1
        l.next = list2
        while p and p.next:
            p = p.next
        p.next = r
        return head.next


if __name__ == '__main__':
    # [0,1,2,1000000,1000001,1000002,5]
    print(Solution().mergeInBetween(stringToListNode("[0,1,2,3,4,5]"), 3, 4, stringToListNode("[1000000,1000001,1000002]")))
    # [0,1,1000000,1000001,1000002,1000003,1000004,6]
    print(Solution().mergeInBetween(stringToListNode("[0,1,2,3,4,5,6]"), 2, 5, stringToListNode("[1000000,1000001,1000002,1000003,1000004]")))