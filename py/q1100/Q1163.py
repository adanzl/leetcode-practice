"""
 * 给你一个字符串 s ，找出它的所有子串并按字典序排列，返回排在最后的那个子串。
 * 提示：
 * 1、1 <= s.length <= 4 * 10^5
 * 2、s 仅含有小写英文字符。
 * 链接：https://leetcode.cn/problems/last-substring-in-lexicographical-order/
"""


class Solution:

    def lastSubstring(self, s: str) -> str:
        q = []  # star-end
        for i, c in enumerate(s):
            if not q or s[q[-1][0]] == c:
                q.append([i, i])
            elif s[q[-1][0]] < c:
                q.clear()
                q.append([i, i])

        while len(q) > 1:
            r = -1
            t = []
            mx = ""
            for p0, p1 in q:
                if p1 + 1 == len(s):
                    if p0 > r:
                        t.append([p0, p1])
                    continue
                if p0 > r:
                    if s[p1 + 1] > mx:
                        t.clear()
                        t.append([p0, p1 + 1])
                    elif s[p1 + 1] == mx:
                        t.append([p0, p1 + 1])

                    mx = max(mx, s[p1 + 1])
                r = p1 + 1
            q = t
        return s[q[0][0]:]


if __name__ == '__main__':
    # "zrziy"
    print(Solution().lastSubstring("zrziy"))
    # "bab"
    print(Solution().lastSubstring("abab"))
    # "tcode"
    print(Solution().lastSubstring("leetcode"))