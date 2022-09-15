from typing import *
"""
 * 我们有两个长度相等且不为空的整型数组 nums1 和 nums2 。在一次操作中，我们可以交换 nums1[i] 和 nums2[i]的元素。
 * 例如，如果 nums1 = [1,2,3,8] ， nums2 =[5,6,7,4] ，你可以交换 i = 3 处的元素，得到 nums1 =[1,2,3,4] 和 nums2 =[5,6,7,8] 。
 * 返回 使 nums1 和 nums2 严格递增 所需操作的最小次数 。
 * 数组 arr 严格递增 且  arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1] 。
 * 注意：用例保证可以实现操作。
 * 提示:
 * 1、2 <= nums1.length <= 10^5
 * 2、nums2.length == nums1.length
 * 3、0 <= nums1[i], nums2[i] <= 2 * 10^5
 * 链接：https://leetcode.cn/problems/minimum-swaps-to-make-sequences-increasing
"""


class Solution:

    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [0, 1]  # 1-2, 2-1
        n = len(nums1)
        mx01, mx02 = mx12, mx11 = nums1[0], nums2[0]
        for i in range(1, n):
            d0, d1 = dp
            dp = [0x3c3c3c3c, 0x3c3c3c3c]
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                dp[0] = min(dp[0], d0)
                dp[1] = min(dp[1], d1 + 1)
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                dp[0] = min(dp[0], d1)
                dp[1] = min(dp[1], d0 + 1)
        return min(dp)


if __name__ == '__main__':
    # 1
    print(Solution().minSwap([3, 3, 8, 9, 10], [1, 7, 4, 6, 8]))
    # 6
    print(Solution().minSwap([2, 1, 6, 9, 10, 13, 13, 16, 19, 26, 23, 24, 25, 27, 32, 31, 35, 36, 37, 39], [0, 5, 8, 8, 10, 12, 14, 15, 22, 22, 28, 29, 30, 31, 30, 33, 33, 36, 37, 38]))
    # 1
    print(Solution().minSwap([1, 3, 5, 4, 9], [1, 2, 3, 7, 10]))
    # 1
    print(Solution().minSwap([1, 3, 5, 4], [1, 2, 3, 7]))
    # 1
    print(Solution().minSwap([0, 3, 5, 8, 9], [2, 1, 4, 6, 9]))
