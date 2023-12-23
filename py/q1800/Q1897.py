"""
 * 给你一个字符串数组 words（下标 从 0 开始 计数）。
 * 在一步操作中，需先选出两个 不同 下标 i 和 j，其中 words[i] 是一个非空字符串，
 * 接着将 words[i] 中的 任一 字符移动到 words[j] 中的 任一 位置上。
 * 如果执行任意步操作可以使 words 中的每个字符串都相等，返回 true ；否则，返回 false 。
 * 提示：
 * 1、1 <= words.length <= 100
 * 2、1 <= words[i].length <= 100
 * 3、words[i] 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/redistribute-characters-to-make-all-strings-equal/
"""

from typing import Counter, List

#
# @lc app=leetcode.cn id=1897 lang=python3
#
# [1897] 重新分配字符使所有字符串都相等
#


# @lc code=start
class Solution:

    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        cnt = Counter()
        for word in words:
            cnt += Counter(word)
        return all([v % n == 0 for v in cnt.values()])


# @lc code=end

if __name__ == '__main__':
    # True
    print(Solution().makeEqual(["abc", "aabc", "bc"]))
    # False
    print(Solution().makeEqual(["ab", "a"]))
    #
    # print(Solution().makeEqual())
