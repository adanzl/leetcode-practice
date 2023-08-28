"""
 * 给你一个 非空 链表的头节点 head ，表示一个不含前导零的非负数整数。
 * 将链表 翻倍 后，返回头节点 head 。
 * 提示：
 * 1、链表中节点的数目在范围 [1, 10^4] 内
 * 2、0 <= Node.val <= 9
 * 3、生成的输入满足：链表表示一个不含前导零的数字，除了数字 0 本身。
 * 链接：https://leetcode.cn/problems/double-a-number-represented-as-a-linked-list/
"""
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p, pre = head, None
        while p:
            p.val *= 2
            nx = p.next
            p.next = pre
            pre = p
            p = nx
        p, pre = pre, None
        v = 0
        while p:
            v, p.val = divmod(p.val + v, 10)
            nx = p.next
            p.next = pre
            pre = p
            p = nx
        while v:
            v, r = divmod(v, 10)
            p = ListNode(r, pre)
            pre = p
        return pre


if __name__ == '__main__':
    # [3,7,8]
    print(Solution().doubleIt(stringToListNode("[1,8,9]")))
    # [1,9,9,8]
    print(Solution().doubleIt(stringToListNode("[9,9,9]")))