"""
 * 给你一个正整数 primeFactors 。你需要构造一个正整数 n ，它满足以下条件：
 * 1、n 质因数（质因数需要考虑重复的情况）的数目 不超过 primeFactors 个。
 * 2、n 好因子的数目最大化。如果 n 的一个因子可以被 n 的每一个质因数整除，我们称这个因子是 好因子 。
 *      比方说，如果 n = 12 ，那么它的质因数为 [2,2,3] ，那么 6 和 12 是好因子，但 3 和 4 不是。
 * 请你返回 n 的好因子的数目。由于答案可能会很大，请返回答案对 10^9 + 7 取余 的结果。
 * 请注意，一个质数的定义是大于 1 ，且不能被分解为两个小于该数的自然数相乘。
 * 一个数 n 的质因子是将 n 分解为若干个质因子，且它们的乘积为 n 。
 * 提示：1 <= primeFactors <= 10^9
 * 链接：https://leetcode.cn/problems/maximize-number-of-nice-divisors/
"""

#
# @lc app=leetcode.cn id=1808 lang=python3
#
# [1808] 好因子的最大数目
#


# @lc code=start
class Solution:

    def maxNiceDivisors(self, primeFactors: int) -> int:
        # n对3取模为0：ans = pow(3,n/3)
        # n对3取模为1：ans = pow(3,n/3 - 1) * 2 * 2
        # n对3取模为2：ans = pow(3,n/3) * 2
        # https://leetcode.cn/problems/maximize-number-of-nice-divisors/solutions/685614/wan-zheng-tui-dao-si-lu-wei-shi-yao-yao-di8x6
        if primeFactors == 1: return 1
        MOD = 10**9 + 7
        a, r = divmod(primeFactors, 3)
        if r == 0:
            return pow(3, a, MOD)
        elif r == 1:
            return (pow(3, a - 1, MOD) << 2) % MOD
        elif r == 2:
            return (pow(3, a, MOD) << 1) % MOD
        return -1


# @lc code=end

if __name__ == '__main__':
    # 620946522
    print(Solution().maxNiceDivisors(1000))
    # 18
    print(Solution().maxNiceDivisors(8))
    # 27
    print(Solution().maxNiceDivisors(9))
    # 6
    print(Solution().maxNiceDivisors(5))
    # 897135186
    print(Solution().maxNiceDivisors(10**9))
