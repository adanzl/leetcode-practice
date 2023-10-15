"""
 * 给你一个整数 n 和一个下标从 0 开始的字符串数组 words ，和一个下标从 0 开始的 二进制 数组 groups ，两个数组长度都是 n 。
 * 你需要从下标 [0, 1, ..., n - 1] 中选出一个 最长子序列 ，将这个子序列记作长度为 k 的 [i0, i1, ..., ik - 1] ，
 * 对于所有满足 0 < j + 1 < k 的 j 都有 groups[ij] != groups[ij + 1] 。
 * 请你返回一个字符串数组，它是下标子序列 依次 对应 words 数组中的字符串连接形成的字符串数组。如果有多个答案，返回任意一个。
 * 子序列 指的是从原数组中删掉一些（也可能一个也不删掉）元素，剩余元素不改变相对位置得到的新的数组。
 * 注意：words 中的字符串长度可能 不相等 。
 * 提示：
 * 1、1 <= n == words.length == groups.length <= 100
 * 2、1 <= words[i].length <= 10
 * 3、0 <= groups[i] < 2
 * 4、words 中的字符串 互不相同 。
 * 5、words[i] 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/longest-unequal-adjacent-groups-subsequence-i/
"""
from typing import List


class Solution:

    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        c0, c1, f = 0, 0, -1
        ans = []
        for g, w in zip(groups, words):
            if f == -1:
                f = g
            if f == g and abs(c0 - c1) < 2:
                if g == 0:
                    c0 += 1
                if g == 1:
                    c1 += 1
                ans.append(w)
                f ^= 1
        return ans


if __name__ == '__main__':
    #
    print(Solution().getWordsInLongestSubsequence(3, ["o", "cfy", "en"], [1, 0, 0]))
    # ["d","g"]
    print(Solution().getWordsInLongestSubsequence(2, ["d", "g"], [0, 1]))
    # ["e","b"]
    print(Solution().getWordsInLongestSubsequence(3, words=["e", "a", "b"], groups=[0, 0, 1]))
    # ["a","b","c"]
    print(Solution().getWordsInLongestSubsequence(4, words=["a", "b", "c", "d"], groups=[1, 0, 1, 1]))