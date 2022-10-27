"""
 * 给你一个整数数组 nums，返回 nums 中最长等差子序列的长度。
 * 回想一下，nums 的子序列是一个列表 nums[i1], nums[i2], ..., nums[ik] ，且 0 <= i1 < i2 < ... < ik <= nums.length - 1。
 * 并且如果 seq[i+1] - seq[i]( 0 <= i < seq.length - 1) 的值都相同，那么序列 seq 是等差的。
 * 提示：
 * 1、2 <= nums.length <= 1000
 * 2、0 <= nums[i] <= 500
 * 链接：https://leetcode.cn/problems/longest-arithmetic-subsequence/
"""
from typing import Counter, List


class Solution:

    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dp = [Counter() for _ in range(n)]
        for i in range(n):
            for j in range(i):
                k = nums[i] - nums[j]
                dp[i][k] = max(dp[i][k], dp[j][k] + 1)
                ans = max(ans, dp[i][k])
        return ans + 1


if __name__ == '__main__':
    # 2
    print(Solution().longestArithSeqLength([83, 20, 17, 43, 52, 78, 68, 45]))
    # 4
    print(Solution().longestArithSeqLength([3, 6, 9, 12]))
    # 3
    print(Solution().longestArithSeqLength([9, 4, 7, 2, 10]))
    # 4
    print(Solution().longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]))
