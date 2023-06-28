"""
 * 给你一个整数数组 nums ，数组由 不同正整数 组成，请你找出并返回数组中 任一 既不是 最小值 也不是 最大值 的数字，如果不存在这样的数字，返回 -1 。
 * 返回所选整数。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 100
 * 3、nums 中的所有数字互不相同
 * 链接：https://leetcode.cn/problems/neither-minimum-nor-maximum/
"""
from typing import List


class Solution:

    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        return sorted(nums)[1]


if __name__ == '__main__':
    # 2
    print(Solution().findNonMinOrMax([3, 2, 1, 4]))
    # -1
    print(Solution().findNonMinOrMax([1, 2]))
    # 2
    print(Solution().findNonMinOrMax([2, 1, 3]))
