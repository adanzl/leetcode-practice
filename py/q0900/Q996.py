"""
 * 给定一个非负整数数组 A，如果该数组每对相邻元素之和是一个完全平方数，则称这一数组为正方形数组。
 * 返回 A 的正方形排列的数目。两个排列 A1 和 A2 不同的充要条件是存在某个索引 i，使得 A1[i] != A2[i]。
 * 提示：
 * 1、1 <= A.length <= 12
 * 2、0 <= A[i] <= 1e9
 * 链接：https://leetcode.cn/problems/number-of-squareful-arrays/
"""
from typing import List
import math


class Solution:

    def numSquarefulPerms1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = set([(x, ) for x in range(n)])

        def add(nv, ans, ndp):
            na = tuple(map(lambda x: nums[x], nv))
            if na not in ans:
                ans.add(na)
                ndp.add(nv)

        for _ in range(1, n):
            ndp, ans = set(), set()
            for v in dp:
                for i in range(n):
                    if i in v: continue
                    num = nums[i]
                    if math.sqrt(num + nums[v[0]]).is_integer():
                        add((i, ) + v, ans, ndp)
                    for j in range(1, len(v)):
                        if math.sqrt(num + nums[v[j - 1]]).is_integer() and math.sqrt(num + nums[v[j]]).is_integer():
                            add(v[:j] + (i, ) + v[j:], ans, ndp)
                    if math.sqrt(num + nums[v[-1]]).is_integer():
                        add(v + (i, ), ans, ndp)
            dp = ndp
        return len(dp)

    def numSquarefulPerms(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        for i in range(n):
            dp[(nums[i], )] = 1 << i  # ans-mask
        for _ in range(1, n):
            ndp = dict()
            for k, v in dp.items():
                for i in range(n):
                    if v & (1 << i) != 0: continue
                    num = nums[i]
                    if math.sqrt(num + k[0]).is_integer():
                        ndp[(num, ) + k] = v | (1 << i)
                    for j in range(1, len(k)):
                        if math.sqrt(num + k[j - 1]).is_integer() and math.sqrt(num + k[j]).is_integer():
                            ndp[k[:j] + (num, ) + k[j:]] = v | (1 << i)
                    if math.sqrt(num + k[-1]).is_integer():
                        ndp[k + (num, )] = v | (1 << i)
            dp = ndp
        return len(dp)


if __name__ == '__main__':
    # 1
    print(Solution().numSquarefulPerms([2, 2, 2, 2, 2, 2, 2, 2, 2]))
    # 1
    print(Solution().numSquarefulPerms([1, 1, 8, 1, 8]))
    # 0
    print(Solution().numSquarefulPerms([99, 62, 10, 47, 53, 9, 83, 33, 15, 24]))
    # 2
    print(Solution().numSquarefulPerms([1, 17, 8]))
    # 1
    print(Solution().numSquarefulPerms([2, 2, 2]))
