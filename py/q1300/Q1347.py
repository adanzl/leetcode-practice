"""
 * 给你两个长度相等的字符串 s 和 t。每一个步骤中，你可以选择将 t 中的 任一字符 替换为 另一个字符。
 * 返回使 t 成为 s 的字母异位词的最小步骤数。
 * 字母异位词 指字母相同，但排列不同（也可能相同）的字符串。
 * 提示：
 * 1、1 <= s.length <= 50000
 * 2、s.length == t.length
 * 3、s 和 t 只包含小写英文字母
 * 链接：https://leetcode.cn/problems/minimum-number-of-steps-to-make-two-strings-anagram
"""

from typing import Counter

#
# @lc app=leetcode.cn id=1347 lang=python3
#
# [1347] 制造字母异位词的最小步骤数
#


# @lc code=start
class Solution:

    def minSteps(self, s: str, t: str) -> int:
        cnt_s, cnt_t = Counter(s), Counter(t)
        ans = 0
        c_i, c_o = 0, 0
        for k, v in cnt_s.items():
            ans += abs(v - cnt_t[k])
        for k, v in cnt_t.items():
            if v and k not in cnt_s:
                ans += v
        return ans // 2


# @lc code=end

if __name__ == '__main__':
    # 5
    print(Solution().minSteps("leetcode", t="practice"))
    # 1
    print(Solution().minSteps("bab", t="aba"))
    # 0
    print(Solution().minSteps("anagram", t="mangaar"))
    # 0
    print(Solution().minSteps("xxyyzz", t="xxyyzz"))
    # 4
    print(Solution().minSteps("friend", t="family"))
