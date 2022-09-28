"""
 * 给定数组nums和一个整数k。我们将给定的数组nums分成 最多k个相邻的非空子数组 。分数 由每个子数组内的平均值的总和构成。
 * 注意我们必须使用 nums 数组中的每一个数进行分组，并且分数不一定需要是整数。
 * 返回我们所能得到的最大 分数 是多少。答案误差在10^-6内被视为是正确的。
 * 提示:
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 10^4
 * 3、1 <= k <= nums.length
 * 链接：https://leetcode.cn/problems/largest-sum-of-averages
"""

from typing import *
from functools import cache


class Solution:

    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i, num in enumerate(nums):
            pre_sum[i + 1] = pre_sum[i] + num

        @cache
        def func(idx, k):
            if k == 1:
                return (pre_sum[n] - pre_sum[idx]) / (n - idx)
            ret = 0
            for i in range(1, n - idx - k + 2):
                v = (pre_sum[idx + i] - pre_sum[idx]) / i + func(idx + i, k - 1)
                ret = max(ret, v)
            return ret

        return func(0, k)


if __name__ == '__main__':
    #
    print(Solution().largestSumOfAverages(list(range(100)), 50))
    # 20.00000
    print(Solution().largestSumOfAverages([9, 1, 2, 3, 9], 3))
    # 14
    print(Solution().largestSumOfAverages([9, 1, 9], 2))
    # 18.16667
    print(Solution().largestSumOfAverages([4, 1, 7, 5, 6, 2, 3], 4))
    # 20.50000
    print(Solution().largestSumOfAverages([1, 2, 3, 4, 5, 6, 7], 4))
