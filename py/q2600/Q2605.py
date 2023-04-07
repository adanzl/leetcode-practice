"""
 * 给你两个只包含 1 到 9 之间数字的数组 nums1 和 nums2 ，每个数组中的元素 互不相同 ，请你返回 最小 的数字，两个数组都 至少 包含这个数字的某个数位。
 * 提示：
 * 1、1 <= nums1.length, nums2.length <= 9
 * 2、1 <= nums1[i], nums2[i] <= 9
 * 3、每个数组中，元素 互不相同 。
 * 链接：https://leetcode.cn/problems/form-smallest-number-from-two-digit-arrays/
"""
from typing import List


class Solution:

    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s = set(nums1).intersection(set(nums2))
        if s: return min(s)
        n1, n2 = min(nums1), min(nums2)
        return min(n1, n2) * 10 + max(n1, n2)


if __name__ == '__main__':
    # 15
    print(Solution().minNumber([4, 1, 3], nums2=[5, 7]))
    # 3
    print(Solution().minNumber([3, 5, 2, 6], nums2=[3, 1, 7]))
