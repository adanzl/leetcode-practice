"""
 * 给你一个下标从 0 开始的字符串 s ，这个字符串只包含 0 到 9 的数字字符。
 * 如果一个字符串 t 中至多有一对相邻字符是相等的，那么称这个字符串 t 是 半重复的 。
 * 例如，0010 、002020 、0123 、2002 和 54944 是半重复字符串，而 00101022 和 1101234883 不是。
 * 请你返回 s 中最长 半重复 子字符串的长度。
 * 一个 子字符串 是一个字符串中一段连续 非空 的字符。
 * 提示：
 * 1、1 <= s.length <= 50
 * 2、'0' <= s[i] <= '9'
 * 链接：https://leetcode.cn/problems/find-the-longest-semi-repetitive-substring/
"""


class Solution:

    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans = 0
        arr = [0, 0]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                ans = max(ans, i - arr[-2] )
                arr.append(i)
        return max(ans, len(s) - arr[-2])


if __name__ == '__main__':
    # 4
    print(Solution().longestSemiRepetitiveSubstring("52233"))
    # 4
    print(Solution().longestSemiRepetitiveSubstring("5494"))
    # 2
    print(Solution().longestSemiRepetitiveSubstring("1111111"))