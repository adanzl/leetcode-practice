"""
 * n 名士兵站成一排。每个士兵都有一个 独一无二 的评分 rating 。
 * 每 3 个士兵可以组成一个作战单位，分组规则如下：
 * 1、从队伍中选出下标分别为 i、j、k 的 3 名士兵，他们的评分分别为 rating[i]、rating[j]、rating[k]
 * 2、作战单位需满足： rating[i] < rating[j] < rating[k] 或者 rating[i] > rating[j] > rating[k] ，其中  0 <= i < j < k < n
 * 请你返回按上述条件可以组建的作战单位数量。每个士兵都可以是多个作战单位的一部分。
 * 提示：
 * 1、n == rating.length
 * 2、3 <= n <= 1000
 * 3、1 <= rating[i] <= 10^5
 * 4、rating 中的元素都是唯一的
* 链接：https://leetcode.cn/problems/count-number-of-teams/
"""
from typing import List


class Solution:

    def numTeams(self, rating: List[int]) -> int:
        ans, n = 0, len(rating)
        dp = [[0] * 2 for _ in range(n + 1)]  # < >
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if rating[i] > rating[j]:
                    dp[i + 1][0] += 1
                    ans += dp[j + 1][0]
                if rating[i] < rating[j]:
                    dp[i + 1][1] += 1
                    ans += dp[j + 1][1]
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().numTeams([2, 5, 3, 4, 1]))
    # 0
    print(Solution().numTeams([2, 1, 3]))
    # 4
    print(Solution().numTeams([1, 2, 3, 4]))
