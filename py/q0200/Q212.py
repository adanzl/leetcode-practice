"""
 * 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。
 * 单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
 * 提示：
 * 1、m == board.length
 * 2、n == board[i].length
 * 3、1 <= m, n <= 12
 * 4、board[i][j] 是一个小写英文字母
 * 5、1 <= words.length <= 3 * 10^4
 * 6、1 <= words[i].length <= 10
 * 7、words[i] 由小写英文字母组成
 * 8、words 中的所有字符串互不相同
 * 链接：https://leetcode.cn/problems/word-search-ii/
"""
from typing import DefaultDict, List


class TNode:

    def __init__(self):
        self.children = DefaultDict(TNode)
        self.string = None


class Solution:

    # 前缀树 Tire Tree
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        m, n = len(board), len(board[0])

        tireTree = TNode()

        def buildTree(word, idx, tree):
            if idx == len(word):
                tree.string = word
                return
            buildTree(word, idx + 1, tree.children[word[idx]])

        def dfs(x, y, tree):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1: return
            c = board[x][y]
            if c not in tree.children: return
            subTree = tree.children[c]
            if subTree.string:
                ans.append(subTree.string)
                subTree.string = None
            board[x][y] = ' '
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                dfs(x + dx, y + dy, subTree)
            board[x][y] = c
            # 已经被处理过的tree就不需要了，防止重复处理
            if not subTree.children: tree.children.pop(c)

        for word in words:
            buildTree(word, 0, tireTree)
        for i in range(m):
            for j in range(n):
                dfs(i, j, tireTree)
                if len(ans) == len(words): return ans
        return ans


if __name__ == '__main__':
    # []
    print(Solution().findWords([["a", "a"]], ["aaa"]))
    # ["a"]
    print(Solution().findWords([["a"]], ["a"]))
    # ["abcdefg","befa","eaabcdgfa","gfedcbaaa"]
    print(Solution().findWords([["a", "b", "c"], ["a", "e", "d"], ["a", "f", "g"]], ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"]))
    # ["eat","oath"]
    print(Solution().findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], words=["oath", "pea", "eat", "rain"]))
    # []
    print(Solution().findWords([["a", "b"], ["c", "d"]], words=["abcb"]))
