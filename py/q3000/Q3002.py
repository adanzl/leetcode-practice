"""
 * 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，它们的长度都是偶数 n 。
 * 你必须从 nums1 中移除 n / 2 个元素，同时从 nums2 中也移除 n / 2 个元素。
 * 移除之后，你将 nums1 和 nums2 中剩下的元素插入到集合 s 中。
 * 返回集合 s 可能的 最多 包含多少元素。
 * 提示：
 * 1、n == nums1.length == nums2.length
 * 2、1 <= n <= 2 * 10^4
 * 3、n是偶数。
 * 4、1 <= nums1[i], nums2[i] <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-size-of-a-set-after-removals/
"""
from typing import List


class Solution:

    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1) // 2
        st1, st2 = set(nums1), set(nums2)
        share = 0
        for num in st1:
            if num in st2:
                share += 1
        v1, v2 = min(n, len(st1) - share), min(n, len(st2) - share)
        s1, s2 = len(st1) - v1, len(st2) - v2
        t1, t2 = min(n - v1, s1), min(n - v2, s2)
        return v1 + v2 + min(t1 + t2, share)


if __name__ == '__main__':
    # 2
    print(Solution().maximumSetSize([1, 2, 1, 2], nums2=[1, 1, 1, 1]))
    # 4
    print(Solution().maximumSetSize([2, 4, 1, 4], [10, 2, 4, 10]))
    # 5
    print(Solution().maximumSetSize([1, 2, 3, 4, 5, 6], nums2=[2, 3, 2, 3, 2, 3]))
    # 6
    print(Solution().maximumSetSize([1, 1, 2, 2, 3, 3], nums2=[4, 4, 5, 5, 6, 6]))
