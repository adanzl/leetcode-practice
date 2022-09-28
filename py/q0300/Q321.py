"""
 * 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
 * 求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
 * 说明: 请尽可能地优化你算法的时间和空间复杂度。
 * 链接：https://leetcode.cn/problems/create-maximum-number/
"""
from typing import *


class Solution:

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def max_num(nums, count):
            if count <= 0:
                return []
            ans = [0] * count
            remain, top = len(nums) - count, -1
            for i in range(len(nums)):
                while top >= 0 and ans[top] < nums[i] and remain > 0:
                    top -= 1
                    remain -= 1
                if top < count - 1:
                    top += 1
                    ans[top] = nums[i]
                else:
                    remain -= 1
            return ans

        def compare(n1, i1, n2, i2):
            e1, e2 = len(n1), len(n2)
            while i1 < e1 and i2 < e2:
                diff = n1[i1] - n2[i2]
                if diff != 0:
                    return diff
                i1 += 1
                i2 += 1
            return (e1 - i1) - (e2 - i2)

        def merge(n1, n2):
            n = len(n1) + len(n2)
            ans = [0] * n
            i1, i2, i = 0, 0, 0
            while i1 < len(n1) and i2 < len(n2):
                if compare(n1, i1, n2, i2) > 0:
                    ans[i] = n1[i1]
                    i1 += 1
                else:
                    ans[i] = n2[i2]
                    i2 += 1
                i += 1
            while i1 < len(n1):
                ans[i] = n1[i1]
                i += 1
                i1 += 1
            while i2 < len(n2):
                ans[i] = n2[i2]
                i += 1
                i2 += 1
            return ans

        ans = []
        l1, l2 = len(nums1), len(nums2)
        for i in range(max(k - l2, 0), min(k, l1) + 1):
            arr = merge(max_num(nums1, i), max_num(nums2, k - i))
            if arr > ans:
                ans = arr
        return ans


if __name__ == "__main__":
    # [6, 7, 6, 0, 4]
    print(Solution().maxNumber([6, 7], [6, 0, 4], 5))
    # [1,1]
    print(Solution().maxNumber([1, 1, 1], [1, 1, 1], 2))
    # [9, 8, 6, 5, 3]
    print(Solution().maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
    # [9, 8, 9]
    print(Solution().maxNumber([3, 9], [8, 9], 3))
