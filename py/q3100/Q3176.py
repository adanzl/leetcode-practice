"""
 * 给你一个整数数组 nums 和一个 非负 整数 k 。
 * 如果一个整数序列 seq 满足在范围下标范围 [0, seq.length - 2] 中存在 不超过 k 个下标 i 满足 seq[i] != seq[i + 1] ，
 * 那么我们称这个整数序列为 好 序列。
 * 请你返回 nums 中 好 子序列 的最长长度
 * 提示：
 * 1、1 <= nums.length <= 500
 * 2、1 <= nums[i] <= 10^9
 * 3、0 <= k <= min(nums.length, 25)
 * 链接：https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-i/
"""
from typing import List


class Solution:

    def maximumLength(self, nums: List[int], k: int) -> int:
        end_dp = {}  # 以各个数结尾的答案
        dp = [0] * (k + 2)  # 满足条件不同下标个数的最终答案
        for num in nums:
            if num not in end_dp:
                end_dp[num] = [0] * (k + 2)
            f = end_dp[num]  # f表是以num结尾的各种k的最长长度
            for i in range(k, -1, -1):  # k+1下标为最终答案
                f[i] = max(f[i], dp[i]) + 1  # 更新f，f[i]和dp[i+1]是对应的，所以f[i]需要通过dp[i]计算
                dp[i + 1] = max(dp[i + 1], f[i])
        return dp[-1]


if __name__ == '__main__':
    # 4
    print(Solution().maximumLength([48, 49, 48, 50, 49], 2))
    # 4
    print(Solution().maximumLength([1, 2, 1, 1, 3], k=2))
    # 2
    print(Solution().maximumLength([1, 2, 3, 4, 5, 1], k=0))
