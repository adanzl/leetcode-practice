"""
 * 给你一个下标从 0 开始的二维整数数组 nums 。
 * 返回位于 nums 至少一条 对角线 上的最大 质数 。如果任一对角线上均不存在质数，返回 0 。
 * 注意：
 * 1、如果某个整数大于 1 ，且不存在除 1 和自身之外的正整数因子，则认为该整数是一个质数。
 * 2、如果存在整数 i ，使得 nums[i][i] = val 或者 nums[i][nums.length - i - 1]= val ，则认为整数 val 位于 nums 的一条对角线上。
 * 提示：
 * 1、1 <= nums.length <= 300
 * 2、nums.length == nums_i.length
 * 3、1 <= nums[i][j] <= 4*10^6
 * 链接：https://leetcode.cn/problems/prime-in-diagonal/
"""
import math
from typing import List


class Solution:

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)

        def is_prime(x):
            if x == 1: return False
            for i in range(2, int(math.sqrt(x) + 1)):
                if x % i == 0:
                    return False
            return True

        ans = 0
        for i in range(n):
            if is_prime(nums[i][i]):
                ans = max(ans, nums[i][i])
            if is_prime(nums[i][n - i - 1]):
                ans = max(ans, nums[i][n - i - 1])
        return ans


if __name__ == '__main__':
    # 11
    print(Solution().diagonalPrime([[1, 2, 3], [5, 6, 7], [9, 10, 11]]))
    # 17
    print(Solution().diagonalPrime([[1, 2, 3], [5, 17, 7], [9, 11, 10]]))
