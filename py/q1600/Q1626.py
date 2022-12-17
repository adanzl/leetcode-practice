"""
 * 假设你是球队的经理。对于即将到来的锦标赛，你想组合一支总体得分最高的球队。球队的得分是球队中所有球员的分数 总和 。
 * 然而，球队中的矛盾会限制球员的发挥，所以必须选出一支 没有矛盾 的球队。如果一名年龄较小球员的分数 严格大于 一名年龄较大的球员，则存在矛盾。同龄球员之间不会发生矛盾。
 * 给你两个列表 scores 和 ages，其中每组 scores[i] 和 ages[i] 表示第 i 名球员的分数和年龄。请你返回 所有可能的无矛盾球队中得分最高那支的分数 。
 * 提示：
 * 1、1 <= scores.length, ages.length <= 1000
 * 2、scores.length == ages.length
 * 3、1 <= scores[i] <= 10^6
 * 4、1 <= ages[i] <= 1000
 * 链接：https://leetcode.cn/problems/best-team-with-no-conflicts/
"""
from typing import List


class Solution:

    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = sorted(zip(scores, ages))
        dp = [0] * 1001
        
        for s, a in arr:
            mx = 0
            for j in range(a + 1):
                mx = max(mx, dp[j])
            dp[a] = mx + s
        return max(dp)


if __name__ == '__main__':
    # 27
    print(Solution().bestTeamScore([9, 2, 8, 8, 2], [4, 1, 3, 3, 5]))
    # 16
    print(Solution().bestTeamScore([4, 5, 6, 5], [2, 1, 2, 1]))
    # 34
    print(Solution().bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]))
    # 6
    print(Solution().bestTeamScore([1, 2, 3, 5], [8, 9, 10, 1]))
