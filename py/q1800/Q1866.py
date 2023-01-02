"""
 * 有 n 根长度互不相同的木棍，长度为从 1 到 n 的整数。请你将这些木棍排成一排，并满足从左侧 可以看到 恰好 k 根木棍。
 * 从左侧 可以看到 木棍的前提是这个木棍的 左侧 不存在比它 更长的 木棍。
 * 例如，如果木棍排列为 [1,3,2,5,4] ，那么从左侧可以看到的就是长度分别为 1、3 、5 的木棍。
 * 给你 n 和 k ，返回符合题目要求的排列 数目 。由于答案可能很大，请返回对 10^9 + 7 取余 的结果。
 * 提示：
 * 1、1 <= n <= 1000
 * 2、1 <= k <= n
 * 链接：https://leetcode.cn/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/
"""


class Solution:

    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        # f(i, j) 表示前i个木棍可见j个的 排列数目，枚举最后一根火柴的情况
        # 1、最后一个可见，此时最后一位只能摆放 a[i]，f(i, j) = f(i-1, j-1)
        # 2、最后一个不可见，最后一位可以摆放 a[0]~a[i-1]，此时前 i-1 个木棍的长度 x = [0,1..x-1,x+1..i-1] 可见 j 个的 排列数目 恰好等于 f(i-1, j)
        # ** 判定相同依据：f(i-1, j)，i-1 个不同的长度的木棍，i = [0,1,2..i-1]，可见 j 个的排列数据 <=> 情况 2
        # 3、f(i, j) = f(i-1, j-1) + (i-1)*f(i-1, j)
        # f(i, j) 只和 f(i-1, j) 有关，可以空间优化
        dp = [0] * (k + 1)
        dp[0] = 1  # 第一次的时候要设置 0 状态为 1
        for i in range(n):
            for j in range(k, 0, -1):
                dp[j] = (dp[j - 1] + (i) * dp[j]) % MOD
            dp[0] = 0  # 除了第一次以外，此处都是 0，主要是由于空间优化引入的问题
        return dp[-1]


if __name__ == '__main__':
    # 3
    print(Solution().rearrangeSticks(3, 2))
    # 1
    print(Solution().rearrangeSticks(5, 5))
    # 647427950
    print(Solution().rearrangeSticks(20, 11))