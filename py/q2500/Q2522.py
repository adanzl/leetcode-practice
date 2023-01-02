"""
 * 给你一个字符串 s ，它每一位都是 1 到 9 之间的数字组成，同时给你一个整数 k 。
 * 如果一个字符串 s 的分割满足以下条件，我们称它是一个 好 分割：
 * 1、s 中每个数位 恰好 属于一个子字符串。
 * 2、每个子字符串的值都小于等于 k 。
 * 请你返回 s 所有的 好 分割中，子字符串的 最少 数目。如果不存在 s 的 好 分割，返回 -1 。
 * 注意：
 * 1、一个字符串的 值 是这个字符串对应的整数。比方说，"123" 的值为 123 ，"1" 的值是 1 。
 * 2、子字符串 是字符串中一段连续的字符序列。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s[i] 是 '1' 到 '9' 之间的数字。
 * 3、1 <= k <= 10^9
 * 链接：https://leetcode.cn/problems/partition-string-into-substrings-with-values-at-most-k/
"""


class Solution:

    def minimumPartition(self, s: str, k: int) -> int:
        n, m = len(s), len(str(k))
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for i in range(n):
            for j in range(1, min(i + 2, m + 1)):
                v = int(s[i - j + 1:i + 1])
                if v > k: break
                dp[i + 1] = min(dp[i + 1], dp[i + 1 - j] + 1)
        return dp[-1] if dp[-1] < n + 1 else -1


if __name__ == '__main__':
    # 4
    print(Solution().minimumPartition("165462", 60))
    # -1
    print(Solution().minimumPartition("238182", 5))
    # 1
    print(Solution().minimumPartition("1", 1))