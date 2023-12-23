"""
 * 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，它们分别含有 n 和 m 个元素。
 * 请你计算以下两个数值：
 * 1、统计 0 <= i < n 中的下标 i ，满足 nums1[i] 在 nums2 中 至少 出现了一次。
 * 2、统计 0 <= i < m 中的下标 i ，满足 nums2[i] 在 nums1 中 至少 出现了一次。
 * 请你返回一个长度为 2 的整数数组 answer ，按顺序 分别为以上两个数值。
 * 提示：
 * 1、n == nums1.length
 * 2、m == nums2.length
 * 3、1 <= n, m <= 100
 * 4、1 <= nums1[i], nums2[i] <= 100
 * 链接：https://leetcode.cn/problems/find-common-elements-between-two-arrays/
"""
from typing import List


class Solution:

    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [sum([1 for num in nums1 if num in nums2]), sum([1 for num in nums2 if num in nums1])]


if __name__ == '__main__':
    # [3,4]
    print(Solution().findIntersectionValues([4, 3, 2, 3, 1], nums2=[2, 2, 5, 2, 3, 6]))
    # [0,0]
    print(Solution().findIntersectionValues([3, 4, 2, 3], nums2=[1, 5]))
