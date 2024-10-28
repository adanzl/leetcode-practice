"""
 * 给你一个整数数组 nums 。
 * 一个正整数 x 的任何一个 严格小于 x 的 正 因子都被称为 x 的 真因数 。比方说 2 是 4 的 真因数，但 6 不是 6 的 真因数。
 * 你可以对 nums 的任何数字做任意次 操作 ，一次 操作 中，你可以选择 nums 中的任意一个元素，将它除以它的 最大真因数 。
 * 你的目标是将数组变为 非递减 的，请你返回达成这一目标需要的 最少操作 次数。
 * 如果 无法 将数组变成非递减的，请你返回 -1 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/minimum-division-operations-to-make-array-non-decreasing/
"""
from functools import cache
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


@cache
def prime_map(x):
    # 分解质因数
    p, num, p_map = 2, x, {}
    while p * p <= num:
        if num % p == 0:
            x = 0
            while num % p == 0:
                num //= p
                x += 1
            p_map[p] = p_map.get(p, 0) + x
        else:
            p += 1
    if num > 1:
        p_map[num] = 1
    return p_map


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i + 1]:
                p_map = prime_map(nums[i])
                nums[i] = min(p_map.keys())
                ans += 1
                if nums[i] > nums[i+1]:
                    return -1
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().minOperations([25, 7]))
    # -1
    print(Solution().minOperations([7, 7, 6]))
    # 0
    print(Solution().minOperations([1, 1, 1, 1]))
