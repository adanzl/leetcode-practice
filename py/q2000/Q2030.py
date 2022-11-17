"""
 * 给你一个字符串 s ，一个整数 k ，一个字母 letter 以及另一个整数 repetition 。
 * 返回 s 中长度为 k 且 字典序最小 的子序列，该子序列同时应满足字母 letter 出现 至少 repetition 次。生成的测试用例满足 letter 在 s 中出现 至少 repetition 次。
 * 子序列 是由原字符串删除一些（或不删除）字符且不改变剩余字符顺序得到的剩余字符串。
 * 字符串 a 字典序比字符串 b 小的定义为：在 a 和 b 出现不同字符的第一个位置上，字符串 a 的字符在字母表中的顺序早于字符串 b 的字符。
 * 提示：
 * 1、1 <= repetition <= k <= s.length <= 5 * 10^4
 * 2、s 由小写英文字母组成
 * 3、letter 是一个小写英文字母，在 s 中至少出现 repetition 次
 * 链接：https://leetcode.cn/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/
"""
from typing import Counter


class Solution:

    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        l_r = Counter(s)[letter] - repetition
        remain = len(s) - k
        other = k - repetition
        ss = []
        for ch in s:
            while ss and ss[-1] > ch and remain:
                if ss[-1] == letter:
                    if l_r:
                        ss.pop()
                        remain -= 1
                        l_r -= 1
                    else:
                        break
                else:
                    ss.pop()
                    remain -= 1
            ss.append(ch)
        if len(ss) > k:
            ans = []
            for ch in ss:
                if ch != letter:
                    if other:
                        ans.append(ch)
                        other -= 1
                else: ans.append(ch)
                if len(ans) == k: break
            ans.extend([letter] * (k - len(ans)))
            ss = ans
        return "".join(ss)


if __name__ == '__main__':
    # "fffffffff"
    print(Solution().smallestSubsequence("facfffkfnffoppfffzfz", 9, "f", 9))
    # "afffff"
    print(Solution().smallestSubsequence("adffhjfmmmmorsfff", 6, "f", 5))
    # "abb"
    print(Solution().smallestSubsequence("aaabbbcccddd", 3, "b", 2))
    # "ecde"
    print(Solution().smallestSubsequence("leetcode", 4, "e", 2))
    # "eet"
    print(Solution().smallestSubsequence("leet", 3, "e", 1))
    # "bb"
    print(Solution().smallestSubsequence("bb", 2, "b", 2))
