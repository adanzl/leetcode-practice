"""
 * 给定两个字符串s1 和 s2，返回 使两个字符串相等所需删除字符的 ASCII 值的最小和 。
 * 提示:
 * 1、0 <= s1.length, s2.length <= 1000
 * 2、s1 和 s2 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/description/
"""

from functools import cache


class Solution:

    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        @cache
        def f(i1, i2) -> int:
            n1, n2 = len(s1), len(s2)
            ans = 0
            if i1 == n1:
                for i in range(i2, n2):
                    ans += ord(s2[i])
                return ans
            if i2 == n2:
                for i in range(i1, n1):
                    ans += ord(s1[i])
                return ans
            if s1[i1] == s2[i2]:
                return f(i1 + 1, i2 + 1)
            return min(f(i1 + 1, i2) + ord(s1[i1]), f(i1, i2 + 1) + ord(s2[i2]))

        return f(0, 0)


if __name__ == '__main__':
    # 231
    print(Solution().minimumDeleteSum("sea", s2="eat"))
    # 403
    print(Solution().minimumDeleteSum("delete", s2="leet"))
    # 0
    print(Solution().minimumDeleteSum("", s2=""))