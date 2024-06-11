"""
 * 给你一个字符串 s ，你需要将它分割成一个或者更多的 平衡 子字符串。
 * 比方说，s == "ababcc" 那么 ("abab", "c", "c") ，("ab", "abc", "c") 和 ("ababcc") 都是合法分割，
 * 但是 ("a", "bab", "cc") ，("aba", "bc", "c") 和 ("ab", "abcc") 不是，不平衡的子字符串用粗体表示。
 * 请你返回 s 最少 能分割成多少个平衡子字符串。
 * 注意：一个 平衡 字符串指的是字符串中所有字符出现的次数都相同。
 * 提示：
 * 1、1 <= s.length <= 1000
 * 2、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/minimum-substring-partition-of-equal-character-frequency/
"""
from collections import Counter


class Solution:

    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(n + 1)]
        dp[0] = 0

        for i in range(n):
            cnt = Counter({s[i]: 1})
            dp[i + 1] = dp[i] + 1
            for j in range(i - 1, -1, -1):
                cnt[s[j]] += 1
                if len(set(cnt.values())) == 1:
                    dp[i + 1] = min(dp[i + 1], dp[j] + 1)
        return dp[-1]


if __name__ == '__main__':
    # 2
    print(Solution().minimumSubstringsInPartition("bccbaacabc"))
    # 3
    print(Solution().minimumSubstringsInPartition("fabccddg"))
    # 2
    print(Solution().minimumSubstringsInPartition("abababaccddb"))
