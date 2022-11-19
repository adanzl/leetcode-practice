"""
 * 给你两个数组 nums1 和 nums2 。
 * 请你返回 nums1 和 nums2 中两个长度相同的 非空 子序列的最大点积。
 * 数组的非空子序列是通过删除原数组中某些元素（可能一个也不删除）后剩余数字组成的序列，但不能改变数字间相对顺序。
 * 比方说，[2,3,5] 是 [1,2,3,4,5] 的一个子序列而 [1,5,3] 不是。
 * 提示：
 * 1、1 <= nums1.length, nums2.length <= 500
 * 2、-1000 <= nums1[i], nums2[i] <= 100
 * 链接：https://leetcode.cn/problems/max-dot-product-of-two-subsequences/
"""
from typing import List


class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        inf = 0x3c3c3c3c
        dp = [[-inf] * (n + 1) for _ in range(m + 1)]  # dp[nums1][nums2]
        for i1 in range(m):  # nums1
            for i2 in range(n):  # nums2
                dp[i1 + 1][i2 + 1] = max(dp[i1 + 1][i2 + 1], dp[i1 + 1][i2])
                dp[i1 + 1][i2 + 1] = max(dp[i1 + 1][i2 + 1], dp[i1][i2 + 1])
                dp[i1 + 1][i2 + 1] = max(dp[i1 + 1][i2 + 1], nums1[i1] * nums2[i2] + (dp[i1][i2] if dp[i1][i2] > 0 else 0))
        return dp[-1][-1]


if __name__ == '__main__':
    # 18
    print(Solution().maxDotProduct([2, 1, -2, 5], [3, 0, -6]))
    # 21
    print(Solution().maxDotProduct([3, -2], [2, -6, 7]))
    # -1
    print(Solution().maxDotProduct([-1, -1], [1, 1]))
