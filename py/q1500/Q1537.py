"""
 * 你有两个 有序 且数组内元素互不相同的数组 nums1 和 nums2 。
 * 一条 合法路径 定义如下：
 * 1、选择数组 nums1 或者 nums2 开始遍历（从下标 0 处开始）。
 * 2、从左到右遍历当前数组。
 * 3、如果你遇到了 nums1 和 nums2 中都存在的值，那么你可以切换路径到另一个数组对应数字处继续遍历（但在合法路径中重复数字只会被统计一次）。
 * 得分定义为合法路径中不同数字的和。
 * 请你返回所有可能合法路径中的最大得分。
 * 由于答案可能很大，请你将它对 10^9 + 7 取余后返回。
 * 提示：
 * 1、1 <= nums1.length <= 10^5
 * 2、1 <= nums2.length <= 10^5
 * 3、1 <= nums1[i], nums2[i] <= 10^7
 * 4、nums1 和 nums2 都是严格递增的数组。
 * 链接：https://leetcode.cn/problems/get-the-maximum-score/
"""
from typing import List


class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10**9 + 7
        m, n = len(nums1), len(nums2)
        best1 = best2 = 0
        i = j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                best1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                best2 += nums2[j]
                j += 1
            else:
                best = max(best1, best2) + nums1[i]
                best1 = best2 = best
                i += 1
                j += 1
        while i < m:
            best1 += nums1[i]
            i += 1
        while j < n:
            best2 += nums2[j]
            j += 1

        return max(best1, best2) % mod


if __name__ == '__main__':
    # 40
    print(Solution().maxSum([1, 2, 3, 4, 5], nums2=[6, 7, 8, 9, 10]))
    # 30
    print(Solution().maxSum([2, 4, 5, 8, 10], nums2=[4, 6, 8, 9]))
    # 109
    print(Solution().maxSum([1, 3, 5, 7, 9], nums2=[3, 5, 100]))
    # 61
    print(Solution().maxSum([1, 4, 5, 8, 9, 11, 19], nums2=[2, 3, 4, 11, 12]))
