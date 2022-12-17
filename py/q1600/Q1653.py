"""
 * 给你一个字符串 s ，它仅包含字符 'a' 和 'b' 。
 * 你可以删除 s 中任意数目的字符，使得 s 平衡 。
 * 我们称 s 平衡的 当不存在下标对 (i,j) 满足 i < j 且 s[i] = 'b' 同时 s[j]= 'a' 。
 * 请你返回使 s 平衡 的 最少 删除次数。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s[i] 要么是 'a' 要么是 'b'​。
 * 链接：https://leetcode.cn/problems/minimum-deletions-to-make-string-balanced/
"""


class Solution:

    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        an, bn = [0] * n, [0] * n
        if s[-1] == 'a': an[-1] = 1
        if s[0] == 'b': bn[0] = 1
        for i in range(n - 2, -1, -1):  # a
            an[i] = an[i + 1] + (1 if s[i] == 'a' else 0)
        ans = an[0]
        for i in range(1, n):  # b
            bn[i] = bn[i - 1] + (1 if s[i] == 'b' else 0)
            if i < n - 1: ans = min(ans, bn[i - 1] + an[i + 1])
        ans = min(ans, bn[n - 1])

        return ans


if __name__ == '__main__':
    # 60
    print(Solution().minimumDeletions("bbbbbbbaabbbbbaaabbbabbbbaabbbbbbaabbaaabaabbbaaaabaaababbbabbabbaaaabbbabbbbbaabbababbbaaaaaababaaababaabbabbbaaaabbbbbabbabaaaabbbaba"))
    # 2
    print(Solution().minimumDeletions("aababbab"))
    # 2
    print(Solution().minimumDeletions("bbaaaaabb"))
    # 0
    print(Solution().minimumDeletions("b"))
    # 0
    print(Solution().minimumDeletions("bbbbbbbbbbbbbb"))