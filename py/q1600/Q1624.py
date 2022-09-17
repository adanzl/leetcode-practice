"""
 * 给你一个字符串 s，请你返回 两个相同字符之间的最长子字符串的长度 ，计算长度时不含这两个字符。如果不存在这样的子字符串，返回 -1 。
 * 子字符串 是字符串中的一个连续字符序列。
 * 提示：
 * 1 <= s.length <= 300
 * s 只含小写英文字母
 * 链接：https://leetcode.cn/problems/largest-substring-between-two-equal-characters/
"""


class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        mark = [-1] * 256
        for i, c in enumerate(s):
            if mark[ord(c)] == -1:
                mark[ord(c)] = i
            else:
                ans = max(ans, i - mark[ord(c)] - 1)
        return ans


if __name__ == '__main__':
    # 0
    print(Solution().maxLengthBetweenEqualCharacters("aa"))
    # 2
    print(Solution().maxLengthBetweenEqualCharacters("abca"))
    # -1
    print(Solution().maxLengthBetweenEqualCharacters("cbzxy"))
    # 4
    print(Solution().maxLengthBetweenEqualCharacters("cabbac"))