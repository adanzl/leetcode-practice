"""
 * 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
 * 提示：
 * 1、链表中结点的数目为 sz
 * 2、1 <= sz <= 30
 * 3、0 <= Node.val <= 100
 * 4、1 <= n <= sz
 * 链接：https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
"""
from typing import *
import sys, os

sys.path.append(os.path.dirname(__file__) + "/../")
from LCUtil import *


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h = ListNode()
        h.next = head
        pre = cur = h
        c = 0
        while cur != None:
            cur = cur.next
            if c > n:
                pre = pre.next
            c += 1
        pre.next = pre.next.next
        return h.next


if __name__ == '__main__':
    # [1,2,3,5]
    print(listNodeToString(Solution().removeNthFromEnd(stringToListNode("[1,2,3,4,5]"), 2)))
    # []
    print(listNodeToString(Solution().removeNthFromEnd(stringToListNode("[1]"), 1)))
    # [1]
    print(listNodeToString(Solution().removeNthFromEnd(stringToListNode("[1,2]"), 1)))
