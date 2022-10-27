"""
 * 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
 * 注意：
 * 1、对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
 * 2、如果 s 中存在这样的子串，我们保证它是唯一的答案。
 * 提示：
 * 1、1 <= s.length, t.length <= 10^5
 * 2、s 和 t 由英文字母组成
 * 链接：https://leetcode.cn/problems/minimum-window-substring/
"""
from collections import Counter


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        ct, cs = Counter(t), Counter()
        r, l, cnt = 0, 0, 0
        ans = s
        while r < len(s):
            if s[r] in ct:
                cs[s[r]] += 1
                if cs[s[r]] == ct[s[r]]: cnt += 1
            while l < r:
                if s[l] in ct and cs[s[l]] <= ct[s[l]]: break
                cs[s[l]] -= 1
                l += 1
            if cnt == len(ct) and r - l + 1 < len(ans): ans = s[l:r + 1]
            r += 1
        return "" if cnt < len(ct) else ans


if __name__ == '__main__':
    # "BANC"
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
    # "a"
    print(Solution().minWindow("a", "a"))
    # ""
    print(Solution().minWindow("a", "aa"))
    # "a"
    print(Solution().minWindow("ab", "a"))