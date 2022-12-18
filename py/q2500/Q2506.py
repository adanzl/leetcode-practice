"""
 * 给你一个下标从 0 开始的字符串数组 words 。
 * 如果两个字符串由相同的字符组成，则认为这两个字符串 相似 。
 * 1、例如，"abca" 和 "cba" 相似，因为它们都由字符 'a'、'b'、'c' 组成。
 * 2、然而，"abacba" 和 "bcfd" 不相似，因为它们不是相同字符组成的。
 * 请你找出满足字符串 words[i] 和 words[j] 相似的下标对 (i, j) ，并返回下标对的数目，其中 0 <= i < j <= word.length - 1 。
 * 提示：
 * 1、1 <= words.length <= 100
 * 2、1 <= words[i].length <= 100
 * 3、words[i] 仅由小写英文字母组成
 * 链接：https://leetcode.cn/problems/count-pairs-of-similar-strings/
"""
from collections import Counter
from typing import List


class Solution:

    def similarPairs(self, words: List[str]) -> int:
        wc = []
        ans = 0
        for w in words:
            c = Counter(w)
            for pc in wc:
                if pc == c.keys(): ans += 1
            wc.append(c.keys())
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]))
    # 3
    print(Solution().similarPairs(["aabb", "ab", "ba"]))
    # 0
    print(Solution().similarPairs(["nba", "cba", "dba"]))
