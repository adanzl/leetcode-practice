"""
 * 给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。
 * 请你返回让 s 成为回文串的 最少操作次数 。
 * 「回文串」是正读和反读都相同的字符串。
 * 提示：
 * 1、1 <= s.length <= 500
 * 2、s 中所有字符都是小写字母。
 * 链接：https://leetcode.cn/problems/minimum-insertion-steps-to-make-a-string-palindrome/
"""
from functools import cache


class Solution:

    def minInsertions(self, s: str) -> int:
        n = len(s)
        rs = s[::-1]

        @cache
        def f(i1, i2):
            if i1 == n: return n - i2
            if i2 == n: return n - i1
            if s[i1] == rs[i2]: return f(i1 + 1, i2 + 1)
            return min(f(i1 + 1, i2), f(i1, i2 + 1)) + 1

        return f(0, 0) // 2


if __name__ == '__main__':
    # 5
    print(Solution().minInsertions("zjveiiwvc"))
    # 0
    print(Solution().minInsertions("zzazz"))
    # 2
    print(Solution().minInsertions("mbadm"))
    # 5
    print(Solution().minInsertions("leetcode"))