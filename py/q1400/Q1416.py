"""
 * 某个程序本来应该输出一个整数数组。但是这个程序忘记输出空格了以致输出了一个数字字符串，我们所知道的信息只有：数组中所有整数都在 [1, k] 之间，且数组中的数字都没有前导 0 。
 * 给你字符串 s 和整数 k 。可能会有多种不同的数组恢复结果。
 * 按照上述程序，请你返回所有可能输出字符串 s 的数组方案数。
 * 由于数组方案数可能会很大，请你返回它对 10^9 + 7 取余 后的结果。
 * 提示：
 * 1、1 <= s.length <= 10^5.
 * 2、s 只包含数字且不包含前导 0 。
 * 3、1 <= k <= 10^9.
 * 链接：https://leetcode.cn/problems/restore-the-array/
"""


class Solution:

    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n, nk = len(s), len(str(k))
        dp = [1] + [0] * (n)
        for i in range(n):
            num = int(s[i])
            if num > k: return 0
            dp[i + 1] = dp[i] if num else 0
            for l in range(1, min(i, nk) + 1):
                num += int(s[i - l]) * 10**l
                if num > k : break
                if s[i - l] == '0': continue
                dp[i + 1] += dp[i - l]
            dp[i + 1] %= MOD
        return dp[-1]


if __name__ == '__main__':
    # 1
    print(Solution().numberOfArrays("1000", 10000))
    # 0
    print(Solution().numberOfArrays("1000", 10))
    # 8
    print(Solution().numberOfArrays("1317", 2000))
    # 1
    print(Solution().numberOfArrays("2020", 30))
    # 34
    print(Solution().numberOfArrays("1234567890", 90))
