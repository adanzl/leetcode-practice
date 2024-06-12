"""
 * 给你两个整数数组 nums1 和 nums2，长度分别为 n 和 m。同时给你一个正整数 k。
 * 如果 nums1[i] 可以被 nums2[j] * k 整除，则称数对 (i, j) 为 优质数对（0 <= i <= n - 1, 0 <= j <= m - 1）。
 * 返回 优质数对 的总数。
 * 提示：
 * 1、1 <= n, m <= 10^5
 * 2、1 <= nums1[i], nums2[j] <= 10^6
 * 3、1 <= k <= 10^3
 * 链接：https://leetcode.cn/problems/find-the-number-of-good-pairs-ii/
"""
from collections import Counter
from math import isqrt
from typing import List


class Solution:

    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt = Counter()
        for n1 in nums1:
            if n1 % k: continue
            n1 //= k
            for v in range(1, isqrt(n1) + 1):
                if n1 % v != 0: continue
                cnt[v] += 1
                if v * v < n1:
                    cnt[n1 // v] += 1
        return sum([cnt[x] for x in nums2])


if __name__ == '__main__':
    # 5
    print(Solution().numberOfPairs([1, 3, 4], nums2=[1, 3, 4], k=1))
    # 2
    print(Solution().numberOfPairs([1, 2, 4, 12], nums2=[2, 4], k=3))
