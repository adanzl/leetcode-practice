"""
 * 给你 3 个正整数 zero ，one 和 limit 。
 * 一个 二进制数组 arr 如果满足以下条件，那么我们称它是 稳定的 ：
 * 1、0 在 arr 中出现次数 恰好 为 zero 。
 * 2、1 在 arr 中出现次数 恰好 为 one 。
 * 3、arr 中每个长度超过 limit 的 子数组 都 同时 包含 0 和 1 。
 * 请你返回 稳定 二进制数组的 总 数目。
 * 由于答案可能很大，将它对 10^9 + 7 取余 后返回。
 * 提示：1 <= zero, one, limit <= 1000
 * 链接：https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-ii
"""

#
# @lc app=leetcode.cn id=3130 lang=python3
#
# [3130] 找出所有稳定的二进制数组 II
#


# @lc code=start
class Solution:

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        # f[i][j][0] 最后一位是 0, i个0，j个1满足的个数
        # f[i+1][j+1][0] = f[i][j+1][0]+f[i][j+1][1]-f[i-limit][j+1][1]
        # f[i+1][j+1][1] = f[i+1][j][0]+f[i+1][j][1]-f[i+1][j-limit][0]
        f = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]
        f[0][0] = [1, 1]
        for i in range(min(limit, zero)):
            f[i + 1][0] = [1, 0]
        for i in range(min(one, limit)):
            f[0][i + 1] = [0, 1]
        for i in range(zero):
            for j in range(one):
                f[i + 1][j + 1][0] = f[i][j + 1][0] + f[i][j + 1][1]
                if i + 1 > limit:
                    f[i + 1][j + 1][0] -= f[i - limit][j + 1][1]
                f[i + 1][j + 1][1] = f[i + 1][j][0] + f[i + 1][j][1]
                if j + 1 > limit:
                    f[i + 1][j + 1][1] -= f[i + 1][j - limit][0]
        return sum(f[-1][-1]) % MOD


# @lc code=end

if __name__ == '__main__':
    # 1
    print(Solution().numberOfStableArrays(1, 4, 2))
    # 2
    print(Solution().numberOfStableArrays(1, one=1, limit=2))
    # 1
    print(Solution().numberOfStableArrays(1, one=2, limit=1))
    # 14
    print(Solution().numberOfStableArrays(3, one=3, limit=2))
