"""
 * 给你一个整数 n 和一个下标从 0 开始的字符串数组 words ，和一个下标从 0 开始的数组 groups ，两个数组长度都是 n 。
 * 两个长度相等字符串的 汉明距离 定义为对应位置字符 不同 的数目。
 * 你需要从下标 [0, 1, ..., n - 1] 中选出一个 最长子序列 ，将这个子序列记作长度为 k 的 [i0, i1, ..., ik - 1] ，它需要满足以下条件：
 * 1、相邻 下标对应的 groups 值 不同。即，对于所有满足 0 < j + 1 < k 的 j 都有 groups[ij] != groups[ij + 1] 。
 * 2、对于所有 0 < j + 1 < k 的下标 j ，都满足 words[ij] 和 words[ij + 1] 的长度 相等 ，且两个字符串之间的 汉明距离 为 1 。
 * 请你返回一个字符串数组，它是下标子序列 依次 对应 words 数组中的字符串连接形成的字符串数组。如果有多个答案，返回任意一个。
 * 子序列 指的是从原数组中删掉一些（也可能一个也不删掉）元素，剩余元素不改变相对位置得到的新的数组。
 * 注意：words 中的字符串长度可能 不相等 。
 * 提示：
 * 1、1 <= n == words.length == groups.length <= 1000
 * 2、1 <= words[i].length <= 10
 * 3、1 <= groups[i] <= n
 * 4、words 中的字符串 互不相同 。
 * 5、words[i] 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/longest-unequal-adjacent-groups-subsequence-ii/
"""
from typing import List


class Solution:

    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        ans = []

        def dis(s1, s2):
            ret = 0
            for c1, c2 in zip(s1, s2):
                ret += int(c1 != c2)
            return ret + abs(len(s1) - len(s2))

        for i, word in enumerate(words):
            dp[i] = [word]
            for j in range(i - 1, -1, -1):
                if len(word) == len(words[j]) and dis(word, words[j]) == 1 and groups[i] != groups[j]:
                    if len(dp[i]) < len(dp[j]) + 1:
                        dp[i] = dp[j] + [word]
            if len(dp[i]) > len(ans):
                ans = dp[i]
        return ans


if __name__ == '__main__':
    # ["aaa","ada"]
    print(Solution().getWordsInLongestSubsequence(3, ["bdb", "aaa", "ada"], [2, 1, 3]))
    # ["bab","cab"]
    print(Solution().getWordsInLongestSubsequence(3, words=["bab", "dab", "cab"], groups=[1, 2, 2]))
    # ["a","b","c","d"]
    print(Solution().getWordsInLongestSubsequence(4, words=["a", "b", "c", "d"], groups=[1, 2, 3, 4]))
