"""
 * 给出非负整数数组 A ，返回两个非重叠（连续）子数组中元素的最大和，子数组的长度分别为 L 和 M。（这里需要澄清的是，长为 L 的子数组可以出现在长为 M 的子数组之前或之后。）
 * 从形式上看，返回最大的 V，而 V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) 并满足下列条件之一：
 * 1、0 <= i < i + L - 1 < j < j + M - 1 < A.length, 或
 * 2、0 <= j < j + M - 1 < i < i + L - 1 < A.length.
 * 提示：
 * 1、L >= 1
 * 2、M >= 1
 * 3、L + M <= A.length <= 1000
 * 4、0 <= A[i] <= 1000
 * 链接：https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/
"""
from itertools import accumulate
from typing import List


class Solution:

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        pre_sum = [0] + list(accumulate(nums))
        ans = 0
        for i in range(n - firstLen + 1):
            v1 = pre_sum[i + firstLen] - pre_sum[i]
            v2 = 0
            for j in range(i - secondLen + 1):
                v2 = max(v2, pre_sum[j + secondLen] - pre_sum[j])
            for j in range(i + firstLen, n - secondLen + 1):
                v2 = max(v2, pre_sum[j + secondLen] - pre_sum[j])
            ans = max(ans, v1 + v2)
        return ans


if __name__ == '__main__':
    # 131
    print(Solution().maxSumTwoNoOverlap([12, 8, 12, 18, 19, 10, 17, 20, 6, 8, 13, 1, 19, 11, 5], 3, 6))
    # 31
    print(Solution().maxSumTwoNoOverlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3))
    # 20
    print(Solution().maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2))
    # 29
    print(Solution().maxSumTwoNoOverlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2))
