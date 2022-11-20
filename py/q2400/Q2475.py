"""
 * 给你一个下标从 0 开始的正整数数组 nums 。请你找出并统计满足下述条件的三元组 (i, j, k) 的数目：
 * 1、0 <= i < j < k < nums.length
 * 2、nums[i]、nums[j] 和 nums[k] 两两不同 。
 * 3、换句话说：nums[i] != nums[j]、nums[i] != nums[k] 且 nums[j] != nums[k] 。
 * 返回满足上述条件三元组的数目。
 * 提示：
 * 1、3 <= nums.length <= 100
 * 2、1 <= nums[i] <= 1000
 * 链接：https://leetcode.cn/problems/number-of-unequal-triplets-in-array/
"""
import os
import sys
from itertools import pairwise
from typing import List

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:
    """
        对于 xx，设：
            小于 xx 的数有 aa 个；
            等于 xx 的数有 bb 个；
            大于 xx 的数有 cc 个。
        那么 xx 对答案的贡献是 abc。
        累加所有贡献，得到答案。
        代码实现时，通过排序可以快速求出 a b c。
    """

    def unequalTriplets(self, nums: List[int]) -> int:
        nums.sort()
        ans = start = 0
        for i, (x, y) in enumerate(pairwise(nums)):
            if x != y:
                ans += start * (i - start + 1) * (len(nums) - 1 - i)
                start = i + 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().unequalTriplets([4, 4, 2, 4, 3]))
    # 0
    print(Solution().unequalTriplets([1, 1, 1, 1, 1]))
