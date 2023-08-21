"""
 * 给你三个字符串 a ，b 和 c ， 你的任务是找到长度 最短 的字符串，且这三个字符串都是它的 子字符串 。
 * 如果有多个这样的字符串，请你返回 字典序最小 的一个。
 * 请你返回满足题目要求的字符串。
 * 注意：
 * 1、两个长度相同的字符串 a 和 b ，如果在第一个不相同的字符处，a 的字母在字母表中比 b 的字母 靠前 ，那么字符串 a 比字符串 b 字典序小 。
 * 2、子字符串 是一个字符串中一段连续的字符序列。
 * 提示：
 * 1、1 <= a.length, b.length, c.length <= 100
 * 2、a ，b ，c 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/shortest-string-that-contains-three-strings/
"""

from itertools import permutations


class Solution:

    def minimumString(self, a: str, b: str, c: str) -> str:

        def merge_str(s0, s1):  # kmp 优化
            if s0 in s1: return s1  # 这个地方就没kmp 然后就很慢
            if s1 in s0: return s0
            s = s1 + s0
            n = len(s)
            next_arr = [-1] * (n + 1)
            i, j = 0, -1
            limit = min(len(s0), len(s1))
            while i < n:
                if j == -1 or (s[i] == s[j] and j < limit):
                    i += 1
                    j += 1
                    next_arr[i] = j
                else:
                    j = next_arr[j]
            l = min(len(s0), len(s1), next_arr[-1])
            return s0 + s1[l:]

        # 妖孽代码
        return min((merge_str(merge_str(s0, s1), s2) for s0, s1, s2 in permutations([a, b, c])), key=lambda x: (len(x), x))

    # 普通选手的解法
    def minimumString1(self, a: str, b: str, c: str) -> str:
        ans = ""

        def combine_str(s0, s1):
            if s0 in s1: return s1
            if s1 in s0: return s0
            for i in range(min(len(s0), len(s1)), 0, -1):
                if s0[-i:] == s1[:i]:
                    return s0 + s1[i:]
            return s0 + s1

        for a, b, c in permutations([a, b, c]):
            s = combine_str(combine_str(a, b), c)
            if not ans or len(s) < len(ans) or len(s) == len(ans) and s < ans:
                ans = s
        return ans


if __name__ == '__main__':
    # "cab"
    print(Solution().minimumString("cab", b="a", c="b"))
    # "bab"
    print(Solution().minimumString("bab", b="a", c="b"))
    # "baaa"
    print(Solution().minimumString("a", b="baa", c="aaa"))
    # "aaabca"
    print(Solution().minimumString("abc", b="bca", c="aaa"))
    # "aba"
    print(Solution().minimumString("ab", b="ba", c="aba"))
    # "ac"
    print(Solution().minimumString("ac", "a", "a"))
    # "aek"
    print(Solution().minimumString("k", "e", "a"))
    # "ab"
    print(Solution().minimumString('a', 'a', 'b'))