"""
 * 给你一个链表的头节点 head 。删除 链表的 中间节点 ，并返回修改后的链表的头节点 head 。
 * 长度为 n 链表的中间节点是从头数起第 ⌊n / 2⌋ 个节点（下标从 0 开始），其中 ⌊x⌋ 表示小于或等于 x 的最大整数。
 * 对于 n = 1、2、3、4 和 5 的情况，中间节点的下标分别是 0、1、1、2 和 2 。
 * 提示：
 * 1、链表中节点的数目在范围 [1, 10^5] 内
 * 2、1 <= Node.val <= 10^5
 * 链接：https://leetcode.cn/problems/delete-the-middle-node-of-a-linked-list/
"""
from typing import Optional

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import ListNode, stringToListNode


class Solution:

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode(next=head)
        p2 = p1 = head
        pre = h
        while p2 and p1:
            p2 = p2.next
            if p2: p2 = p2.next
            else: break
            pre = p1
            p1 = p1.next
        if p1: pre.next = p1.next
        return h.next


if __name__ == '__main__':
    # [1,3,4,1,2,6]
    print(Solution().deleteMiddle(stringToListNode("[1,3,4,7,1,2,6]")))
    # []
    print(Solution().deleteMiddle(stringToListNode("[2]")))
    # [2]
    print(Solution().deleteMiddle(stringToListNode("[2,1]")))
    # [1,2,4]
    print(Solution().deleteMiddle(stringToListNode("[1,2,3,4]")))