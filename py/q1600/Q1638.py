"""
 * 给你两个字符串 s 和 t ，请你找出 s 中的非空子串的数目，这些子串满足替换 一个不同字符 以后，是 t 串的子串。
 * 换言之，请你找到 s 和 t 串中 恰好 只有一个字符不同的子字符串对的数目。
 * 比方说， "computer" 和 "computation" 加粗部分只有一个字符不同： 'e'/'a' ，所以这一对子字符串会给答案加 1 。
 * 请你返回满足上述条件的不同子字符串对数目。
 * 一个 子字符串 是一个字符串中连续的字符。
 * 提示：
 * 1、1 <= s.length, t.length <= 100
 * 2、s 和 t 都只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/count-substrings-that-differ-by-one-character/
"""


class Solution:

    def countSubstrings(self, s: str, t: str) -> int:
        ns, nt = len(s), len(t)
        dp0 = [[0] * (ns + 1) for _ in range(nt + 1)]
        dp1 = [[0] * (ns + 1) for _ in range(nt + 1)]
        ans = 0
        for i in range(nt):
            for j in range(ns):
                if t[i] == s[j]:
                    dp0[i + 1][j + 1] = dp0[i][j] + 1
                    dp1[i + 1][j + 1] = dp1[i][j]
                else:
                    dp1[i + 1][j + 1] = dp0[i][j] + 1
                ans += dp1[i + 1][j + 1]
        return ans


if __name__ == '__main__':
    # 6
    print(Solution().countSubstrings("aba", "baba"))
    # 3
    print(Solution().countSubstrings("ab", "bb"))
    # 0
    print(Solution().countSubstrings("a", "a"))
    # 10
    print(Solution().countSubstrings("abe", "bbc"))
