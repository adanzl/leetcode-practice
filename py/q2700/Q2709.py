"""
 * 给你一个下标从 0 开始的整数数组 nums ，你可以在一些下标之间遍历。对于两个下标 i 和 j（i != j），
 * 当且仅当 gcd(nums[i], nums[j]) > 1 时，我们可以在两个下标之间通行，其中 gcd 是两个数的 最大公约数 。
 * 你需要判断 nums 数组中 任意 两个满足 i < j 的下标 i 和 j ，是否存在若干次通行可以从 i 遍历到 j 。
 * 如果任意满足条件的下标对都可以遍历，那么返回 true ，否则返回 false 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/greatest-common-divisor-traversal/
"""
from functools import cache
from typing import List


class Solution:

    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        @cache
        def prime_map(x):
            # 分解质因数
            p = 2
            num = x
            p_map = {}
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

        pa = {}

        def parent(x):
            if x in pa:
                return pa[x]
            pa[x] = x
            return x

        def find(x):
            if x != parent(x):
                pa[x] = find(pa[x])
            return pa[x]

        for _, v in enumerate(nums):
            if v == 1: return len(nums) == 1
            p = prime_map(v)
            r0 = find(list(p.keys())[0])
            for v in p.keys():
                r1 = find(v)
                if r0 != r1:
                    pa[r1] = r0
        for v in pa.keys():
            find(v)
        return len(set(pa.values())) == 1


if __name__ == '__main__':
    # False
    print(Solution().canTraverseAllPairs([42, 40, 45, 42, 50, 33, 30, 45, 33, 45, 30, 36, 44, 1, 21, 10, 40, 42, 42]))
    # True
    print(Solution().canTraverseAllPairs([2, 3, 6]))
    # False
    print(Solution().canTraverseAllPairs([3, 9, 5]))
    # True
    print(Solution().canTraverseAllPairs([4, 3, 12, 8]))
    # True
    print(Solution().canTraverseAllPairs([1]))
