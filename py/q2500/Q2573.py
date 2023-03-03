"""
 * 对任一由 n 个小写英文字母组成的字符串 word ，我们可以定义一个 n x n 的矩阵，并满足：
 * lcp[i][j] 等于子字符串 word[i,...,n-1] 和 word[j,...,n-1] 之间的最长公共前缀的长度。
 * 给你一个 n x n 的矩阵 lcp 。返回与 lcp 对应的、按字典序最小的字符串 word 。如果不存在这样的字符串，则返回空字符串。
 * 对于长度相同的两个字符串 a 和 b ，如果在 a 和 b 不同的第一个位置，字符串 a 的字母在字母表中出现的顺序先于 b 中的对应字母，则认为字符串 a 按字典序比字符串 b 小。
 * 例如，"aabd" 在字典上小于 "aaca" ，因为二者不同的第一位置是第三个字母，而 'b' 先于 'c' 出现。
 * 提示：
 * 1、1 <= n == lcp.length == lcp[i].length <= 1000
 * 2、0 <= lcp[i][j] <= n
 * 链接：https://leetcode.cn/problems/find-the-string-with-lcp/
"""
from string import ascii_lowercase
from typing import List


class Solution:

    def findTheString(self, lcp: List[List[int]]) -> str:
        i, n = 0, len(lcp)
        s = [''] * n
        for c in ascii_lowercase:
            while i < n and s[i]:
                i += 1
            if i == n: break  # 构造完毕
            for j in range(i, n):
                if lcp[i][j]:
                    s[j] = c
        if '' in s: return ""  # 没有构造完

        # 直接在原数组上验证
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                actual_lcp = 0 if s[i] != s[j] else 1 if i == n - 1 or j == n - 1 else lcp[i + 1][j + 1] + 1
                if lcp[i][j] != actual_lcp: return ""
        return "".join(s)

    def findTheString1(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        parent = [i for i in range(n)]
        denny = [set() for _ in range(n)]
        cnt = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for i in range(n):
            if lcp[i][i] != n - i: return ""
            for j in range(i, n):
                if lcp[i][j] != lcp[j][i] or lcp[i][j] > min(n - i, n - j):
                    return ""
                v = lcp[i][j]
                for k in range(v):
                    r1, r2 = find(i + k), find(j + k)
                    if r1 == r2: continue
                    parent[r2] = r1
                    cnt -= 1
                if v + max(i, j) < n:
                    denny[i + v].add(j + v)
                    denny[j + v].add(i + v)
        if cnt > 26: return ""
        for i in range(n):
            r = find(i)
            for d in denny[i]:
                if find(d) == r:
                    return ""
        ans = ""
        idx = 0
        mp = {}
        for i in parent:
            if i not in mp:
                mp[i] = idx
                idx += 1
            ans += chr(ord("a") + mp[i])
        return ans


if __name__ == '__main__':
    # "ababaabaaccaa"
    print(Solution().findTheString([[13, 0, 3, 0, 1, 3, 0, 1, 1, 0, 0, 1, 1], [0, 12, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0], [3, 0, 11, 0, 1, 4, 0, 1, 1, 0, 0, 1, 1],
                                    [0, 2, 0, 10, 0, 0, 3, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 9, 1, 0, 2, 1, 0, 0, 2, 1], [3, 0, 4, 0, 1, 8, 0, 1, 1, 0, 0, 1, 1], [0, 2, 0, 3, 0, 0, 7, 0, 0, 0, 0, 0, 0],
                                    [1, 0, 1, 0, 2, 1, 0, 6, 1, 0, 0, 2, 1], [1, 0, 1, 0, 1, 1, 0, 1, 5, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0],
                                    [1, 0, 1, 0, 2, 1, 0, 2, 1, 0, 0, 2, 1], [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]]))
    # ""
    print(Solution().findTheString([[4, 1, 1, 1], [1, 3, 1, 1], [1, 1, 2, 1], [1, 1, 1, 1]]))
    # "abcbbaab"
    print(Solution().findTheString([[8, 0, 0, 0, 0, 1, 2, 0], [0, 7, 0, 1, 1, 0, 0, 1], [0, 0, 6, 0, 0, 0, 0, 0], [0, 1, 0, 5, 1, 0, 0, 1], [0, 1, 0, 1, 4, 0, 0, 1], [1, 0, 0, 0, 0, 3, 1, 0],
                                    [2, 0, 0, 0, 0, 1, 2, 0], [0, 1, 0, 1, 1, 0, 0, 1]]))
    # "abab"
    print(Solution().findTheString([[4, 0, 2, 0], [0, 3, 0, 1], [2, 0, 2, 0], [0, 1, 0, 1]]))
    # "aabababba"
    print(Solution().findTheString([[9, 1, 0, 1, 0, 1, 0, 0, 1], [1, 8, 0, 4, 0, 2, 0, 0, 1], [0, 0, 7, 0, 3, 0, 1, 2, 0], [1, 4, 0, 6, 0, 2, 0, 0, 1], [0, 0, 3, 0, 5, 0, 1, 2, 0],
                                    [1, 2, 0, 2, 0, 4, 0, 0, 1], [0, 0, 1, 0, 1, 0, 3, 1, 0], [0, 0, 2, 0, 2, 0, 1, 2, 0], [1, 1, 0, 1, 0, 1, 0, 0, 1]]))
    # ""
    print(Solution().findTheString([[4, 3, 2, 1], [3, 3, 2, 1], [2, 2, 2, 1], [1, 1, 1, 3]]))
    # "aaaa"
    print(Solution().findTheString([[4, 3, 2, 1], [3, 3, 2, 1], [2, 2, 2, 1], [1, 1, 1, 1]]))
