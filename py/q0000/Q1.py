"""
 * 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
 * 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
 * 你可以按任意顺序返回答案。
 * 提示：
 * 1、2 <= nums.length <= 10^4
 * 2、-10^9 <= nums[i] <= 10^9
 * 3、-10^9 <= target <= 10^9
 * 4、只会存在一个有效答案
 * 链接：https://leetcode.cn/problems/two-sum/
"""
from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
            if target - n in m:
                return [m[target - n], i]
            m[n] = i
        return []


if __name__ == '__main__':
    # [0, 1]
    print(Solution().twoSum([2, 7, 11, 15], target=9))
    # [1, 2]
    print(Solution().twoSum([3, 2, 4], target=6))
    # [0, 1]
    print(Solution().twoSum([3, 3], target=6))
