"""
 * 给你两个长度可能不等的整数数组 nums1 和 nums2 。两个数组中的所有值都在 1 到 6 之间（包含 1 和 6）。
 * 每次操作中，你可以选择 任意 数组中的任意一个整数，将它变成 1 到 6 之间 任意 的值（包含 1 和 6）。
 * 请你返回使 nums1 中所有数的和与 nums2 中所有数的和相等的最少操作次数。如果无法使两个数组的和相等，请返回 -1 。
 * 提示：
 * 1、1 <= nums1.length, nums2.length <= 10^5
 * 2、1 <= nums1[i], nums2[i] <= 6
 * 链接：https://leetcode.cn/problems/equal-sum-arrays-with-minimum-number-of-operations/
"""
from typing import List


class Solution:

    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sm1, sm2 = sum(nums1), sum(nums2)
        n1, n2 = len(nums1), len(nums2)
        if sm1 < sm2:
            n2, n1 = n1, n2
            sm2, sm1 = sm1, sm2
            nums2, nums1 = nums1, nums2
        d = sm1 - sm2
        nums1.sort(reverse=True)
        nums2.sort()
        i1, i2 = 0, 0
        ans = 0
        while i1 < n1 and i2 < n2 and d:
            if nums1[i1] - 1 >= 6 - nums2[i2]:
                d -= min(d, nums1[i1] - 1)
                i1 += 1
            else:
                d -= min(d, 6 - nums2[i2])
                i2 += 1
            ans += 1
        while i1 < n1 and d:
            d -= min(d, nums1[i1] - 1)
            i1 += 1
            ans += 1
        while i2 < n2 and d:
            d -= min(d, 6 - nums2[i2])
            i2 += 1
            ans += 1
        return ans if d == 0 else -1


if __name__ == '__main__':
    # 4
    print(Solution().minOperations([5, 6, 4, 3, 1, 2], [6, 3, 3, 1, 4, 5, 3, 4, 1, 3, 4]))
    # 3
    print(Solution().minOperations([1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 2, 2]))
    # -1
    print(Solution().minOperations([1, 1, 1, 1, 1, 1, 1], [6]))
    # 3
    print(Solution().minOperations([6, 6], [1]))
