"""
 * 给你一个整数数组 nums 和两个整数 minK 以及 maxK 。
 * nums 的定界子数组是满足下述条件的一个子数组：
 * 1、子数组中的 最小值 等于 minK 。
 * 2、子数组中的 最大值 等于 maxK 。
 * 返回定界子数组的数目。
 * 子数组是数组中的一个连续部分。
 * 提示：
 * 1、2 <= nums.length <= 10^5
 * 2、1 <= nums[i], minK, maxK <= 10^6
 * 链接：https://leetcode.cn/problems/count-subarrays-with-fixed-bounds/
"""
from typing import List


class Solution:

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        left = min_i = max_i = -1  # left 要排除
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                min_i, max_i = -1, -1
                left = i
            else:
                if num == minK: min_i = i
                if num == maxK: max_i = i
                ans += max(min(min_i, max_i) - left, 0)
        return ans


if __name__ == '__main__':
    # 10
    print(Solution().countSubarrays([1, 1, 1, 1], 1, 1))
    # 2
    print(Solution().countSubarrays([1, 3, 5, 2, 7, 5], 1, 5))
    # 81
    print(Solution().countSubarrays([35054, 398719, 945315, 945315, 820417, 945315, 35054, 945315, 171832, 945315, 35054, 109750, 790964, 441974, 552913], 35054, 945315))
