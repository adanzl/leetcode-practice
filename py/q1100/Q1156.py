"""
 * 如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。
 * 给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。
 * 提示：
 * 1、1 <= text.length <= 20000
 * 2、text 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/swap-for-longest-repeated-character-substring/
"""
from collections import Counter


class Solution:

    def maxRepOpt1(self, text: str) -> int:
        cnt = Counter()
        n = len(text)
        l = 0
        s = []
        for i in range(1, n):
            if text[i] != text[i - 1]:
                s.append([l, i - 1, text[i - 1]])
                cnt[text[i - 1]] += 1
                l = i
        s.append([l, n - 1, text[n - 1]])
        cnt[text[n - 1]] += 1
        ans = 0
        for i, (l, r, c) in enumerate(s):
            if r - l + 1 == 1 and i > 0 and i < len(s) - 1 and s[i - 1][2] == s[i + 1][2]:
                ans = max(ans, 1 + s[i - 1][1] - s[i - 1][0] + 1 + s[i + 1][1] - s[i + 1][0] + (1 if cnt[s[i - 1][2]] > 2 else 0))
            if cnt[c] > 1:
                ans = max(ans, r - l + 1 + 1)
            ans = max(ans, r - l + 1)
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().maxRepOpt1("ababa"))
    # 6
    print(Solution().maxRepOpt1("aaabaaa"))
    # 4
    print(Solution().maxRepOpt1("aaabbaaa"))
    # 5
    print(Solution().maxRepOpt1("aaaaa"))
    # 1
    print(Solution().maxRepOpt1("abcdef"))