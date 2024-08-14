"""
 * 给你两个 从小到大排好序 且下标从 0 开始的整数数组 nums1 和 nums2 以及一个整数 k ，
 * 请你返回第 k （从 1 开始编号）小的 nums1[i] * nums2[j] 的乘积，
 * 其中 0 <= i < nums1.length 且 0 <= j < nums2.length 。
 * 提示：
 * 1、1 <= nums1.length, nums2.length <= 5 * 10^4
 * 2、-10^5 <= nums1[i], nums2[j] <= 10^5
 * 3、1 <= k <= nums1.length * nums2.length
 * 4、nums1 和 nums2 都是从小到大排好序的。
 * 链接：https://leetcode.cn/problems/kth-smallest-product-of-two-sorted-arrays/
"""

import bisect
from typing import List
import math

#
# @lc app=leetcode.cn id=2040 lang=python3
#
# [2040] 两个有序数组的第 K 小乘积
#


# @lc code=start
class Solution:

    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums_neg1, nums_neg2, nums_pos1, nums_pos2 = [], [], [], []
        z1, z2 = 0, 0
        for num in nums1:
            if num == 0: z1 += 1
            if num < 0: nums_neg1.append(num)
            if num > 0: nums_pos1.append(num)
        for num in nums2:
            if num == 0: z2 += 1
            if num < 0: nums_neg2.append(num)
            if num > 0: nums_pos2.append(num)
        neg_size = len(nums_neg1) * len(nums_pos2) + len(nums_neg2) * len(nums_pos1)
        z_size = z1 * len(nums2) + z2 * len(nums1) - z1 * z2
        if neg_size < k <= neg_size + z_size:
            return 0
        if k <= neg_size:
            lo, hi = 0, 0
            if nums_neg1 and nums_pos2:
                lo = min(nums_neg1[0] * nums_pos2[-1], lo)
            if nums_neg2 and nums_pos1:
                lo = min(nums_neg2[0] * nums_pos1[-1], lo)
            while lo < hi:
                mid = (lo + hi) // 2
                val = 0
                for num in nums_pos1:
                    ii = bisect.bisect_right(nums_neg2, (mid // num))
                    val += ii
                for num in nums_pos2:
                    ii = bisect.bisect_right(nums_neg1, (mid // num))
                    val += ii
                if val >= k:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        else:
            lo, hi = 0, 0
            if nums_neg1 and nums_neg2:
                hi = max(nums_neg1[0] * nums_neg2[0], hi)
            if nums_pos2 and nums_pos1:
                hi = max(nums_pos2[-1] * nums_pos1[-1], hi)
            while lo < hi:
                mid = (lo + hi) // 2
                val = 0
                for num in nums_pos1:
                    ii = bisect.bisect_right(nums_pos2, mid // num)
                    val += ii
                for num in nums_neg2:
                    ii = bisect.bisect_left(nums_neg1, math.trunc(mid / num))
                    val += len(nums_neg1) - ii
                if val >= k - z_size - neg_size:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        return -1


# @lc code=end

if __name__ == '__main__':
    # 54
    print(Solution().kthSmallestProduct([-6], nums2=[-9], k=1))
    # 10
    print(Solution().kthSmallestProduct([-9, 6, 10], [-7, -1, 1, 2, 3, 4, 4, 6, 9, 10], 15))
    # -6
    print(Solution().kthSmallestProduct([-2, -1, 0, 1, 2], nums2=[-3, -1, 2, 4, 5], k=3))
    # 8
    print(Solution().kthSmallestProduct([2, 5], nums2=[3, 4], k=2))
    # 0
    print(Solution().kthSmallestProduct([-4, -2, 0, 3], nums2=[2, 4], k=6))
