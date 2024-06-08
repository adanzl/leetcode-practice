"""
 * 给你两个字符串数组 wordsContainer 和 wordsQuery 。
 * 对于每个 wordsQuery[i] ，你需要从 wordsContainer 中找到一个与 wordsQuery[i] 有 最长公共后缀 的字符串。
 * 如果 wordsContainer 中有两个或者更多字符串有最长公共后缀，那么答案为长度 最短 的。
 * 如果有超过两个字符串有 相同 最短长度，那么答案为它们在 wordsContainer 中出现 更早 的一个。
 * 请你返回一个整数数组 ans ，其中 ans[i]是 wordsContainer中与 wordsQuery[i] 有 最长公共后缀 字符串的下标。
 * 提示：
 * 1、1 <= wordsContainer.length, wordsQuery.length <= 10^4
 * 2、1 <= wordsContainer[i].length <= 5 * 10^3
 * 3、1 <= wordsQuery[i].length <= 5 * 10^3
 * 4、wordsContainer[i] 只包含小写英文字母。
 * 5、wordsQuery[i] 只包含小写英文字母。
 * 6、wordsContainer[i].length 的和至多为 5 * 10^5 。
 * 7、wordsQuery[i].length 的和至多为 5 * 10^5 。
 * 链接：https://leetcode.cn/problems/longest-common-suffix-queries/
"""
from collections import defaultdict
from typing import List


class Solution:

    class TREE:
        def __init__(self):
            self.end = False
            self.sub = defaultdict(Solution.TREE)
            self.content = -1
            
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        suf_tree = Solution.TREE()
        mn_len_idx = 0
        for i, w in enumerate(wordsContainer):
            t = suf_tree
            if len(w) < len(wordsContainer[mn_len_idx]):
                mn_len_idx = i
            for j in range(len(w)-1, -1, -1):
                t = t.sub[w[j]]
                if t.content == -1 or len(w) < len(wordsContainer[t.content]):
                    t.content = i
        ans = []
        for wq in wordsQuery:
            t = suf_tree
            v = mn_len_idx
            for i in range(len(wq) - 1, -1, -1):
                if wq[i] not in t.sub:
                    break
                t = t.sub[wq[i]]
                v = t.content
            ans.append(v)
                
        return ans


if __name__ == '__main__':
    # [1,1,1]
    print(Solution().stringIndices(["abcd", "bcd", "xbcd"], wordsQuery=["cd", "bcd", "xyz"]))
    # [2,0,2]
    print(Solution().stringIndices(["abcdefgh", "poiuygh", "ghghgh"], wordsQuery=["gh", "acbfgh", "acbfegh"]))
