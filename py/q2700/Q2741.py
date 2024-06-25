"""
 * 给你一个下标从 0 开始的整数数组 nums ，它包含 n 个 互不相同 的正整数。
 * 如果 nums 的一个排列满足以下条件，我们称它是一个特别的排列：
 * 对于 0 <= i < n - 1 的下标 i ，要么 nums[i] % nums[i+1] == 0 ，要么 nums[i+1] % nums[i] == 0 。
 * 请你返回特别排列的总数目，由于答案可能很大，请将它对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、2 <= nums.length <= 14
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/special-permutations
"""

from functools import cache
from typing import List

#
# @lc app=leetcode.cn id=2741 lang=python3
#
# [2741] 特别的排列
#


# @lc code=start
class Solution:

    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        @cache
        def dfs(lst, mark):
            if mark == 0: return 1
            ret = 0
            for i in range(n):
                if mark & (1 << i):
                    if lst % nums[i] == 0 or nums[i] % lst == 0:
                        ret += dfs(nums[i], mark - (1 << i))
            return ret % MOD

        return dfs(1, (1 << n) - 1)


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().specialPerm([2, 3, 6]))
    # 2
    print(Solution().specialPerm([1, 4, 3]))
