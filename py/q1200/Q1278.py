"""
 * 给你一个由小写字母组成的字符串 s，和一个整数 k。
 * 请你按下面的要求分割字符串：
 * 1、首先，你可以将 s 中的部分字符修改为其他的小写英文字母。
 * 2、接着，你需要把 s 分割成 k 个非空且不相交的子串，并且每个子串都是回文串。
 * 3、请返回以这种方式分割字符串所需修改的最少字符数。
 * 提示：
 * 1、1 <= k <= s.length <= 100
 * 2、s 中只含有小写英文字母。
 * 链接：https://leetcode.cn/problems/palindrome-partitioning-iii/
"""

from functools import cache


class Solution:

    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        ans = n

        @cache
        def edit_dis(l, r):
            if l == r: return 0
            return (edit_dis(l + 1, r - 1) if r - l > 1 else 0) + (0 if s[l] == s[r] else 1)

        dp = [[0x3c3c3c3c] * (k + 1) for _ in range(n + 1)]  # char count - seg cnt - min_edit_dis
        dp[0][0] = 0
        for i in range(1, n + 1):  # char count
            for j in range(1, k + 1):  # seg cnt
                for l in range(1, i - j + 2):  # last seg length
                    dp[i][j] = min(dp[i][j], dp[i - l][j - 1] + edit_dis(i - l, i - 1))

        return dp[n][k]


if __name__ == '__main__':
    # 1
    print(Solution().palindromePartition("abc", 2))
    # 0
    print(Solution().palindromePartition("aabbc", 3))
    # 0
    print(Solution().palindromePartition("leetcode", 8))