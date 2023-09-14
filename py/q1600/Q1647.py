"""
 * 如果字符串 s 中 不存在 两个不同字符 频次 相同的情况，就称 s 是 优质字符串 。
 * 给你一个字符串 s，返回使 s 成为 优质字符串 需要删除的 最小 字符数。
 * 字符串中字符的 频次 是该字符在字符串中的出现次数。
 * 例如，在字符串 "aab" 中，'a' 的频次是 2，而 'b' 的频次是 1 。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 仅含小写英文字母
 * 链接：https://leetcode.cn/problems/minimum-deletions-to-make-character-frequencies-unique/
"""

from typing import Counter

#
# @lc app=leetcode.cn id=1647 lang=python3
#
# [1647] 字符频次唯一的最小删除次数
#


# @lc code=start
class Solution:

    def minDeletions(self, s: str) -> int:
        ans = 0
        ss = sorted(Counter(s).values(), reverse=True)
        pre = ss[0]
        for i in range(1, len(ss)):
            limit = max(min(pre - 1, ss[i]), 0)
            ans += ss[i] - limit
            pre = limit
        return ans


# @lc code=end

if __name__ == '__main__':
    # 0
    print(Solution().minDeletions("aab"))
    # 2
    print(Solution().minDeletions("aaabbbcc"))
    # 2
    print(Solution().minDeletions("ceabaacb"))
