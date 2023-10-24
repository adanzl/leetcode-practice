"""
 * 给你一个整数数组 nums 。每一次操作中，你可以将 nums 中 任意 一个元素替换成 任意 整数。
 * 如果 nums 满足以下条件，那么它是 连续的 ：
 * 1、nums 中所有元素都是 互不相同 的。
 * 2、nums 中 最大 元素与 最小 元素的差等于 nums.length - 1 。
 * 比方说，nums = [4, 2, 5, 3] 是 连续的 ，但是 nums = [1, 2, 3, 5, 6] 不是连续的 。
 * 请你返回使 nums 连续 的 最少 操作次数。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-continuous/
"""
import bisect
from itertools import pairwise
from typing import List


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        nn = [a for a, b in pairwise(nums) if a != b] + [nums[-1]]
        n = len(nums)
        ans = n
        for i, num in enumerate(nn):
            idx = bisect.bisect(nn, num + n - 1)
            ans = min(ans, n - (idx - i))
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().minOperations([1, 2, 3, 5, 6]))
    # 0
    print(Solution().minOperations([4, 2, 5, 3]))
    # 3
    print(Solution().minOperations([1, 10, 100, 1000]))
