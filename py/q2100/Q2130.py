"""
 * 在一个大小为 n 且 n 为 偶数 的链表中，对于 0 <= i <= (n / 2) - 1 的 i ，第 i 个节点（下标从 0 开始）的孪生节点为第 (n-1-i) 个节点 。
 * 比方说，n = 4 那么节点 0 是节点 3 的孪生节点，节点 1 是节点 2 的孪生节点。这是长度为 n = 4 的链表中所有的孪生节点。
 * 孪生和 定义为一个节点和它孪生节点两者值之和。
 * 给你一个长度为偶数的链表的头节点 head ，请你返回链表的 最大孪生和 。
 * 提示：
 * 1、链表的节点数目是 [2, 10^5] 中的 偶数 。
 * 2、1 <= Node.val <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-twin-sum-of-a-linked-list/
"""

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        p = head
        while p:
            arr.append(p.val)
            p = p.next
        n = len(arr)
        ans = 0
        for i in range(n // 2):
            ans = max(arr[i] + arr[n - 1 - i], ans)
        return ans


if __name__ == '__main__':
    # 6
    print(Solution().pairSum(stringToListNode("[5,4,2,1]")))
    # 7
    print(Solution().pairSum(stringToListNode("[4,2,2,3]")))
    # 100001
    print(Solution().pairSum(stringToListNode("[1,100000]")))