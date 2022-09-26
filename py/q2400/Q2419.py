"""
 * 给你一个长度为 n 的整数数组 nums 。
 * 考虑 nums 中进行 按位与（bitwise AND）运算得到的值 最大 的 非空 子数组。
 * 换句话说，令 k 是 nums 任意 子数组执行按位与运算所能得到的最大值。那么，只需要考虑那些执行一次按位与运算后等于 k 的子数组。
 * 返回满足要求的 最长 子数组的长度。
 * 数组的按位与就是对数组中的所有数字进行按位与运算。
 * 子数组 是数组中的一个连续元素序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/longest-subarray-with-maximum-bitwise-and/
"""
from typing import *


class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        arr = sorted(zip(nums, list(range(n))), key=lambda x: (-x[0], x[1]))
        ans = 1
        l = 1
        mx = arr[0][0]
        for i in range(1, n):
            if arr[i][0] != mx: break
            if arr[i][1] == arr[i - 1][1] + 1:
                l += 1
                ans = max(ans, l)
            else:
                l = 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().longestSubarray([1, 2, 3, 3, 2, 2]))
    # 1
    print(Solution().longestSubarray([1, 2, 3, 4]))
