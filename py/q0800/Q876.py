"""
 * 给定一个头结点为 head 的非空单链表，返回链表的中间结点。
 * 如果有两个中间结点，则返回第二个中间结点。
 * 提示：给定链表的结点数介于 1 和 100 之间。
 * 链接：https://leetcode.cn/problems/middle-of-the-linked-list/submissions/
"""
from typing import List

import sys, os
sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nx = h = ListNode(next=head)
        while nx:
            nx = nx.next
            h = h.next
            if nx:
                nx = nx.next
        return h


if __name__ == '__main__':
    # [3,4,5]
    print(Solution().middleNode(stringToListNode('[1,2,3,4,5]')))
    # [4,5,6]
    print(Solution().middleNode(stringToListNode('[1,2,3,4,5,6]')))
    # [1]
    print(Solution().middleNode(stringToListNode('[1]')))