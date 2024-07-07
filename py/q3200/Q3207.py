"""
 * 给你一个下标从 0 开始的整数数组 enemyEnergies ，它表示一个下标从 0 开始的敌人能量数组。
 * 同时给你一个整数 currentEnergy ，它表示你一开始拥有的能量值总量。
 * 你一开始的分数为 0 ，且一开始所有的敌人都未标记。
 * 你可以通过以下操作 之一 任意次（也可以 0 次）来得分：
 * 1、选择一个 未标记 且满足 currentEnergy >= enemyEnergies[i] 的敌人 i 。在这个操作中：
 *      你会获得 1 分。
 *      你的能量值减少 enemyEnergies[i] ，也就是说 currentEnergy = currentEnergy - enemyEnergies[i] 。
 * 2、如果你目前 至少 有 1 分，你可以选择一个 未标记 的敌人 i 。在这个操作中：
 *      你的能量值增加 enemyEnergies[i] ，也就是说 currentEnergy = currentEnergy + enemyEnergies[i] 。
 *      敌人 i 被标记 。
 * 请你返回通过以上操作，最多 可以获得多少分。
 * 提示：
 * 1、1 <= enemyEnergies.length <= 10^5
 * 2、1 <= enemyEnergies[i] <= 10^9
 * 3、0 <= currentEnergy <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-points-after-enemy-battles/
"""
from typing import List


class Solution:

    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        if currentEnergy < enemyEnergies[0]: return 0
        currentEnergy += sum(enemyEnergies) - enemyEnergies[0]
        return currentEnergy // enemyEnergies[0]


if __name__ == '__main__':
    # 3
    print(Solution().maximumPoints([3, 2, 2], currentEnergy=2))
    # 5
    print(Solution().maximumPoints([2], currentEnergy=10))
