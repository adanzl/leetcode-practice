"""
 * 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 nums 的子数组中元素的最大公因数等于 k 的子数组数目。
 * 子数组 是数组中一个连续的非空序列。
 * 数组的最大公因数 是能整除数组中所有元素的最大整数。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i], k <= 10^9
 * 链接：https://leetcode.cn/problems/number-of-subarrays-with-gcd-equal-to-k/
"""
from math import gcd
from typing import List


class Solution:

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] == k: ans += 1
            g = nums[i]
            for j in range(i - 1, -1, -1):
                g = gcd(nums[j], g)
                if g == k:
                    ans += 1
        return ans


if __name__ == '__main__':
    # 10
    print(Solution().subarrayGCD([4, 3, 1, 3, 3], 1))
    # 4
    print(Solution().subarrayGCD([9, 3, 1, 2, 6, 3], 3))
    # 7
    print(Solution().subarrayGCD([3, 12, 9, 6], 3))
    # 0
    print(Solution().subarrayGCD([4], 7))
