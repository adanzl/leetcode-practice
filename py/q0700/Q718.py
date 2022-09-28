"""
 * 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
 * 说明:
 * 1 <= len(A), len(B) <= 1000
 * 0 <= A[i], B[i] < 100
 * 链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
"""
from typing import *


class Solution:

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
        return max(max(row) for row in dp)


if __name__ == '__main__':
    # 3
    print(Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4]))
    # 3
    print(Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    # 5
    print(Solution().findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))
