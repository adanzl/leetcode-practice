"""
 * 给你一个字符串 s 和一个 正 整数 k 。
 * 从字符串 s 中选出一组满足下述条件且 不重叠 的子字符串：
 * 1、每个子字符串的长度 至少 为 k 。
 * 2、每个子字符串是一个 回文串 。
 * 返回最优方案中能选择的子字符串的 最大 数目。
 * 子字符串 是字符串中一个连续的字符序列。
 * 提示：
 * 1、1 <= k <= s.length <= 2000
 * 2、s 仅由小写英文字母组成
 * 链接：https://leetcode.cn/problems/maximum-number-of-non-overlapping-palindrome-substrings/
"""


class Solution:

    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        def is_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True

        p_cnt = [0] * (n)
        for r in range(n):
            for l in range(r - k + 1, -1, -1):
                if is_palindrome(s, l, r):
                    p_cnt[r] = r - l + 1
                    break
        for i in range(n):
            dp[i + 1] = max(dp[i], dp[i - p_cnt[i] + 1] + 1) if p_cnt[i] else dp[i]
        return dp[-1]


if __name__ == '__main__':
    # 2
    print(Solution().maxPalindromes("kwnwkekokedadq", 5))
    # 4
    print(Solution().maxPalindromes("fttfjofpnpfydwdwdnns", 2))
    # 2
    print(Solution().maxPalindromes("abaccdbbd", k=3))
    # 0
    print(Solution().maxPalindromes("adbcda", k=2))
