"""
 * 考试中有 n 种类型的题目。给你一个整数 target 和一个下标从 0 开始的二维整数数组 types ，其中 types[i] = [count_i, marks_i] 表示第 i 种类型的题目有 count_i 道，每道题目对应 marks_i 分。
 * 返回你在考试中恰好得到 target 分的方法数。由于答案可能很大，结果需要对 109 +7 取余。
 * 注意，同类型题目无法区分。
 * 比如说，如果有 3 道同类型题目，那么解答第 1 和第 2 道题目与解答第 1 和第 3 道题目或者第 2 和第 3 道题目是相同的。
 * 提示：
 * 1、1 <= target <= 1000
 * 2、n == types.length
 * 3、1 <= n <= 50
 * 4、types[i].length == 2
 * 5、1 <= count_i, marks_i <= 50
 * 链接：https://leetcode.cn/problems/number-of-ways-to-earn-points/
"""
from typing import List


class Solution:

    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10**9 + 7
        dp = [1] + [0] * (target)
        for c, s in types:
            ndp = dp[:]
            for i in range(1, c + 1):
                for j in range(s * i, target + 1):
                    ndp[j] += dp[j - s * i]
                    ndp[j] %= MOD
            dp = ndp
        return dp[target] % MOD


if __name__ == '__main__':
    # 7
    print(Solution().waysToReachTarget(6, types=[[6, 1], [3, 2], [2, 3]]))
    # 4
    print(Solution().waysToReachTarget(5, types=[[50, 1], [50, 2], [50, 5]]))
    # 1
    print(Solution().waysToReachTarget(18, types=[[6, 1], [3, 2], [2, 3]]))
