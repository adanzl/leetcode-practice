"""
 * 链表中的 临界点 定义为一个 局部极大值点 或 局部极小值点 。
 * 如果当前节点的值 严格大于 前一个节点和后一个节点，那么这个节点就是一个  局部极大值点 。
 * 如果当前节点的值 严格小于 前一个节点和后一个节点，那么这个节点就是一个  局部极小值点 。
 * 注意：节点只有在同时存在前一个节点和后一个节点的情况下，才能成为一个 局部极大值点 / 极小值点 。
 * 给你一个链表 head ，返回一个长度为 2 的数组 [minDistance, maxDistance] ，
 * 其中 minDistance 是任意两个不同临界点之间的最小距离，maxDistance 是任意两个不同临界点之间的最大距离。
 * 如果临界点少于两个，则返回 [-1，-1] 。
 * 提示：
 * 1、链表中节点的数量在范围 [2, 10^5] 内
 * 2、1 <= Node.val <= 10^5
 * 链接：https://leetcode.cn/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points
"""
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *
from typing import List

#
# @lc app=leetcode.cn id=2058 lang=python3
#
# [2058] 找出临界点之间的最小和最大距离
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        LIMIT = 0x3c3c3c3c3c3c
        mn_dis, mx_dis = LIMIT, 0
        lst_mn, lst_mx, l_mn, l_mx = -1, -1, -1, -1
        idx, p, pre, p_pre = 0, head, None, None

        def min_dis(idx):
            nonlocal mn_dis
            if lst_mx != -1:
                mn_dis = min(mn_dis, idx - lst_mx)
            if lst_mn != -1:
                mn_dis = min(mn_dis, idx - lst_mn)

        while p:
            if p_pre and pre:
                if p_pre.val < pre.val > p.val:
                    min_dis(idx - 1)
                    lst_mx = idx - 1
                    if l_mx == -1: l_mx = lst_mx
                if p_pre.val > pre.val < p.val:
                    min_dis(idx - 1)
                    lst_mn = idx - 1
                    if l_mn == -1: l_mn = lst_mn
                        
            p_pre = pre
            pre = p
            p = p.next
            idx += 1
        mx_dis = max(mx_dis, max(lst_mn, lst_mx) - min(l_mn if l_mn != -1 else LIMIT, l_mx if l_mx != -1 else LIMIT))

        return [mn_dis if mn_dis != LIMIT else -1, mx_dis if mx_dis else -1]


# @lc code=end

if __name__ == '__main__':
    # [-1,-1]
    print(Solution().nodesBetweenCriticalPoints(stringToListNode('[2,2,1,3]')))
    # [1,1]
    print(Solution().nodesBetweenCriticalPoints(stringToListNode('[4,2,4,1]')))
    # [1,3]
    print(Solution().nodesBetweenCriticalPoints(stringToListNode('[5,3,1,2,5,1,2]')))
    # [-1,-1]
    print(Solution().nodesBetweenCriticalPoints(stringToListNode('[3,1]')))
    # [3,3]
    print(Solution().nodesBetweenCriticalPoints(stringToListNode('[1,3,2,2,3,2,2,2,7]')))
    # [-1,-1]
    print(Solution().nodesBetweenCriticalPoints(stringToListNode('[2,3,3,2]')))
