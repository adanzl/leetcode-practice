"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 value 。
 * 在一步操作中，你可以对 nums 中的任一元素加上或减去 value 。
 * 例如，如果 nums = [1,2,3] 且 value = 2 ，你可以选择 nums[0] 减去 value ，得到 nums = [-1,2,3] 。
 * 数组的 MEX (minimum excluded) 是指其中数组中缺失的最小非负整数。
 * 例如，[-1,2,3] 的 MEX 是 0 ，而 [1,0,3] 的 MEX 是 2 。
 * 返回在执行上述操作 任意次 后，nums 的最大 MEX 。
 * 提示：
 * 1、1 <= nums.length, value <= 10^5
 * 2、-10^9 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/smallest-missing-non-negative-integer-after-operations/
"""
from typing import List


class Solution:

    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        nums = sorted([num % value for num in nums])
        nn = 0
        sign = {}
        for i in range(len(nums)):
            v = nums[i]
            if v in sign:
                v = sign[v] + value
            sign[nums[i]] = v
            sign[v] = v
        while True:
            if nn not in sign:
                return nn
            nn += 1


if __name__ == '__main__':
    # 4
    print(Solution().findSmallestInteger([1, -10, 7, 13, 6, 8], value=5))
    # 2
    print(Solution().findSmallestInteger([1, -10, 7, 13, 6, 8], value=7))
    #
    # print(Solution().findSmallestInteger())