"""
 * 你将会得到一份单词表 words，一个字母表 letters （可能会有重复字母），以及每个字母对应的得分情况表 score。
 * 请你帮忙计算玩家在单词拼写游戏中所能获得的「最高得分」：能够由 letters 里的字母拼写出的 任意 属于 words 单词子集中，分数最高的单词集合的得分。
 * 单词拼写游戏的规则概述如下：
 * 1、玩家需要用字母表 letters 里的字母来拼写单词表 words 中的单词。
 * 2、可以只使用字母表 letters 中的部分字母，但是每个字母最多被使用一次。
 * 3、单词表 words 中每个单词只能计分（使用）一次。
 * 4、根据字母得分情况表score，字母 'a', 'b', 'c', ... , 'z' 对应的得分分别为 score[0], score[1], ..., score[25]。
 * 5、本场游戏的「得分」是指：玩家所拼写出的单词集合里包含的所有字母的得分之和。
 * 提示：
 * 1、1 <= words.length <= 14
 * 2、1 <= words[i].length <= 15
 * 3、1 <= letters.length <= 100
 * 4、letters[i].length == 1
 * 5、score.length == 26
 * 6、0 <= score[i] <= 10
 * 7、words[i] 和 letters[i] 只包含小写的英文字母。
 * 链接：https://leetcode.cn/problems/maximum-score-words-formed-by-letters/
"""
from typing import List, Counter


class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        w_scores = [Counter(w) for w in words]
        c_letters = Counter(letters)
        n = len(words)
        ans = 0
        for i in range(1 << n):
            sc = Counter()
            for j in range(n):
                if (i >> j) & 1:
                    sc += w_scores[j]
            fit = True
            for k, v in sc.items():
                if c_letters[k] < v:
                    fit = False
                    break
            if fit and sc:
                sm = 0
                for k, v in sc.items():
                    sm += score[ord(k) - ord('a')] * v
                ans = max(ans, sm)
        return ans


if __name__ == '__main__':
    # 23
    print(Solution().maxScoreWords(["dog", "cat", "dad", "good"], ["a", "a", "c", "d", "d", "d", "g", "o", "o"], [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # 27
    print(Solution().maxScoreWords(["xxxz", "ax", "bx", "cx"], ["z", "a", "b", "c", "x", "x", "x"], [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]))
    # 0
    print(Solution().maxScoreWords(["leetcode"], ["l", "e", "t", "c", "o", "d"], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]))
