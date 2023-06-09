"""
 * 定义一个函数 f(s)，统计 s  中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。
 * 例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。
 * 现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，需统计 words 中满足 f(queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。
 * 请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。
 * 提示：
 * 1、1 <= queries.length <= 2000
 * 2、1 <= words.length <= 2000
 * 3、1 <= queries[i].length, words[i].length <= 10
 * 4、queries[i][j]、words[i][j] 都由小写英文字母组成
 * 链接：https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/
"""
import bisect
from collections import Counter
from typing import List


class Solution:

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        def f(s):
            cnt = Counter(s)
            return cnt[sorted(cnt.keys())[0]]

        arr = sorted([f(w) for w in words])
        n = len(words)
        ans = []
        for q in queries:
            ans.append(n - bisect.bisect_right(arr, f(q)))
        return ans


if __name__ == '__main__':
    # [1]
    print(Solution().numSmallerByFrequency(["cbd"], words=["zaaaz"]))
    # [1, 2]
    print(Solution().numSmallerByFrequency(["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"]))
