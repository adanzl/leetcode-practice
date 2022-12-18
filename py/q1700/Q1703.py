"""
 * 给你一个整数数组 nums 和一个整数 k 。 nums 仅包含 0 和 1 。每一次移动，你可以选择 相邻 两个数字并将它们交换。
 * 请你返回使 nums 中包含 k 个 连续 1 的 最少 交换次数。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、nums[i] 要么是 0 ，要么是 1 。
 * 3、1 <= k <= sum(nums)
 * 链接：https://leetcode.cn/problems/minimum-adjacent-swaps-for-k-consecutive-ones/
"""
from itertools import accumulate
from typing import List


class Solution:

    def minMoves(self, nums: List[int], k: int) -> int:
        # 中位数贪心
        # 1 0 0 1 0 1
        # 此时，将左右的1移动到中间的1， 交换次数最小，即移动到中位数的位置
        # 题目转换为枚举每个 1 作为最左侧1的情况
        # 设 s 为 p 的前缀和，k=5，则
        # 距离和 = |p0 - p2| + |p1 - p2| + |p2 - p2| + |p3 - p2| + |p4 - p2|
        #       = (p2 - p0) + (p2 - p1) + (p2 - p2) + (p3 - p2) + (p4 - p2)
        #       = 2p2-(p0 ＋ P1) ＋ (p2 ＋ p3 ＋ P4) - 3p2
        #       = -(s[2] - s[0]) + (s[5] - s[2]) - p2
        #       = s[0]＋ s[5] - 2s[2] - p2
        # 如果 s=4 则：距离和 = s[0] + s[4] - 2s[2]
        # 对于一般情况，距离和 = s[0] + s[k] - 2s[k/2] - p[k/2]·(k%2)
        # 那么要计算的就是 s[i] ＋ s[i+k] - 2s[i+k/2] - p[i+k/2]·(k%2) 的最小值，这里i=0,1,...,m-k，其中m为1的个数
        # https://leetcode.cn/problems/minimum-adjacent-swaps-for-k-consecutive-ones/solution/tu-jie-zhuan-huan-cheng-zhong-wei-shu-ta-iz4v/
        p = [q - i for i, q in enumerate(i for i, x in enumerate(nums) if x)]
        s = list(accumulate(p, initial=0))  # p 的前缀和
        # p[i:i+k] 中所有数到 p[i+k//2] 的距离之和，取最小值
        return min(s[i] + s[i + k] - s[i + k // 2] * 2 - p[i + k // 2] * (k % 2) for i in range(len(p) - k + 1))


if __name__ == '__main__':
    # 2
    print(Solution().minMoves([0, 1, 1, 0, 0, 1, 0, 0, 0], 3))
    # 6
    print(Solution().minMoves([1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1], 7))
    # 1
    print(Solution().minMoves([1, 0, 0, 1, 0, 1], 2))
    # 0
    print(Solution().minMoves([1, 1], 1))
    # 5
    print(Solution().minMoves([1, 0, 0, 0, 0, 0, 1, 1], 3))
    # 0
    print(Solution().minMoves([1, 1, 0, 1], 2))
