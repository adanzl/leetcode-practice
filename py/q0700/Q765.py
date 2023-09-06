"""
 * 给你一个头结点为 head 的单链表和一个整数 k ，请你设计一个算法将链表分隔为 k 个连续的部分。
 * 每部分的长度应该尽可能的相等：任意两部分的长度差距不能超过 1 。这可能会导致有些部分为 null 。
 * 这 k 个部分应该按照在链表中出现的顺序排列，并且排在前面的部分的长度应该大于或等于排在后面的长度。
 * 返回一个由上述 k 部分组成的数组。
 * 提示：
 * 1、链表中节点的数目在范围 [0, 1000]
 * 2、0 <= Node.val <= 1000
 * 3、1 <= k <= 50
 * 链接：https://leetcode.cn/problems/split-linked-list-in-parts/
"""
from typing import List

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cnt = 0
        p = head
        while p:
            cnt += 1
            p = p.next
        a, r = divmod(cnt, k)
        ans: List[Optional[ListNode]] = [None] * k
        p = head
        for i in range(k):
            size = a + 1 if i < r else a
            if not p: break
            h = p
            ans[i] = h
            for _ in range(size - 1):
                if not h.next: break
                h = h.next
            p = h.next
            h.next = None
        return ans


if __name__ == '__main__':
    # [[1,2,3,4],[5,6,7],[8,9,10]]
    print(Solution().splitListToParts(stringToListNode('[1,2,3,4,5,6,7,8,9,10]'), 3))
    # [[1],[2],[3],[],[]]
    print(Solution().splitListToParts(stringToListNode('[1,2,3]'), 5))