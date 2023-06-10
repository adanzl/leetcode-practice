"""
 * 给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
 * 删除完毕后，请你返回最终结果链表的头节点。
 * 你可以返回任何满足题目要求的答案。
 * （注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）
 * 提示：
 * 1、给你的链表中可能有 1 到 1000 个节点。
 * 2、对于链表中的每个节点，节点的值：-1000 <= node.val <= 1000.
 * 链接：https://leetcode.cn/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
"""

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode(-1, head)
        stack = [h]
        p = head
        while p:
            v = p.val
            if v:
                for i in range(len(stack) - 1, 0, -1):
                    v += stack[i].val
                    if v == 0:
                        stack[i - 1].next = p.next
                        stack = stack[:i]
                        break
                else:
                    stack.append(p)
            else:
                stack[-1].next = p.next
            p = p.next
        return h.next


if __name__ == '__main__':
    # []
    print(listNodeToString(Solution().removeZeroSumSublists(stringToListNode('[0]'))))
    # [1]
    print(listNodeToString(Solution().removeZeroSumSublists(stringToListNode('[1,0]'))))
    # [3,1]
    print(listNodeToString(Solution().removeZeroSumSublists(stringToListNode('[1, 2, -3, 3, 1]'))))
    # [1,2,4]
    print(listNodeToString(Solution().removeZeroSumSublists(stringToListNode('[1, 2, 3, -3, 4]'))))
    # [1]
    print(listNodeToString(Solution().removeZeroSumSublists(stringToListNode('[1, 2, 3, -3, -2]'))))
