"""
 * 给你两个正整数 left 和 right ，请你找到两个整数 num1 和 num2 ，它们满足：
 * 1、left <= nums1 < nums2 <= right  。
 * 2、nums1 和 nums2 都是 质数 。
 * 3、nums2 - nums1 是满足上述条件的质数对中的 最小值 。
 * 请你返回正整数数组 ans = [nums1, nums2] 。如果有多个整数对满足上述条件，请你返回 nums1 最小的质数对。如果不存在符合题意的质数对，请你返回 [-1, -1] 。
 * 如果一个整数大于 1 ，且只能被 1 和它自己整除，那么它是一个质数。
 * 提示：1 <= left <= right <= 10^6
 * 链接：https://leetcode.cn/problems/closest-prime-numbers-in-range/
"""

from typing import List


class Solution:

    def closestPrimes(self, left: int, right: int) -> List[int]:
        LIMIT = 10**6 + 5
        # 线性筛选质数
        b_prime = [False] * LIMIT
        prime_list = []
        ans = [-1, -1]
        mn = LIMIT
        for i in range(2, right + 5):
            if not b_prime[i]:
                if prime_list and left <= prime_list[-1] < i <= right:
                    if i - prime_list[-1] < mn:
                        mn = i - prime_list[-1]
                        ans = [prime_list[-1], i]
                prime_list.append(i)

            for prime in prime_list:
                next = prime * i
                if next < LIMIT:
                    b_prime[next] = True
                else:
                    break
        return ans


if __name__ == '__main__':
    # [11, 13]
    print(Solution().closestPrimes(10, 19))
    # [-1, -1]
    print(Solution().closestPrimes(4, 6))