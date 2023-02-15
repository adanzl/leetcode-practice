"""
 * 给你一个由正整数组成的数组 nums 。
 * 数字序列的 最大公约数 定义为序列中所有整数的共有约数中的最大整数。
 * 例如，序列 [4,6,16] 的最大公约数是 2 。
 * 数组的一个 子序列 本质是一个序列，可以通过删除数组中的某些元素（或者不删除）得到。
 * 例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
 * 计算并返回 nums 的所有 非空 子序列中 不同 最大公约数的 数目 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 2 * 10^5
 * 链接：https://leetcode.cn/problems/number-of-different-subsequences-gcds/
"""
from typing import List
from math import gcd


class Solution:

    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        ans, mx = 0, max(nums)
        has = [False] * (mx + 1)
        for x in nums:
            has[x] = True
        for i in range(1, mx + 1):
            g = 0  # 0 和任何数 x 的最大公约数都是 x
            for j in range(i, mx + 1, i):  # 枚举 i 的倍数 j
                if has[j]:  # 如果 j 在 nums 中
                    g = gcd(g, j)  # 更新最大公约数
                    if g == i:  # 找到一个答案（g 无法继续减小）
                        ans += 1
                        break  # 提前退出循环
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().countDifferentSubsequenceGCDs([6, 10, 3]))
    # 7
    print(Solution().countDifferentSubsequenceGCDs([5, 15, 40, 5, 6]))