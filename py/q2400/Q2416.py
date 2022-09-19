"""
 * 给你一个长度为 n 的数组 words ，该数组由 非空 字符串组成。
 * 定义字符串 word 的 分数 等于以 word 作为 前缀 的 words[i] 的数目。
 * 例如，如果 words = ["a", "ab", "abc", "cab"] ，那么 "ab" 的分数是 2 ，因为 "ab" 是 "ab" 和 "abc" 的一个前缀。
 * 返回一个长度为 n 的数组 answer ，其中 answer[i] 是 words[i] 的每个非空前缀的分数 总和 。
 * 注意：字符串视作它自身的一个前缀。
 * 提示：
 * 1、1 <= words.length <= 1000
 * 2、1 <= words[i].length <= 1000
 * words[i] 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/sum-of-prefix-scores-of-strings/
"""

from collections import defaultdict
from typing import *


class Node:
    __slots__ = ('children', 'score')

    def __init__(self):
        self.children = defaultdict(Node)
        self.score = 0


class Solution:
    # trie tree
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        root = Node()
        for word in words:
            p = root
            for c in word:
                p = p.children[c]
                p.score += 1

        def dfs(root, word):
            ret, p = 0, root
            for c in word:
                p = p.children[c]
                ret += p.score
                pass
            return ret

        ans = []
        for word in words:
            ans.append(dfs(root, word))
        return ans      


if __name__ == '__main__':
    # [5,4,3,2]
    print(Solution().sumPrefixScores(["abc", "ab", "bc", "b"]))
    # [4]
    print(Solution().sumPrefixScores(["abcd"]))
