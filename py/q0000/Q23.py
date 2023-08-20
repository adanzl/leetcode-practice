"""
 * 给你一个链表数组，每个链表都已经按升序排列。
 * 请你将所有链表合并到一个升序链表中，返回合并后的链表。
 * 提示：
 * 1、k == lists.length
 * 2、0 <= k <= 10^4
 * 3、0 <= lists[i].length <= 500
 * 4、-10^4 <= lists[i][j] <= 10^4
 * 5、lists[i] 按 升序 排列
 * 6、lists[i].length 的总和不超过 10^4
 * 链接：https://leetcode.cn/problems/merge-k-sorted-lists/
"""
from heapq import heapify, heappop, heappush, heapreplace
from typing import List

import sys, os
sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [[node.val, i] for i, node in enumerate(lists) if node]
        heapify(h)
        p = head = ListNode()
        while h and p:
            _, idx = h[0]
            node = lists[idx]
            if node is not None:
                p.next = node
                nx = lists[idx] = node.next
                p = p.next
                if nx:
                    heapreplace(h, [nx.val, idx])
                else:
                    heappop(h)
        return head.next

if __name__ == '__main__':
    # [1,1,2,3,4,4,5,6]
    print(Solution().mergeKLists(stringToListNodeList("[[1,4,5],[1,3,4],[2,6]]")))
    # []
    print(Solution().mergeKLists(stringToListNodeList("[]")))
    # []
    print(Solution().mergeKLists(stringToListNodeList("[[]]")))