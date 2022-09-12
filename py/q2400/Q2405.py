from typing import *
"""
 * 给你一个字符串 s ，请你将该字符串划分成一个或多个 子字符串 ，并满足每个子字符串中的字符都是 唯一 的。也就是说，在单个子字符串中，字母的出现次数都不超过 一次 。
 * 满足题目要求的情况下，返回 最少 需要划分多少个子字符串。
 * 注意，划分后，原字符串中的每个字符都应该恰好属于一个子字符串。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 仅由小写英文字母组成
 * 链接：https://leetcode.cn/problems/optimal-partition-of-string
"""


class Solution:

    def partitionString(self, s: str) -> int:
        ans, set_ = 0, set()
        for c in s:
            if c in set_:
                ans += 1
                set_.clear()
            set_.add(c)
        return ans + 1


if __name__ == '__main__':
    # 4
    print(Solution().partitionString('abacaba'))
    # 6
    print(Solution().partitionString('ssssss'))
