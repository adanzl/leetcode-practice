"""
 * 给你一个整数数组 nums 和一个链表的头节点 head。从链表中移除所有存在于 nums 中的节点后，返回修改后的链表的头节点。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 3、nums 中的所有元素都是唯一的。
 * 4、链表中的节点数在 [1, 10^5] 的范围内。
 * 5、1 <= Node.val <= 10^5
 * 6、输入保证链表中至少有一个值没有在 nums 中出现过。
 * 链接：https://leetcode.cn/problems/delete-nodes-from-linked-list-present-in-array/description/
"""
from typing import List
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_s = set(nums)
        h = ListNode()
        h.next = head
        pre, p = h, head
        while p:
            if p.val not in num_s:
                pre.next = p
                pre = p
            p = p.next
        pre.next = None
        return h.next


if __name__ == '__main__':
    # [4,5]
    print(Solution().modifiedList([1, 2, 3], stringToListNode('[1,2,3,4,5]')))
    # [2,2,2]
    print(Solution().modifiedList([1], stringToListNode('[1,2,1,2,1,2]')))
    # [1,2,3,4]
    print(Solution().modifiedList([5], stringToListNode('[1,2,3,4]')))
