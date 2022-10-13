"""
 * 给定一个字符串 s，计算 s 的 不同非空子序列 的个数。因为结果可能很大，所以返回答案需要对 10^9 + 7 取余 。
 * 字符串的 子序列 是经由原字符串删除一些（也可能不删除）字符但不改变剩余字符相对位置的一个新字符串。
 * 例如，"ace" 是 "abcde" 的一个子序列，但 "aec" 不是。
 * 提示：
 * 1、1 <= s.length <= 2000
 * 2、s 仅由小写英文字母组成
 * 链接：https://leetcode.cn/problems/distinct-subsequences-ii/
"""


class Solution:

    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26
        sm = 0
        for c in s:
            i = ord(c) - ord('a')
            pre = dp[i]
            dp[i] = sm + 1
            sm = sm - pre + dp[i]
        return sm % MOD


if __name__ == '__main__':
    # 7
    print(Solution().distinctSubseqII("abc"))
    # 6
    print(Solution().distinctSubseqII("aba"))
    # 3
    print(Solution().distinctSubseqII("aaa"))