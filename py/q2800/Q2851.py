"""
 * 给你两个长度都为 n 的字符串 s 和 t 。你可以对字符串 s 执行以下操作：
 * 将 s 长度为 l （0 < l < n）的 后缀字符串 删除，并将它添加在 s 的开头。
 * 比方说，s = 'abcd' ，那么一次操作中，你可以删除后缀 'cd' ，并将它添加到 s 的开头，得到 s = 'cdab' 。
 * 给你一个整数 k ，请你返回 恰好 k 次操作将 s 变为 t 的方案数。
 * 由于答案可能很大，返回答案对 10^9 + 7 取余 后的结果。
 * 提示：
 * 1、2 <= s.length <= 5 * 10^5
 * 2、1 <= k <= 10^15
 * 3、s.length == t.length
 * 4、s 和 t 都只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/string-transformation/
"""

from typing import List

#
# @lc app=leetcode.cn id=2851 lang=python3
#

# @lc code=start

MOD = 10**9 + 7


class Solution:
    # kmp 构建next数组
    def build_next(self, ss):
        next_arr = [0] * len(ss)
        c = 0
        for i in range(1, len(ss)):
            v = ss[i]
            while c and ss[c] != v:
                c = next_arr[c - 1]
            if ss[c] == v:
                c += 1
            next_arr[i] = c
        return next_arr

    def kmp_search(self, s: str, pattern: str) -> int:
        next_arr = self.build_next(pattern)
        c, ans = 0, 0
        for v in s:
            while c and pattern[c] != v:
                c = next_arr[c - 1]
            if pattern[c] == v:
                c += 1
            if c == len(pattern):
                ans += 1
                c = next_arr[c - 1]
        return ans

    def matrix_mul(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # 矩阵乘法
        r1, c1, _, c2 = len(mat1), len(mat1[0]), len(mat2), len(mat2[0])
        ans = [[0] * c2 for _ in range(r1)]
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    ans[i][j] += mat1[i][k] * mat2[k][j]
                    ans[i][j] %= MOD
        return ans

    def matrix_pow(self, mat: List[List[int]], n: int) -> List[List[int]]:
        # 矩阵快速幂
        r, c = len(mat), len(mat[0])
        ans = [[1 if i == j else 0 for i in range(c)] for j in range(r)]
        while n:
            if n & 1:
                ans = self.matrix_mul(ans, mat)
            mat = self.matrix_mul(mat, mat)
            n >>= 1
        return ans

    def numberOfWays(self, s: str, t: str, k: int) -> int:

        n = len(s)
        cnt = self.kmp_search(s + s[:-1], t)  # cnt 表示 s 作为循环字符串时，包含 t 的个数
        if cnt == 0: return 0
        # f[i][0] 表示 s 经过 i 次变换 成为 t，f[i + 1][0] = f[i][0] * (cnt - 1) + f[i][1] * (cnt)
        # f[i][1] 表示 s 经过 i 次变换 不是 t，f[i + 1][1] = f[i][0] * (n - cnt) + f[i][1] * (n - cnt - 1)
        # f[i+1] = m * f[i]
        # 初值 f[0] = [1, 0] ,如果 s == t ，否则 f[0] = [0, 1]，f[k] = m^k * f[0]
        f = [[1], [0]] if s == t else [[0], [1]]
        m = [
            [cnt - 1, cnt],
            [n - cnt, n - cnt - 1],
        ]
        ans = self.matrix_mul(self.matrix_pow(m, k), f)
        return ans[0][0]


# @lc code=end

if __name__ == '__main__':
    # 322134019
    print(Solution().numberOfWays("wkldv", "ldvwk", 854972569843185))
    # 2
    print(Solution().numberOfWays("abcd", t="cdab", k=2))
    # 2
    print(Solution().numberOfWays("ababab", t="ababab", k=1))
    # 478297
    print(Solution().numberOfWays("otwqxmpktt", "totwqxmpkt", 7))
    # 8
    print(Solution().numberOfWays("ceoceo", "eoceoc", 2))
    # 0
    print(Solution().numberOfWays("ab", "bb", 0))