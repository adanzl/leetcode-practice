"""
 * 给你一个长度为 n 的整数数组 nums ，这个数组中至多有 50 个不同的值。同时你有 m 个顾客的订单 quantity ，其中，整数 quantity[i] 是第 i 位顾客订单的数目。
 * 请你判断是否能将 nums 中的整数分配给这些顾客，且满足：
 * 1、第 i 位顾客 恰好 有 quantity[i] 个整数。
 * 2、第 i 位顾客拿到的整数都是 相同的 。
 * 3、每位顾客都满足上述两个要求。
 * 如果你可以分配 nums 中的整数满足上面的要求，那么请返回 true ，否则返回 false 。
 * 提示：
 * 1、n == nums.length
 * 2、1 <= n <= 10^5
 * 3、1 <= nums[i] <= 1000
 * 4、m == quantity.length
 * 5、1 <= m <= 10
 * 6、1 <= quantity[i] <= 10^5
 * 7、nums 中至多有 50 个不同的数字。
 * 链接：https://leetcode.cn/problems/distribute-repeating-integers/
"""
from collections import Counter
from functools import cache
from typing import List


class Solution:
    # can not greedy
    def canDistribute1(self, nums: List[int], quantity: List[int]) -> bool:
        lst = Counter(nums).values()
        n = len(quantity)
        quantity = sorted(quantity, reverse=True)

        @cache
        def dfs(lst, k):
            if k == n:
                return True
            lst = list(lst)
            for i in range(len(lst)):
                if lst[i] >= quantity[k]:
                    if dfs(tuple(lst[:i] + [lst[i] - quantity[k]] + lst[i + 1:]), k + 1):
                        return True
            return False

        return dfs(tuple(lst), 0)

    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        cnt = list(Counter(nums).values())
        n, m = len(cnt), len(quantity)
        # dp[i][j] 表示前 i 个数字中，是否能够组成状态 j
        # dp 的转移，假设存在 cnt[i] 满足 j 的一个子状态 s，同时 cnt[0..i-1] 满足 j 的剩余状态 j^s，则 dp[i][j] = True
        # if dp[i-1][j^s] and cnt[i] >= sm[s] then dp[i][j] = True
        dp = [[False] * (1 << m) for _ in range(n + 1)]
        dp[0][0] = True
        sm = [0] * (1 << m)  # 预处理子状态的和
        for i in range(1, 1 << m):  # 移除最右 1， low_bit
            sm[i] = sm[i & (i - 1)] + quantity[(i & -i).bit_length() - 1]

        for i in range(1, n + 1):
            for j in range(1 << m):
                if dp[i - 1][j]:
                    dp[i][j] = True
                    continue
                # 降序遍历非空子集 https://oi-wiki.org/math/binary-set/#%E5%AD%90%E9%9B%86%E9%81%8D%E5%8E%86
                s = j
                while s:
                    last = dp[i - 1][j ^ s]  # cnt[0..i-1] 能否满足子集 j^s
                    need = sm[s] <= cnt[i - 1]  # cnt[i] 能否满足子集 s
                    if last and need:
                        dp[i][j] = True
                        break
                    s = (s - 1) & j
        return dp[-1][-1]


if __name__ == '__main__':
    # True
    print(Solution().canDistribute([1, 1, 1, 1, 2, 2, 2], [3, 2, 2]))
    # False
    print(Solution().canDistribute([1, 2, 3, 4], [2]))
    # True
    print(Solution().canDistribute([1, 2, 3, 3], [2]))
    # True
    print(Solution().canDistribute([1, 1, 2, 2], [2, 2]))
