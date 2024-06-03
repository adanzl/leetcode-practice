"""
 * 如果某个字符串中 至多一个 字母出现 奇数 次，则称其为 最美 字符串。
 * 例如，"ccjjc" 和 "abab" 都是最美字符串，但 "ab" 不是。
 * 给你一个字符串 word ，该字符串由前十个小写英文字母组成（'a' 到 'j'）。
 * 请你返回 word 中 最美非空子字符串 的数目。
 * 如果同样的子字符串在 word 中出现多次，那么应当对 每次出现 分别计数。
 * 子字符串 是字符串中的一个连续字符序列。
 * 提示：
 * 1、1 <= word.length <= 10^5
 * 2、word 由从 'a' 到 'j' 的小写英文字母组成
 * 链接：https://leetcode.cn/problems/number-of-wonderful-substrings
"""

from typing import Counter

#
# @lc app=leetcode.cn id=1915 lang=python3
#
# [1915] 最美子字符串的数目
#


# @lc code=start
class Solution:

    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        flag, cnt = 0, Counter({0: 1})
        for c in word:
            flag ^= 1 << (ord(c) - ord('a') + 1)
            ans += cnt[flag]
            for i in range(15):
                ans += cnt[flag ^ (1 << i)]
            cnt[flag] += 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # 4
    print(Solution().wonderfulSubstrings("aba"))
    # 9
    print(Solution().wonderfulSubstrings("aabb"))
    # 2
    print(Solution().wonderfulSubstrings("he"))
