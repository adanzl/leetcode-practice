"""
 * 字母序连续字符串 是由字母表中连续字母组成的字符串。换句话说，字符串 "abcdefghijklmnopqrstuvwxyz" 的任意子字符串都是 字母序连续字符串 。
 * 例如，"abc" 是一个字母序连续字符串，而 "acb" 和 "za" 不是。
 * 给你一个仅由小写英文字母组成的字符串 s ，返回其 最长 的 字母序连续子字符串 的长度。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/
"""


class Solution:

    def longestContinuousSubstring(self, s: str) -> int:
        ans, pre, l = 1, 0, 0
        for c in s:
            if ord(c) == pre + 1:
                l += 1
                ans = max(ans, l)
            else:
                l = 1
            pre = ord(c)
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().longestContinuousSubstring("abacaba"))
    # 5
    print(Solution().longestContinuousSubstring("abcde"))