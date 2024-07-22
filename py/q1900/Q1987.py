"""
 * 给你一个二进制字符串 binary 。 
 * binary 的一个 子序列 如果是 非空 的且没有 前导 0 （除非数字是 "0" 本身），那么它就是一个 好 的子序列。
 * 请你找到 binary 不同好子序列 的数目。
 * 比方说，如果 binary = "001" ，那么所有 好 子序列为 ["0", "0", "1"] ，所以 不同 的好子序列为 "0" 和 "1" 。 
 * 注意，子序列 "00" ，"01" 和 "001" 不是好的，因为它们有前导 0 。
 * 请你返回 binary 中 不同好子序列 的数目。由于答案可能很大，请将它对 10^9 + 7 取余 后返回。
 * 一个 子序列 指的是从原数组中删除若干个（可以一个也不删除）元素后，不改变剩余元素顺序得到的序列。
 * 提示：
 * 1、1 <= binary.length <= 10^5
 * 2、binary 只含有 '0' 和 '1' 。
 * 链接：https://leetcode.cn/problems/number-of-unique-good-subsequences/
"""

#
# @lc app=leetcode.cn id=1987 lang=python3
#
# [1987] 不同的好子序列数目
#


# @lc code=start
class Solution:

    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        dp = [0, 0]
        MOD = 10**9 + 7
        for c in binary[::-1]:
            dp[int(c)] = (dp[0] + dp[1] + 1) % MOD
        if '0' in binary:
            dp[1] += 1
        return dp[1] % MOD


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().numberOfUniqueGoodSubsequences('001'))
    # 2
    print(Solution().numberOfUniqueGoodSubsequences('11'))
    # 5
    print(Solution().numberOfUniqueGoodSubsequences('101'))
