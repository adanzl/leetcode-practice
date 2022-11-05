"""
 * 给你两个字符串数组 queries 和 dictionary 。数组中所有单词都只包含小写英文字母，且长度都相同。
 * 一次 编辑 中，你可以从 queries 中选择一个单词，将任意一个字母修改成任何其他字母。从 queries 中找到所有满足以下条件的字符串：不超过 两次编辑内，字符串与 dictionary 中某个字符串相同。
 * 请你返回 queries 中的单词列表，这些单词距离 dictionary 中的单词 编辑次数 不超过 两次 。单词返回的顺序需要与 queries 中原本顺序相同。
 * 提示：
 * 1、1 <= queries.length, dictionary.length <= 100
 * 2、n == queries[i].length == dictionary[j].length
 * 3、1 <= n <= 100
 * 4、所有 queries[i] 和 dictionary[j] 都只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/words-within-two-edits-of-dictionary/
"""
from typing import List


class Solution:

    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for query in queries:
            find = False
            for d in dictionary:
                cnt = 0
                for c1, c2 in zip(query, d):
                    if c1 != c2: cnt += 1
                    if cnt > 2: break
                if cnt <= 2:
                    find = True
                    break
            if find: ans.append(query)
        return ans


if __name__ == '__main__':
    # ["tsl","yyy","rbc","dda","qus","hyb","ilu"]
    print(Solution().twoEditWords(["tsl", "sri", "yyy", "rbc", "dda", "qus", "hyb", "ilu", "ahd"], ["uyj", "bug", "dba", "xbe", "blu", "wuo", "tsf", "tga"]))
