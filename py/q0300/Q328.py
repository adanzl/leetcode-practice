"""
 * 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。
 * 请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
 * 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
 * 说明:
 * 1、应当保持奇数节点和偶数节点的相对顺序。
 * 2、链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
 * 提示:
 * 1、n ==  链表中的节点数
 * 2、0 <= n <= 10^4
 * 3、-10^6 <= Node.val <= 10^6
 * 链接：https://leetcode-cn.com/problems/odd-even-linked-list
"""
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        h1, h2, p = ListNode(next=head), ListNode(), head
        p1, p2 = h1, h2
        while p:
            p1.next = p
            p1 = p
            p = p.next
            p2.next = p
            p2 = p
            if not p: break
            p = p.next
        p1.next = h2.next
        return h1.next


if __name__ == '__main__':
    # [1,3,5,2,4]
    print(Solution().oddEvenList(stringToListNode("[1,2,3,4,5]")))
    # [2,3,6,7,1,5,4]
    print(Solution().oddEvenList(stringToListNode("[2,1,3,5,6,4,7]")))