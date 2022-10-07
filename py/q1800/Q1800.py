"""
 * 给你一个正整数组成的数组 nums ，返回 nums 中一个 升序 子数组的最大可能元素和。
 * 子数组是数组中的一个连续数字序列。
 * 已知子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，若对所有 i（l <= i < r），numsi < numsi+1 都成立，则称这一子数组为 升序 子数组。
 * 注意，大小为 1 的子数组也视作 升序 子数组。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 100
 * 链接：https://leetcode.cn/problems/maximum-ascending-subarray-sum/
"""
from typing import List


class Solution:

    def maxAscendingSum(self, nums: List[int]) -> int:
        ans, sm, pre = 0, 0, 0
        for num in nums:
            if num > pre:
                sm += num
            else:
                sm = num
            pre = num
            ans = max(ans, sm)
        return ans


if __name__ == '__main__':
    # 65
    print(Solution().maxAscendingSum([10, 20, 30, 5, 10, 50]))
    # 150
    print(Solution().maxAscendingSum([10, 20, 30, 40, 50]))
    # 33
    print(Solution().maxAscendingSum([12, 17, 15, 13, 10, 11, 12]))
    # 100
    print(Solution().maxAscendingSum([100, 10, 1]))
