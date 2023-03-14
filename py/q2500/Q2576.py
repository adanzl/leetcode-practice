"""
 * 给你一个下标从 0 开始的整数数组 nums 。
 * 一开始，所有下标都没有被标记。你可以执行以下操作任意次：
 * 选择两个 互不相同且未标记 的下标 i 和 j ，满足 2 * nums[i] <= nums[j] ，标记下标 i 和 j 。
 * 请你执行上述操作任意次，返回 nums 中最多可以标记的下标数目。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/
"""
from typing import List


class Solution:

    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        l, r = 0, n // 2 - 1
        while l <= r:  # 最小的k个数和最大的k个数匹配
            mid = (l + r) // 2
            if all([nums[i] * 2 <= nums[n - 1 - mid + i] for i in range(mid + 1)]):
                ans = mid + 1
                l = mid + 1
            else:
                r = mid - 1
        return ans * 2


if __name__ == '__main__':
    # 26
    print(Solution().maxNumOfMarkedIndices([42, 83, 48, 10, 24, 55, 9, 100, 10, 17, 17, 99, 51, 32, 16, 98, 99, 31, 28, 68, 71, 14, 64, 29, 15, 40]))
    # 0
    print(Solution().maxNumOfMarkedIndices([7, 6, 8]))
    # 4
    print(Solution().maxNumOfMarkedIndices([9, 2, 5, 4]))
    # 2
    print(Solution().maxNumOfMarkedIndices([3, 5, 2, 4]))
