"""
 * 给你一个下标从 0 开始的 正 整数数组 nums 。你可以对数组执行以下操作 任意 次：
 * 选择一个满足 0 <= i < n - 1 的下标 i ，将 nums[i] 或者 nums[i+1] 两者之一替换成它们的最大公约数。
 * 请你返回使数组 nums 中所有元素都等于 1 的 最少 操作次数。如果无法让数组全部变成 1 ，请你返回 -1 。
 * 两个正整数的最大公约数指的是能整除这两个数的最大正整数。
 * 提示：
 * 1、2 <= nums.length <= 50
 * 2、1 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/
"""
from math import gcd
from typing import List


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        if gcd(*nums) > 1:
            return -1
        n = len(nums)
        cnt1 = sum(x == 1 for x in nums)
        if cnt1: return n - cnt1
        min_size = n
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    # 这里本来是 j-i+1，把 +1 提出来合并到 return 中
                    min_size = min(min_size, j - i)
                    break
        return min_size + n - 1


if __name__ == '__main__':
    # 4
    print(Solution().minOperations([2, 6, 3, 4]))
    # -1
    print(Solution().minOperations([2, 10, 6, 14]))
    #
    # print(Solution().minOperations())