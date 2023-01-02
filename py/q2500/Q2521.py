"""
 * 给你一个正整数数组 nums ，对 nums 所有元素求积之后，找出并返回乘积中 不同质因数 的数目。
 * 注意：
 * 1、质数 是指大于 1 且仅能被 1 及自身整除的数字。
 * 2、如果 val2 / val1 是一个整数，则整数 val1 是另一个整数 val2 的一个因数。
 * 提示：
 * 1、1 <= nums.length <= 10^4
 * 2、2 <= nums[i] <= 1000
 * 链接：https://leetcode.cn/problems/distinct-prime-factors-of-product-of-array/
"""
from typing import List


class Solution:

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        ans = set()
        for num in nums:
            p = 2
            while p * p <= num:
                if num % p == 0:
                    while num % p == 0:
                        num //= p
                    ans.add(p)
                else:
                    p += 1
            if num > 1:
                ans.add(num)
        return len(ans)


if __name__ == '__main__':
    # 4
    print(Solution().distinctPrimeFactors([2, 4, 3, 7, 10, 6]))
    # 1
    print(Solution().distinctPrimeFactors([2, 4, 8, 16]))
