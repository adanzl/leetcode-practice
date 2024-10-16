"""
 * 给你一个数组 maximumHeight ，其中 maximumHeight[i] 表示第 i 座塔可以达到的 最大 高度。
 * 你的任务是给每一座塔分别设置一个高度，使得：
 * 1、第 i 座塔的高度是一个正整数，且不超过 maximumHeight[i] 。
 * 2、所有塔的高度互不相同。
 * 请你返回设置完所有塔的高度后，可以达到的 最大 总高度。如果没有合法的设置，返回 -1 。
 * 提示：
 * 1、1 <= maximumHeight.length <= 10^5
 * 2、1 <= maximumHeight[i] <= 10^9
 * 链接：https://leetcode.cn/problems/maximize-the-total-height-of-unique-towers/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        ans, pre = 0, INF
        for h in maximumHeight:
            if pre == h:
                v = h - 1
            elif pre > h:
                v = h
            else:
                v = pre - 1
            if v <= 0:
                return -1
            ans += v
            pre = v
        return ans


if __name__ == '__main__':
    # 10
    print(Solution().maximumTotalSum([2, 3, 4, 3]))
    # 25
    print(Solution().maximumTotalSum([15, 10]))
    # -1
    print(Solution().maximumTotalSum([2, 2, 1]))
