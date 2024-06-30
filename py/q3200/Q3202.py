"""
 * 给你一个整数数组 nums 和一个 正 整数 k 。
 * nums 的一个 子序列 sub 的长度为 x ，如果其满足以下条件，则称其为 有效子序列 ：
 * (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k
 * 返回 nums 的 最长有效子序列 的长度。
 * 提示：
 * 1、2 <= nums.length <= 10^3
 * 2、1 <= nums[i] <= 10^7
 * 3、1 <= k <= 10^3
 * 链接：https://leetcode.cn/problems/find-the-maximum-length-of-valid-subsequence-ii/
"""
from typing import List


class Solution:

    def maximumLength(self, nums: List[int], k: int) -> int:
        ans = 0
        dp = [[0] * k for _ in range(k)]
        for num in nums:
            r = num % k
            for rr in range(k):
                v = (rr + k - r) % k
                dp[r][rr] = max(dp[r][rr], dp[v][rr] + 1)
                ans = max(ans, dp[r][rr])
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().maximumLength([1, 4, 2, 3, 1, 4], k=3))
    # 5
    print(Solution().maximumLength([1, 2, 3, 4, 5], k=2))
    #
    # print(Solution().maximumLength())
