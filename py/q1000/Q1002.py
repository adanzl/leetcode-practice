"""
 * 给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（ 包括重复字符），并以数组形式返回。
 * 你可以按 任意顺序 返回答案。
 * 提示：
 * 1、1 <= words.length <= 100
 * 2、1 <= words[i].length <= 100
 * 3、words[i] 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/find-common-characters
"""

import string
from typing import Counter, List

#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#


# @lc code=start
class Solution:

    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        for c in string.ascii_lowercase:
            cnt = 0x3c3c3c3c
            for w in words:
                cnt = min(cnt, Counter(w)[c])
            for _ in range(cnt):
                ans.append(c)
        return ans


# @lc code=end

if __name__ == '__main__':
    # ["e","l","l"]
    print(Solution().commonChars(["bella", "label", "roller"]))
    # ["c","o"]
    print(Solution().commonChars(["cool", "lock", "cook"]))
