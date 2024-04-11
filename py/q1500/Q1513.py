"""
 * 给你一个二进制字符串 s（仅由 '0' 和 '1' 组成的字符串）。
 * 返回所有字符都为 1 的子字符串的数目。
 * 由于答案可能很大，请你将它对 10^9 + 7 取模后返回。
 * 提示：
 * 1、s[i] == '0' 或 s[i] == '1'
 * 2、1 <= s.length <= 10^5
 * 链接：https://leetcode.cn/problems/number-of-substrings-with-only-1s
"""

from typing import List

#
# @lc app=leetcode.cn id=1513 lang=python3
#
# [1513] 仅含 1 的子串数
#


# @lc code=start
class Solution:

    def numSub(self, s: str) -> int:
        ans, len_1 = 0, 0
        for c in s:
            if c == '1':
                len_1 += 1
                ans = (ans + len_1) % (10**9 + 7)
            else:
                len_1 = 0
        return ans


# @lc code=end

if __name__ == '__main__':
    # 9
    print(Solution().numSub('0110111'))
    # 2
    print(Solution().numSub('101'))
    # 21
    print(Solution().numSub('111111'))
    # 0
    print(Solution().numSub('000'))
