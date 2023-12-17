"""
 * 给你一个下标从 0 开始的字符串 word 。
 * 一次操作中，你可以选择 word 中任意一个下标 i ，将 word[i] 修改成任意一个小写英文字母。
 * 请你返回消除 word 中所有相邻 近似相等 字符的 最少 操作次数。
 * 两个字符 a 和 b 如果满足 a == b 或者 a 和 b 在字母表中是相邻的，那么我们称它们是 近似相等 字符。
 * 提示：
 * 1、1 <= word.length <= 100
 * 2、word 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/remove-adjacent-almost-equal-characters/
"""


class Solution:

    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        dp = [1, 0]  # 变-不变
        for i in range(1, n):
            if abs(ord(word[i]) - ord(word[i - 1])) <= 1:
                ndp = [min(dp) + 1, dp[0]]
            else:
                ndp = [min(dp) + 1, min(dp)]
            dp = ndp
        return min(dp)


if __name__ == '__main__':
    # 2
    print(Solution().removeAlmostEqualCharacters('aaaaa'))
    # 2
    print(Solution().removeAlmostEqualCharacters('abddez'))
    # 3
    print(Solution().removeAlmostEqualCharacters('zyxyxyz'))
