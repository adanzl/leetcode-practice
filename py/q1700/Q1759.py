"""
 * 给你一个字符串 s ，返回 s 中 同构子字符串 的数目。由于答案可能很大，只需返回对 10^9 + 7 取余 后的结果。
 * 同构字符串 的定义为：如果一个字符串中的所有字符都相同，那么该字符串就是同构字符串。
 * 子字符串 是字符串中的一个连续字符序列。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 由小写字符串组成
 * 链接：https://leetcode.cn/problems/count-number-of-homogenous-substrings/
"""

from itertools import groupby


class Solution:

    def countHomogenous1(self, s: str) -> int:
        res = 0
        for k, g in groupby(s):
            n = len(list(g))
            res += (n + 1) * n // 2
        return res % (10**9 + 7)

    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        pre = s[0]
        n, cnt, ans = len(s), 1, 0
        for i in range(1, n):
            if s[i] == pre:
                cnt += 1
            else:
                ans += (cnt + 1) * cnt // 2
                pre = s[i]
                cnt = 1
        ans += (cnt + 1) * cnt // 2
        return ans % MOD


if __name__ == '__main__':
    # 13
    print(Solution().countHomogenous("abbcccaa"))
    # 2
    print(Solution().countHomogenous("xy"))
    # 15
    print(Solution().countHomogenous("zzzzz"))