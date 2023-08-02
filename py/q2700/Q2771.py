"""
 * 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，长度均为 n 。
 * 让我们定义另一个下标从 0 开始、长度为 n 的整数数组，nums3 。
 * 对于范围 [0, n - 1] 的每个下标 i ，你可以将 nums1[i] 或 nums2[i] 的值赋给 nums3[i] 。
 * 你的任务是使用最优策略为 nums3 赋值，以最大化 nums3 中 最长非递减子数组 的长度。
 * 以整数形式表示并返回 nums3 中 最长非递减 子数组的长度。
 * 注意：子数组 是数组中的一个连续非空元素序列。
 * 提示：
 * 1、1 <= nums1.length == nums2.length == n <= 10^5
 * 2、1 <= nums1[i], nums2[i] <= 10^9
 * 链接：https://leetcode.cn/problems/longest-non-decreasing-subarray-from-two-arrays/
"""
from typing import List


class Solution:

    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 1
        dp = [1, 1]  # 0-1
        n = len(nums1)
        for i in range(1, n):
            ndp = [1, 1]
            if nums1[i] >= nums1[i - 1]:
                ndp[0] = max(ndp[0], dp[0] + 1)
            if nums1[i] >= nums2[i - 1]:
                ndp[0] = max(ndp[0], dp[1] + 1)
            if nums2[i] >= nums1[i - 1]:
                ndp[1] = max(ndp[1], dp[0] + 1)
            if nums2[i] >= nums2[i - 1]:
                ndp[1] = max(ndp[1], dp[1] + 1)
            dp = ndp
            ans = max(ans, max(dp))

        return ans


if __name__ == '__main__':
    # 2
    print(Solution().maxNonDecreasingLength([2, 3, 1], nums2=[1, 2, 1]))
    # 4
    print(Solution().maxNonDecreasingLength([1, 3, 2, 1], nums2=[2, 2, 3, 4]))
    # 2
    print(Solution().maxNonDecreasingLength([1, 1], nums2=[2, 2]))
