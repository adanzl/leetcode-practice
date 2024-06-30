"""
 * 给你一个整数数组 nums。
 * nums 的子序列 sub 的长度为 x ，如果其满足以下条件，则称其为 有效子序列：
 * (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2
 * 返回 nums 的 最长的有效子序列 的长度。
 * 一个 子序列 指的是从原数组中删除一些元素（也可以不删除任何元素），剩余元素保持原来顺序组成的新数组。
 * 提示：
 * 1、2 <= nums.length <= 2 * 10^5
 * 2、1 <= nums[i] <= 10^7
 * 链接：https://leetcode.cn/problems/find-the-maximum-length-of-valid-subsequence-i/
"""
from typing import List


class Solution:

    def maximumLength(self, nums: List[int]) -> int:
        ans = 0
        dp = [[0, 0], [0, 0]]
        for num in nums:
            r = num % 2
            dp[r][0] = max(dp[r][0], dp[r][0] + 1)
            dp[r][1] = max(dp[r][1], dp[r ^ 1][1] + 1)
            ans = max(ans, dp[r][0], dp[r][1])
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().maximumLength([1, 2, 3, 4]))
    # 6
    print(Solution().maximumLength([1, 2, 1, 1, 2, 1, 2]))
    # 2
    print(Solution().maximumLength([1, 3]))
