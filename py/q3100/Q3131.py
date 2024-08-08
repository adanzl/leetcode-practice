"""
 * 给你两个长度相等的数组 nums1 和 nums2。
 * 数组 nums1 中的每个元素都与变量 x 所表示的整数相加。如果 x 为负数，则表现为元素值的减少。
 * 在与 x 相加后，nums1 和 nums2 相等 。当两个数组中包含相同的整数，并且这些整数出现的频次相同时，两个数组 相等 。
 * 返回整数 x 。
 * 提示：
 * 1、1 <= nums1.length == nums2.length <= 100
 * 2、0 <= nums1[i], nums2[i] <= 1000
 * 3、测试用例以这样的方式生成：存在一个整数 x，使得 nums1 中的每个元素都与 x 相加后，nums1 与 nums2 相等。
 * 链接：https://leetcode.cn/problems/find-the-integer-added-to-array-i
"""

from typing import List

#
# @lc app=leetcode.cn id=3131 lang=python3
#
# [3131] 找出与数组相加的整数 I
#


# @lc code=start
class Solution:

    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return sorted(nums2)[0] - sorted(nums1)[0]


# @lc code=end

if __name__ == '__main__':
    # 3
    print(Solution().addedInteger([2, 6, 4], nums2=[9, 7, 5]))
    # -1
    print(Solution().addedInteger([10], nums2=[5]))
    # 0
    print(Solution().addedInteger([1, 1, 1, 1], nums2=[1, 1, 1, 1]))
