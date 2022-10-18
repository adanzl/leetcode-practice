"""
 * 给你一个 不包含 任何零的整数数组 nums ，找出自身与对应的负数都在数组中存在的最大正整数 k 。
 * 返回正整数 k ，如果不存在这样的整数，返回 -1 。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、-1000 <= nums[i] <= 1000
 * 3、nums[i] != 0
 * 链接：https://leetcode.cn/problems/largest-positive-integer-that-exists-with-its-negative/
"""
from typing import List


class Solution:

    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        ans = -1
        for num in nums:
            if num < 0: continue
            if -num in s:
                ans = max(ans, num)
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().findMaxK([-1, 2, -3, 3]))
    # 7
    print(Solution().findMaxK([-1, 10, 6, 7, -7, 1]))
    # -1
    print(Solution().findMaxK([-10, 8, 6, 7, -2, -3]))
