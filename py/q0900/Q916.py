"""
 * 给你两个字符串数组 words1 和 words2。
 * 现在，如果 b 中的每个字母都出现在 a 中，包括重复出现的字母，那么称字符串 b 是字符串 a 的 子集 。
 * 例如，"wrr" 是 "warrior" 的子集，但不是 "world" 的子集。
 * 如果对 words2 中的每一个单词 b，b 都是 a 的子集，那么我们称 words1 中的单词 a 是 通用单词 。
 * 以数组形式返回 words1 中所有的通用单词。你可以按 任意顺序 返回答案。
 * 提示：
 * 1、1 <= words1.length, words2.length <= 10^4
 * 2、1 <= words1[i].length, words2[i].length <= 10
 * 3、words1[i] 和 words2[i] 仅由小写英文字母组成
 * 4、words1 中的所有字符串 互不相同
 * 链接：https://leetcode.cn/problems/word-subsets/
"""

from typing import Counter, List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=916 lang=python3
# @lcpr version=20004
#
# [916] 单词子集
#


# @lc code=start
class Solution:

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        wc = Counter()
        for w in words2:
            c2 = Counter(w)
            for k, v in c2.items():
                wc[k] = max(wc[k], v)
        ans = []
        for w in words1:
            c1 = Counter(w)
            for k, v in wc.items():
                if c1[k] < v:
                    break
            else:
                ans.append(w)
        return ans


# @lc code=end

#

if __name__ == '__main__':
    # ["facebook","google","leetcode"]
    print(Solution().wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]))
    # ["apple","google","leetcode"]
    print(Solution().wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]))
    # ["facebook","google"]
    print(Solution().wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "oo"]))
    # ["google","leetcode"]
    print(Solution().wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["lo", "eo"]))
    # ["facebook","leetcode"]
    print(Solution().wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["ec", "oc", "ceo"]))
