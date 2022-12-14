"""
 * 给你一个字符串 s ，如果可以将它分割成三个 非空 回文子字符串，那么返回 true ，否则返回 false 。
 * 当一个字符串正着读和反着读是一模一样的，就称其为 回文字符串 。
 * 提示：
 * 1、3 <= s.length <= 2000
 * 2、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/palindrome-partitioning-iv/
"""

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n)]  # 构建回文对
        for i in range(n):
            l = r = i
            while l >=0 and r < n and s[l] == s[r]:
                dp[l][r] = True
                r += 1
                l -= 1
            l, r = i, i+1
            while l >=0 and r < n and s[l] == s[r]:
                dp[l][r] = True
                r += 1
                l -= 1
        for i in range(n-2):
            for j in range(i + 1, n-1):
                if dp[0][i] and dp[i+1][j] and dp[j+1][n-1]: return True
        return False

if __name__ == '__main__':
    # True
    print(Solution().checkPartitioning("abcbdd"))
    # False
    print(Solution().checkPartitioning("bcbddxy"))