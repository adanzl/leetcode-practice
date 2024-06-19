"""
 * 如果数组的每一对相邻元素都是两个奇偶性不同的数字，则该数组被认为是一个 特殊数组 。
 * Aging 有一个整数数组 nums。如果 nums 是一个 特殊数组 ，返回 true，否则返回 false。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 100
 * 链接：https://leetcode.cn/problems/special-array-i/
"""
from typing import List


class Solution:

    def isArraySpecial(self, nums: List[int]) -> bool:
        ans = nums[0] % 2
        for i in range(1, len(nums)):
            if ans == nums[i] % 2: return False
            ans = nums[i] % 2
        return True


if __name__ == '__main__':
    # True
    print(Solution().isArraySpecial([2]))
    # True
    print(Solution().isArraySpecial([1]))
    # True
    print(Solution().isArraySpecial([2, 1, 4]))
    # False
    print(Solution().isArraySpecial([4, 3, 1, 6]))
