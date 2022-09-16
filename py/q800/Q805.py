"""
 * 给定你一个整数数组 nums
 * 我们要将 nums 数组中的每个元素移动到 A 数组 或者 B 数组中，使得 A 数组和 B 数组不为空，并且 average(A) == average(B) 。
 * 如果可以完成则返回true ， 否则返回 false  。
 * 注意：对于数组 arr ,  average(arr) 是 arr 的所有元素除以 arr 长度的和。
 * 提示:
 * 1、1 <= nums.length <= 30
 * 2、0 <= nums[i] <= 10^4
"""

from typing import *
from math import isclose


class Solution:

    def splitArraySameAverage(self, nums: List[int]) -> bool:
        # 0-1背包思路
        n = len(nums)
        avg = sum(nums) / n
        dp = [set() for i in range(n)]
        dp[0].add(0)
        for idx, num in enumerate(nums):
            for i in range(min(n - 1, idx + 1), 0, -1):
                limit = avg * i
                for v in dp[i - 1]:
                    nm = v + num
                    if isclose(nm, limit):
                        return True
                    dp[i].add(nm)
        return False


if __name__ == '__main__':
    # True
    print(Solution().splitArraySameAverage([4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5]))
    # False
    print(Solution().splitArraySameAverage([17, 3, 7, 12, 1]))
    # True
    print(Solution().splitArraySameAverage([18, 0, 16, 2]))
    # True
    print(Solution().splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8]))
    # False
    print(Solution().splitArraySameAverage([3, 74, 86, 33, 50, 96, 79, 51, 27, 29, 80, 65, 19, 92, 58, 25, 59, 87, 61, 17, 89, 17]))
    # False
    print(Solution().splitArraySameAverage([3, 1]))
