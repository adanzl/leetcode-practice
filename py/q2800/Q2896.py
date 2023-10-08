"""
 * 给你两个下标从 0 开始的二进制字符串 s1 和 s2 ，两个字符串的长度都是 n ，再给你一个正整数 x 。
 * 你可以对字符串 s1 执行以下操作 任意次 ：
 * 1、选择两个下标 i 和 j ，将 s1[i] 和 s1[j] 都反转，操作的代价为 x 。
 * 2、选择满足 i < n - 1 的下标 i ，反转 s1[i] 和 s1[i + 1] ，操作的代价为 1 。
 * 请你返回使字符串 s1 和 s2 相等的 最小 操作代价之和，如果无法让二者相等，返回 -1 。
 * 注意 ，反转字符的意思是将 0 变成 1 ，或者 1 变成 0 。
 * 提示：
 * 1、n == s1.length == s2.length
 * 2、1 <= n, x <= 500
 * 3、s1 和 s2 只包含字符 '0' 和 '1' 。
 * 链接：https://leetcode.cn/problems/apply-operations-to-make-two-strings-equal/
"""

from functools import cache


class Solution:

    def minOperations(self, s1: str, s2: str, x: int) -> int:
        e = 0
        for c0, c1 in zip(s1, s2):
            if c0 != c1:
                e ^= 1
        if e == 1:
            return -1
        n = len(s1)
        ss = list(s1)

        @cache
        def dfs(idx, pairs):
            for i in range(idx, n - 1):
                if ss[i] == s2[i]:
                    continue
                if i < n - 1:
                    ss[i + 1] = str(int(s1[i + 1]) ^ 1)
                    v1 = dfs(i + 1, pairs) + 1
                    ss[i + 1] = s1[i + 1]
                    v2 = dfs(i + 1, pairs ^ 1) + (x if pairs == 0 else 0)
                    return min(v1, v2)
            return 0

        return dfs(0, 0)


if __name__ == '__main__':
    # 33
    print(Solution().minOperations("11111001100111101010101010100000010000000010110100111000001100101100000010000011100",
                                   "11101101001010101001000110010101011001100110011011001101100100101101100101100000010", 50))
    # 4
    print(Solution().minOperations("101101", "000000", 6))
    # 4
    print(Solution().minOperations('1100011000', '0101001010', 2))
    # -1
    print(Solution().minOperations('10110', '00011', 4))
