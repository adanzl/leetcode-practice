"""
 * 如果一个字符串满足以下条件，则称其为 美丽字符串 ：
 * 1、它由英语小写字母表的前 k 个字母组成。
 * 2、它不包含任何长度为 2 或更长的回文子字符串。
 * 给你一个长度为 n 的美丽字符串 s 和一个正整数 k 。
 * 请你找出并返回一个长度为 n 的美丽字符串，该字符串还满足：在字典序大于 s 的所有美丽字符串中字典序最小。如果不存在这样的字符串，则返回一个空字符串。
 * 对于长度相同的两个字符串 a 和 b ，如果字符串 a 在与字符串 b 不同的第一个位置上的字符字典序更大，则字符串 a 的字典序大于字符串 b 。
 * 例如，"abcd" 的字典序比 "abcc" 更大，因为在不同的第一个位置（第四个字符）上 d 的字典序大于 c 。
 * 提示：
 * 1、1 <= n == s.length <= 10^5
 * 2、4 <= k <= 26
 * 3、s 是一个美丽字符串
 * 链接：https://leetcode.cn/problems/lexicographically-smallest-beautiful-string/
"""


class Solution:

    def smallestBeautifulString(self, s: str, k: int) -> str:
        ss = list(s)
        n = len(s)
        a = "abcdefghijklmnopqrstuvwxyz"[:k]

        def func(ss, idx):
            i = idx + 1
            if i == n: return True
            c = ss[idx]
            for j in range(k):
                if i > 0 and a[j] == ss[i - 1]: continue
                if i > 1 and a[j] == ss[i - 2]: continue
                ss[i] = a[j]
                if func(ss, i): return True
                ss[i] = c
            return True

        for i in range(n - 1, -1, -1):
            idx = a.index(ss[i])
            if idx == k - 1: continue
            for j in range(idx + 1, k):
                if i > 0 and a[j] == ss[i - 1]: continue
                if i > 1 and a[j] == ss[i - 2]: continue
                ss[i] = a[j]
                if func(ss, i):
                    return "".join(ss)
                else:
                    ss[i] = a[idx]
        return ''


if __name__ == '__main__':
    # "abda"
    print(Solution().smallestBeautifulString("abcz", k=26))
    # ""
    print(Solution().smallestBeautifulString("dc", k=4))
    #
    # print(Solution().smallestBeautifulString())