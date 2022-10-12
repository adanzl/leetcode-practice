"""
 * 给定链表头结点 head，该链表上的每个结点都有一个 唯一的整型值 。同时给定列表 nums，该列表是上述链表中整型值的一个子集。
 * 返回列表 nums 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 nums 中）构成的集合。
 * 提示：
 * 1、链表中节点数为n
 * 2、1 <= n <= 10^4
 * 3、0 <= Node.val < n
 * 4、Node.val 中所有值 不同
 * 5、1 <= nums.length <= n
 * 6、0 <= nums[i] < n
 * 7、nums 中所有值 不同
 * 链接：https://leetcode.cn/problems/linked-list-components/
"""
from typing import List

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        if head is None: return 0
        n_set = set(nums)
        node = head
        ans, l = 0, 0
        while node is not None:
            if node.val in n_set:
                l += 1
            else:
                ans += 1 if l else 0
                l = 0
            node = node.next
        return ans + (1 if l else 0)


if __name__ == '__main__':
    # 1
    print(Solution().numComponents(stringToListNode("[0,2,4,3,1]"), [3, 2, 4]))
    # 2
    print(Solution().numComponents(stringToListNode("[0,1,2,3]"), [0, 1, 3]))
    # 2
    print(Solution().numComponents(stringToListNode("[0,1,2,3,4]"), [0, 3, 1, 4]))
