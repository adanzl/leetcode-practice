"""
 * 给你一个字符串 num ，表示一个大整数。请你在字符串 num 的所有 非空子字符串 中找出 值最大的奇数 ，并以字符串形式返回。
 * 如果不存在奇数，则返回一个空字符串 "" 。
 * 子字符串 是字符串中的一个连续的字符序列。
 * 提示：
 * 1、1 <= num.length <= 10^5
 * 2、num 仅由数字组成且不含前导零
 * 链接：https://leetcode.cn/problems/largest-odd-number-in-string
"""

from typing import List

#
# @lc app=leetcode.cn id=1903 lang=python3
#
# [1903] 字符串中的最大奇数
#


# @lc code=start
class Solution:

    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ''


# @lc code=end

if __name__ == '__main__':
    # "5"
    print(Solution().largestOddNumber("52"))
    # ""
    print(Solution().largestOddNumber("4206"))
    # "35427"
    print(Solution().largestOddNumber("35427"))
