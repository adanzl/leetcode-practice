"""
 * 给出一个单词数组 words ，其中每个单词都由小写英文字母组成。
 * 如果我们可以 不改变其他字符的顺序 ，在 wordA 的任何地方添加 恰好一个 字母使其变成 wordB ，那么我们认为 wordA 是 wordB 的 前身 。
 * 例如，"abc" 是 "abac" 的 前身 ，而 "cba" 不是 "bcad" 的 前身
 * 词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word1 是 word2 的前身，word2 是 word3 的前身，依此类推。一个单词通常是 k == 1 的 单词链 。
 * 从给定单词列表 words 中选择单词组成词链，返回 词链的 最长可能长度 。
 * 提示：
 * 1、1 <= words.length <= 1000
 * 2、1 <= words[i].length <= 16
 * 3、words[i] 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/longest-string-chain/
"""
from typing import List


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        ans = 1
        n = len(words)
        dp = [1] * n

        def edit_1(s1, s2):
            if len(s2) - len(s1) != 1: return False
            n = len(s2)
            for i in range(n):
                if s1 == s2[0:i] + s2[i + 1:n]: return True
            return False

        for i in range(n):
            for j in range(i - 1, -1, -1):
                if len(words[i]) - len(words[j]) > 1: break
                if edit_1(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
    # 5
    print(Solution().longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
    # 1
    print(Solution().longestStrChain(["abcd", "dbqca"]))
