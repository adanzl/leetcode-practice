"""
 * 总共有 n 个人和 40 种不同的帽子，帽子编号从 1 到 40 。
 * 给你一个整数列表的列表 hats ，其中 hats[i] 是第 i 个人所有喜欢帽子的列表。
 * 请你给每个人安排一顶他喜欢的帽子，确保每个人戴的帽子跟别人都不一样，并返回方案数。
 * 由于答案可能很大，请返回它对 10^9 + 7 取余后的结果。
 * 提示：
 * 1、n == hats.length
 * 2、1 <= n <= 10
 * 3、1 <= hats[i].length <= 40
 * 4、1 <= hats[i][j] <= 40
 * 5、hats[i] 包含一个数字互不相同的整数列表。
 * 链接：https://leetcode.cn/problems/number-of-ways-to-wear-different-hats-to-each-other/
"""
from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    # low_bit = m & (-m)
    def numberWays(self, hats: List[List[int]]) -> int:
        # 需要转换为帽子找人
        MOD = 10**9 + 7
        n = len(hats)
        p = defaultdict(list)
        for i, hat in enumerate(hats):
            for h in hat:
                p[h].append(i)
        hs = list(p.keys())

        @cache
        def dfs(idx, mark):  # hat_idx, n_hat
            if mark.bit_count() == n: return 1
            if idx == len(hs): return 0
            ret = dfs(idx + 1, mark)
            for h in p[hs[idx]]:
                if mark & 1 << h: continue
                ret += dfs(idx + 1, mark | 1 << h)
            return ret % MOD

        return dfs(0, 0)


if __name__ == '__main__':
    # 4
    print(Solution().numberWays([[3, 5, 1], [3, 5]]))
    # 1
    print(Solution().numberWays([[3, 4], [4, 5], [5]]))
    # 24
    print(Solution().numberWays([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]))
    # 111
    print(Solution().numberWays([[1, 2, 3], [2, 3, 5, 6], [1, 3, 7, 9], [1, 8, 9], [2, 5, 7]]))
