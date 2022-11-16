"""
 * 给定字符串 s 和字符串数组 words, 返回  words[i] 中是s的子序列的单词个数 。
 * 字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。
 * 例如， “ace” 是 “abcde” 的子序列。
 * 提示:
 * 1 <= s.length <= 5 * 10^4
 * 1 <= words.length <= 5000
 * 1 <= words[i].length <= 50
 * words[i]和 s 都只由小写字母组成。
 * 链接：https://leetcode.cn/problems/number-of-matching-subsequences/
"""
from bisect import bisect_right
from collections import defaultdict
from typing import List


class Solution:

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        ids = defaultdict(list)
        for i, c in enumerate(s):
            ids[c].append(i)
        for word in words:
            last = -1
            for c in word:
                idx = bisect_right(ids[c], last)
                if idx == len(ids[c]):
                    break
                last = ids[c][idx]
            else:
                ans += 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().numMatchingSubseq("abcde", words=["a", "bb", "acd", "ace"]))
    # 2
    print(Solution().numMatchingSubseq("dsahjpjauf", words=["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))
    #
    # print(Solution().numMatchingSubseq())