"""
 * 给你一个字符串 s 和一个整数 k 。
 * 定义函数 distance(s1, s2) ，用于衡量两个长度为 n 的字符串 s1 和 s2 之间的距离，即：
 * 字符 'a' 到 'z' 按 循环 顺序排列，对于区间 [0, n - 1] 中的 i ，计算所有「 s1[i] 和 s2[i] 之间 最小距离」的 和 。
 * 例如，distance("ab", "cd") == 4 ，且 distance("a", "z") == 1 。
 * 你可以对字符串 s 执行 任意次 操作。在每次操作中，可以将 s 中的一个字母 改变 为 任意 其他小写英文字母。
 * 返回一个字符串，表示在执行一些操作后你可以得到的 字典序最小 的字符串 t ，且满足 distance(s, t) <= k 。
 * 提示：
 * 1、1 <= s.length <= 100
 * 2、0 <= k <= 2000
 * 3、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/lexicographically-smallest-string-after-operations-with-constraint/
"""


class Solution:

    def getSmallestString(self, s: str, k: int) -> str:
        ss = list(s)
        idx = {}
        chs = 'abcdefghijklmnopqrstuvwxyz'
        for i, c in enumerate(chs):
            idx[c] = i
        for i in range(len(s)):
            if k == 0:
                break
            ii = idx[s[i]]
            # change to a
            d = min(ii, 26 - ii)
            if d <= k:
                ss[i] = 'a'
                k -= d
            else:
                ss[i] = chs[ii - k]
                break
        return ''.join(ss)


if __name__ == '__main__':
    # "aaaz"
    print(Solution().getSmallestString("zbbz", k=3))
    # "aawcd"
    print(Solution().getSmallestString("xaxcd", k=4))
    # "lol"
    print(Solution().getSmallestString("lol", k=0))
