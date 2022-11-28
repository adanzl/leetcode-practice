"""
 * 给你一个链表的头节点 head 。
 * 对于列表中的每个节点 node ，如果其右侧存在一个具有 严格更大 值的节点，则移除 node 。
 * 返回修改后链表的头节点 head 。
 * 提示：
 * 1、给定列表中的节点数目在范围 [1, 10^5] 内
 * 2、1 <= Node.val <= 10^5
 * 链接：https://leetcode.cn/problems/remove-nodes-from-linked-list/
"""
from typing import Optional, Deque
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode(0x3c3c3c3c)
        cur = head
        q = Deque()
        while cur:
            while q and q[-1].val < cur.val:
                q.pop()
            q.append(cur)
            cur = cur.next
        ans = h
        while q:
            ans.next = q.popleft()
            ans = ans.next
        return h.next


if __name__ == '__main__':
    # [13,8]
    print(Solution().removeNodes(stringToListNode('[5,2,13,3,8]')))
    # [1,1,1,1]
    print(Solution().removeNodes(stringToListNode('[1,1,1,1]')))