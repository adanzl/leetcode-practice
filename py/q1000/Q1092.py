"""
 * 给出两个字符串 str1 和 str2，返回同时以 str1 和 str2 作为子序列的最短字符串。如果答案不止一个，则可以返回满足条件的任意一个答案。
 * （如果从字符串 T 中删除一些字符（也可能不删除，并且选出的这些字符可以位于 T 中的 任意位置），可以得到字符串 S，那么 S 就是 T 的子序列）
 * 提示：
 * 1、1 <= str1.length, str2.length <= 1000
 * 2、str1 和 str2 都由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/shortest-common-supersequence/submissions/
"""


class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # LCS
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        ans = ""
        i, j = m, n
        while i and j:
            if dp[i][j] == dp[i][j - 1]:
                ans += str2[j - 1]
                j -= 1
            elif dp[i][j] == dp[i - 1][j]:
                ans += str1[i - 1]
                i -= 1
            else:
                ans += str1[i - 1]
                i -= 1
                j -= 1
        ans = ans[::-1]
        if i:
            ans = str1[:i] + ans
        if j:
            ans = str2[:j] + ans

        return ans


if __name__ == '__main__':
    # "dddbbdcbccaaaccbababaacbdcbacddadcdacbdddcadccacddbadcadcbabdaccbccdcdcbaaabcaccacbbdcbaabb"
    print(Solution().shortestCommonSupersequence("bcaaacbbbcbdcaddadcacbdddcdcccdadadcbabaccbccdcdcbcaccacbbdcbabb", "dddbbdcbccaccbababaacbcbacdddcdabadcacddbacadabdabcdbaaabaccbdaa"))
    # "cabac"
    print(Solution().shortestCommonSupersequence("abac", "cab"))
    # "aaaaaaaa"
    print(Solution().shortestCommonSupersequence("aaaaaaaa", "aaaaaaaa"))