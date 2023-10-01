"""
 * 给你一个下标从 0 开始的正整数数组 nums 。
 * 你可以对数组执行以下两种操作 任意次 ：
 * 1、从数组中选择 两个 值 相等 的元素，并将它们从数组中 删除 。
 * 2、从数组中选择 三个 值 相等 的元素，并将它们从数组中 删除 。
 * 请你返回使数组为空的 最少 操作次数，如果无法达成，请返回 -1 。
 * 提示：
 * 1、2 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/split-array-into-maximum-number-of-subarrays/
"""
from typing import List


class Solution:

    def maxSubarrays(self, nums: List[int]) -> int:
        av = reduce(and_, nums)
        if av != 0: return 1
        ans = 0
        v = nums[0]
        for i in range(1, len(nums)):
            if v == 0:
                ans += 1
                v = nums[i]
            else:
                v &= nums[i]
        if v == av: ans += 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().maxSubarrays([1, 0, 2, 0, 1, 2]))
    # 1
    print(Solution().maxSubarrays([5, 7, 1, 3]))
