"""
 * 给你一个整数数组 nums 。如果 nums 的子序列满足下述条件，则认为该子序列是一个 方波 ：
 * 1、子序列的长度至少为 2 ，并且
 * 2、将子序列从小到大排序 之后 ，除第一个元素外，每个元素都是前一个元素的 平方 。
 * 返回 nums 中 最长方波 的长度，如果不存在 方波 则返回 -1 。
 * 子序列 也是一个数组，可以由另一个数组删除一些或不删除元素且不改变剩余元素的顺序得到。
 * 提示：
 * 1、2 <= nums.length <= 10^5
 * 2、2 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/longest-square-streak-in-an-array/
"""
import math
from typing import List


class Solution:

    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        ans = -1
        for i, num in enumerate(nums):
            sq = math.sqrt(num)
            dp[num] = max(1, dp.get(num, 1))
            sq = int(sq)
            if sq * sq != num: continue
            size = dp.get(sq, 0)
            dp[num] = max(size + 1, dp.get(num, 1))
            ans = max(ans, size + 1)
        return ans if ans > 1 else -1


if __name__ == '__main__':
    # -1
    print(Solution().longestSquareStreak([3, 13, 14, 14, 2]))
    # 4
    print(Solution().longestSquareStreak([4, 16, 256, 65536]))
    # 3
    print(Solution().longestSquareStreak([4, 3, 6, 16, 8, 2]))
    # -1
    print(Solution().longestSquareStreak([2, 3, 5, 6, 7]))
