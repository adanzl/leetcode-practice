"""
 * 给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围 [left, right] 内的子数组，并返回满足条件的子数组的个数。
 * 生成的测试用例保证结果符合 32-bit 整数范围。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^9
 * 3、0 <= left <= right <= 10^9
 * 链接：https://leetcode.cn/problems/number-of-subarrays-with-bounded-maximum/
"""
from typing import List

class Solution:

    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        n, a, b = len(nums), 0, 0
        for i in range(n):
            if nums[i] > right:
                a = 0
                b = 0
            elif left <= nums[i] <= right:
                a = b + 1
                b += 1
            else:
                b += 1
            ans += a
        return ans


if __name__ == '__main__':
    # 22
    print(Solution().numSubarrayBoundedMax([73, 55, 36, 5, 55, 14, 9, 7, 72, 52], 32, 69))
    # 3
    print(Solution().numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))
    # 7
    print(Solution().numSubarrayBoundedMax([2, 9, 2, 5, 6], 2, 8))
