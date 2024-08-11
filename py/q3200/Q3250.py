"""
 * 给你一个长度为 n 的 正 整数数组 nums 。
 * 如果两个 非负 整数数组 (arr1, arr2) 满足以下条件，我们称它们是 单调 数组对：
 * 1、两个数组的长度都是 n 。
 * 2、arr1 是单调 非递减 的，换句话说 arr1[0] <= arr1[1] <= ... <= arr1[n - 1] 。
 * 3、arr2 是单调 非递增 的，换句话说 arr2[0] >= arr2[1] >= ... >= arr2[n - 1] 。
 * 4、对于所有的 0 <= i <= n - 1 都有 arr1[i] + arr2[i] == nums[i] 。
 * 请你返回所有 单调 数组对的数目。
 * 由于答案可能很大，请你将它对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、1 <= n == nums.length <= 2000
 * 2、1 <= nums[i] <= 50
 * 链接：https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-i/description/
"""
from functools import cache
from typing import List


class Solution:

    def countOfPairs(self, nums: List[int]) -> int:

        MOD = 10**9 + 7

        @cache
        def dfs(idx, limit0, limit1):
            if idx == len(nums):
                return 1
            ret = 0
            down = max(limit0, nums[idx] - limit1)
            up = nums[idx]
            for nx in range(down, up + 1):
                ret += dfs(idx + 1, nx, nums[idx] - nx)
            return ret % MOD

        return dfs(0, 0, nums[0])


if __name__ == '__main__':
    # 4
    print(Solution().countOfPairs([2, 3, 2]))
    # 126
    print(Solution().countOfPairs([5, 5, 5, 5]))
    #
    # print(Solution().countOfPairs())
