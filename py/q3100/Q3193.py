"""
 * 给你一个整数 n 和一个二维数组 requirements ，其中 requirements[i] = [end_i, cnt_i] 表示这个要求中的末尾下标和 逆序对 的数目。
 * 整数数组 nums 中一个下标对 (i, j) 如果满足以下条件，那么它们被称为一个 逆序对 ：
 * 1、i < j 且 nums[i] > nums[j]
 * 2、请你返回 [0, 1, 2, ..., n - 1] 的 排列 perm 的数目，满足对 所有 的 requirements[i] 都有 perm[0..end_i] 恰好有 cnt_i 个逆序对。
 * 由于答案可能会很大，将它对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、2 <= n <= 300
 * 2、1 <= requirements.length <= n
 * 3、requirements[i] = [end_i, cnt_i]
 * 4、0 <= end_i <= n - 1
 * 5、0 <= cnt_i <= 400
 * 6、输入保证至少有一个 i 满足 end_i == n - 1 。
 * 7、输入保证所有的 end_i 互不相同。
 * 链接：https://leetcode.cn/problems/count-the-number-of-inversions/
"""

from functools import cache
from typing import List

#
# @lc app=leetcode.cn id=3193 lang=python3
#
# [3193] 统计逆序对的数目
#


# @lc code=start
class Solution:

    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10**9 + 7
        r_map = {}
        for e, c in requirements:
            r_map[e] = c

        @cache
        def dfs(idx, mx):
            if idx in r_map and mx != r_map[idx]:
                return 0
            if mx > (idx + 1) * idx // 2:
                return 0
            if idx == 0: return 1
            ret = 0
            for tail in range(min(mx, idx) + 1):
                ret += dfs(idx - 1, mx - tail)
            return ret % MOD

        return dfs(n - 1, r_map[n - 1])


# @lc code=end

if __name__ == '__main__':
    # 0
    print(Solution().numberOfPermutations(3, [[2, 2], [0, 1]]))
    # 1
    print(Solution().numberOfPermutations(2, requirements=[[1, 0]]))
    # 2
    print(Solution().numberOfPermutations(3, requirements=[[2, 2], [0, 0]]))
    # 1
    print(Solution().numberOfPermutations(3, requirements=[[2, 2], [1, 1], [0, 0]]))
    # 1
    print(Solution().numberOfPermutations(2, requirements=[[0, 0], [1, 0]]))
