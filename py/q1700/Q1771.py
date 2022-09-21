"""
 * 给你两个字符串 word1 和 word2 ，请你按下述方法构造一个字符串：
 * 1、从 word1 中选出某个 非空 子序列 subsequence1 。
 * 2、从 word2 中选出某个 非空 子序列 subsequence2 。
 * 3、连接两个子序列 subsequence1 + subsequence2 ，得到字符串。
 * 返回可按上述方法构造的最长 回文串 的 长度 。如果无法构造回文串，返回 0 。
 * 字符串 s 的一个 子序列 是通过从 s 中删除一些（也可能不删除）字符而不更改其余字符的顺序生成的字符串。
 * 回文串 是正着读和反着读结果一致的字符串。
 * 提示：
 * 1、1 <= word1.length, word2.length <= 1000
 * 2、word1 和 word2 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/maximize-palindrome-length-from-subsequences/
"""
from typing import *


class Solution:

    def longestPalindrome(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        word = word1 + word2
        dp = [[0] * (l1 + l2) for _ in range(l1 + l2)]  # l-r
        n = l1 + l2
        for i in range(n):
            dp[i][i] = 1
        ans = 0
        for l in range(n - 1, -1, -1):
            for r in range(l + 1, n):
                if word[r] == word[l]:
                    dp[l][r] = dp[l + 1][r - 1] + 2
                    if dp[l][r] > ans and l < l1 and r >= l1:
                        ans = dp[l][r]
                else:
                    dp[l][r] = max(dp[l][r - 1], dp[l + 1][r])
        return ans


if __name__ == '__main__':
    # 0
    print(Solution().longestPalindrome("aa", "bb"))
    # 6
    print(Solution().longestPalindrome("afaaadacb", "ca"))
    # 5
    print(Solution().longestPalindrome("cacb", "cbba"))
    # 3
    print(Solution().longestPalindrome("ab", "ab"))