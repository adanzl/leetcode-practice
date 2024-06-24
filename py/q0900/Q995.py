"""
 * 给定一个二进制数组 nums 和一个整数 k 。
 * k位翻转 就是从 nums 中选择一个长度为 k 的 子数组 ，同时把子数组中的每一个 0 都改成 1 ，把子数组中的每一个 1 都改成 0 。
 * 返回数组中不存在 0 所需的最小 k位翻转 次数。如果不可能，则返回 -1 。
 * 子数组 是数组的 连续 部分。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= k <= nums.length
 * 链接：https://leetcode.cn/problems/number-of-squareful-arrays/
"""
from itertools import pairwise
from typing import List


class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 差分
        diff = [nums[0]] + [b - a for a, b in pairwise(nums)] + [0]
        v, ans = 0, 0
        for i in range(n - k + 1):
            v += diff[i]
            if v & 1 == 0:  # even
                diff[i] += 1
                diff[i + k] -= 1
                v += 1
                ans += 1
        for i in range(n - k + 1, n):
            v += diff[i]
            if v & 1 == 0:  # even
                return -1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().minKBitFlips([0, 1, 0], 1))
    # -1
    print(Solution().minKBitFlips([1, 1, 0], 2))
    # 3
    print(Solution().minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3))
