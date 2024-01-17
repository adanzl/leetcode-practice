"""
 * 给你一个下标从 0 开始的数组 words ，数组中包含 互不相同 的字符串。
 * 如果字符串 words[i] 与字符串 words[j] 满足以下条件，我们称它们可以匹配：
 * 1、字符串 words[i] 等于 words[j] 的反转字符串。
 * 2、0 <= i < j < words.length
 * 请你返回数组 words 中的 最大 匹配数目。
 * 注意，每个字符串最多匹配一次。
 * 提示：
 * 1、1 <= words.length <= 50
 * 2、words[i].length == 2
 * 3、words 包含的字符串互不相同。
 * 4、words[i] 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/find-maximum-number-of-string-pairs
"""

from typing import List

#
# @lc app=leetcode.cn id=2744 lang=python3
#
# [2744] 最大字符串配对数目
#


# @lc code=start
class Solution:

    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        s = set(words)
        for w in s:
            rs = w[::-1]
            if w != rs and rs in s:
                ans += 1
        return ans // 2


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().maximumNumberOfStringPairs(["cd", "ac", "dc", "ca", "zz"]))
    # 1
    print(Solution().maximumNumberOfStringPairs(["ab", "ba", "cc"]))
    # 0
    print(Solution().maximumNumberOfStringPairs(["aa", "ab"]))
