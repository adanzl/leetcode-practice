"""
 * 给你一个整数数组 nums 和一个整数 k 。
 * 将数组拆分成一些非空子数组。拆分的 代价 是每个子数组中的 重要性 之和。
 * 令 trimmed(subarray) 作为子数组的一个特征，其中所有仅出现一次的数字将会被移除。
 * 例如，trimmed([3,1,2,4,3,4]) = [3,4,3,4] 。
 * 子数组的 重要性 定义为 k + trimmed(subarray).length 。
 * 例如，如果一个子数组是 [1,2,3,3,3,4,4] ，trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4] 。这个子数组的重要性就是 k + 5 。
 * 找出并返回拆分 nums 的所有可行方案中的最小代价。
 * 子数组 是数组的一个连续 非空 元素序列。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、0 <= nums[i] < nums.length
 * 3、1 <= k <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-cost-to-split-an-array/
"""

from collections import Counter
from typing import List

#
# @lc app=leetcode.cn id=2547 lang=python3
#
# [2547] 拆分数组的最小代价
#


# @lc code=start
class Solution:

    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] + [10**10] * (n)  # 枚举最后一次划分
        for i in range(n):
            cnt = Counter()
            s = 0
            for j in range(i, -1, -1):
                cnt[nums[j]] += 1
                if cnt[nums[j]] == 2:
                    s += 2
                if cnt[nums[j]] > 2:
                    s += 1
                dp[i + 1] = min(dp[i] + k, dp[j] + s + k, dp[i + 1])
        return dp[-1]


# @lc code=end

if __name__ == '__main__':
    # 8
    print(Solution().minCost([1, 2, 1, 2, 1, 3, 3], k=2))
    # 6
    print(Solution().minCost([1, 2, 1, 2, 1], k=2))
    # 10
    print(Solution().minCost([1, 2, 1, 2, 1], k=5))
