"""
 * 来自未来的体育科学家给你两个整数数组 energyDrinkA 和 energyDrinkB，数组长度都等于 n。
 * 这两个数组分别代表 A、B 两种不同能量饮料每小时所能提供的强化能量。
 * 你需要每小时饮用一种能量饮料来 最大化 你的总强化能量。
 * 然而，如果从一种能量饮料切换到另一种，你需要等待一小时来梳理身体的能量体系（在那个小时里你将不会获得任何强化能量）。
 * 返回在接下来的 n 小时内你能获得的 最大 总强化能量。
 * 注意 你可以选择从饮用任意一种能量饮料开始。
 * 提示：
 * 1、n == energyDrinkA.length == energyDrinkB.length
 * 2、3 <= n <= 10^5
 * 3、1 <= energyDrinkA[i], energyDrinkB[i] <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dp = [[0, 0] for _ in range(n + 1)]
        dp[1] = [energyDrinkA[0], energyDrinkB[0]]
        for i in range(1, n):
            dp[i + 1][0] = max(dp[i][0], dp[i - 1][1]) + energyDrinkA[i]
            dp[i + 1][1] = max(dp[i][1], dp[i - 1][0]) + energyDrinkB[i]
        return max(dp[-1])


if __name__ == '__main__':
    # 7
    print(Solution().maxEnergyBoost([4, 1, 1], energyDrinkB=[1, 1, 3]))
    # 5
    print(Solution().maxEnergyBoost([1, 3, 1], energyDrinkB=[3, 1, 1]))
