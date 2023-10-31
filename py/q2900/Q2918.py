"""
 * 给你两个由正整数和 0 组成的数组 nums1 和 nums2 。
 * 你必须将两个数组中的 所有 0 替换为 严格 正整数，并且满足两个数组中所有元素的和 相等 。
 * 返回 最小 相等和 ，如果无法使两数组相等，则返回 -1 。
 * 提示：
 * 1、1 <= nums1.length, nums2.length <= 10^5
 * 2、0 <= nums1[i], nums2[i] <= 10^6
 * 链接：https://leetcode.cn/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
"""
from typing import List


class Solution:

    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sm0, z0, sm1, z1 = 0, 0, 0, 0
        for num in nums1:
            if num == 0:
                z0 += 1
                sm0 += 1
            else:
                sm0 += num
        for num in nums2:
            if num == 0:
                z1 += 1
                sm1 += 1
            else:
                sm1 += num
        if sm0 > sm1:
            sm0, z0, sm1, z1 = sm1, z1, sm0, z0
        if sm0 != sm1 and z0 == 0: return -1
        return sm1


if __name__ == '__main__':
    # 12
    print(Solution().minSum([3, 2, 0, 1, 0], nums2=[6, 5, 0]))
    # -1
    print(Solution().minSum([2, 0, 2, 0], nums2=[1, 4]))
    #
    # print(Solution().minSum())