"""
 * 给你一个整数数组 nums 和一个 非负 整数 k 。
 * 一次操作中，你可以选择任一下标 i ，然后将 nums[i] 加 1 或者减 1 。
 * 请你返回将 nums 中位数 变为 k 所需要的 最少 操作次数。
 * 一个数组的 中位数 指的是数组按 非递减 顺序排序后最中间的元素。如果数组长度为偶数，我们选择中间两个数的较大值为中位数。
 * 提示：
 * 1、1 <= nums.length <= 2 * 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= k <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-operations-to-make-median-of-array-equal-to-k
"""
from typing import List


class Solution:

    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, n = 0, len(nums)
        for i in range(n // 2, n):
            if nums[i] < k:
                ans += k - nums[i]
            else:
                break
        for i in range(n // 2, -1, -1):
            if nums[i] > k:
                ans += nums[i] - k
            else:
                break
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().minOperationsToMakeMedianK([2, 5, 6, 8, 5], k=4))
    # 3
    print(Solution().minOperationsToMakeMedianK([2, 5, 6, 8, 5], k=7))
    # 0
    print(Solution().minOperationsToMakeMedianK([1, 2, 3, 4, 5, 6], k=4))
