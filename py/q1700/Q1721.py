"""
 * 给你链表的头节点 head 和一个整数 k 。
 * 交换 链表正数第 k 个节点和倒数第 k 个节点的值后，返回链表的头节点（链表 从 1 开始索引）。
 * 提示：
 * 1、链表中节点的数目是 n
 * 2、1 <= k <= n <= 10^5
 * 3、0 <= Node.val <= 100
 * 链接：https://leetcode.cn/problems/swapping-nodes-in-a-linked-list/
"""
from typing import List, Optional

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = head
        arr = []
        while p:
            arr.append(p)
            p = p.next
        arr[k-1].val, arr[-k].val = arr[-k].val, arr[k-1].val
        return head


if __name__ == '__main__':
    # [1,4,3,2,5]
    print(Solution().swapNodes(stringToListNode('[1,2,3,4,5]'), k=2))
    # [7,9,6,6,8,7,3,0,9,5]
    print(Solution().swapNodes(stringToListNode('[7,9,6,6,7,8,3,0,9,5]'), 5))
    # [1]
    print(Solution().swapNodes(stringToListNode('[1]'), 1))
    # [2,1]
    print(Solution().swapNodes(stringToListNode('[1,2]'), 1))
    # [1,2,3]
    print(Solution().swapNodes(stringToListNode('[1,2,3]'), 2))
