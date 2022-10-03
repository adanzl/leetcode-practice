"""
 * 给你一个仅由小写英文字母组成的字符串 s 。在一步操作中，你可以：
 * 1、删除 整个字符串 s ，或者
 * 2、对于满足 1 <= i <= s.length / 2 的任意 i ，如果 s 中的 前 i 个字母和接下来的 i 个字母 相等 ，删除 前 i 个字母。
 * 例如，如果 s = "ababc" ，那么在一步操作中，你可以删除 s 的前两个字母得到 "abc" ，因为 s 的前两个字母和接下来的两个字母都等于 "ab" 。
 * 返回删除 s 所需的最大操作数。
 * 提示：
 * 1、1 <= s.length <= 4000
 * 2、s 仅由小写英文字母组成
 * 链接：https://leetcode.cn/problems/maximum-deletions-on-a-string/
"""
from typing import *
from math import *
from collections import *


class Solution:

    def deleteString(self, s: str) -> int:
        n = len(s)
        dp = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            for j in range(i, (n + i) // 2):
                if s[i:j + 1] == s[j + 1:j + j - i + 2]:
                    dp[i] = max(dp[i], 1 + dp[j + 1])
        return dp[0]


if __name__ == '__main__':
    # 5
    print(Solution().deleteString("aaaaa"))
    # 2
    print(Solution().deleteString("abcabcdabc"))
    # 4
    print(Solution().deleteString("aaabaab"))