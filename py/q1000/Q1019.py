"""
 * 给定一个长度为 n 的链表 head
 * 对于列表中的每个节点，查找下一个 更大节点 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 严格大于 它的值。
 * 返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值。
 * 如果第 i 个节点没有下一个更大的节点，设置 answer[i] = 0 。
 * 提示：
 * 1、链表中节点数为 n
 * 2、1 <= n <= 10^4
 * 3、1 <= Node.val <= 10^9
 * 链接：https://leetcode.cn/problems/next-greater-node-in-linked-list/
"""
from typing import List
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans, s, p, idx = [], [], head, 0
        while p:
            while s and s[-1][0] < p.val:
                ans[s.pop()[1]] = p.val
            s.append([p.val, idx])
            idx += 1
            ans.append(0)
            p = p.next
        return ans


if __name__ == '__main__':
    # [5,5,0]
    print(Solution().nextLargerNodes(stringToListNode("[2,1,5]")))
    # [7,0,5,5,0]
    print(Solution().nextLargerNodes(stringToListNode("[2,7,4,3,5]")))