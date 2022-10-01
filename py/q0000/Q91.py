"""
 * 一条包含字母 A-Z 的消息通过以下方式进行了编码：
 * 'A' -> 1
 * 'B' -> 2
 * ...
 * 'Z' -> 26
 * 给定一个只包含数字的非空字符串，请计算解码方法的总数。
 * 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
 * 1、"AAJF" ，将消息分组为 (1 1 10 6)
 * 2、"KJF" ，将消息分组为 (11 10 6)
 * 注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
 * 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
 * 题目数据保证答案肯定是一个 32 位 的整数。
 * 提示：
 * 1、1 <= s.length <= 100
 * 2、s 只包含数字，并且可能包含前导零。
 * 链接：https://leetcode-cn.com/problems/decode-ways
"""
from typing import *


class Solution:

    def numDecodings(self, s: str) -> int:
        c_dict = dict(zip([str(x) for x in range(1, 27)], 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        pre = 1 if s[0] != '0' else 0
        ans = pre
        for i in range(1, len(s)):
            t = ans
            if s[i] not in c_dict:
                ans = 0
            if s[i - 1:i + 1] in c_dict:
                ans += pre
            pre = t
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().numDecodings("2101"))
    # 0
    print(Solution().numDecodings("00"))
    # 3
    print(Solution().numDecodings("226"))