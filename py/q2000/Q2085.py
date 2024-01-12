"""
 * 给你两个字符串数组 words1 和 words2 ，请你返回在两个字符串数组中 都恰好出现一次 的字符串的数目。
 * 提示：
 * 1、1 <= words1.length, words2.length <= 1000
 * 2、1 <= words1[i].length, words2[j].length <= 30
 * 3、words1[i] 和 words2[j] 都只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/count-common-words-with-one-occurrence
"""

from typing import Counter, List

#
# @lc app=leetcode.cn id=2085 lang=python3
#


# @lc code=start
class Solution:

    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ans = 0
        cnt1, cnt2 = Counter(words1), Counter(words2)
        for w, c in cnt1.items():
            if c == 1 and cnt2[w] == 1:
                ans += 1

        return ans


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().countWords(["leetcode", "is", "amazing", "as", "is"], words2=["amazing", "leetcode", "is"]))
    # 0
    print(Solution().countWords(["b", "bb", "bbb"], words2=["a", "aa", "aaa"]))
    # 1
    print(Solution().countWords(["a", "ab"], words2=["a", "a", "a", "ab"]))
