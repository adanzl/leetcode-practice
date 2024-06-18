"""
 * 在神秘的地牢中，n 个魔法师站成一排。
 * 每个魔法师都拥有一个属性，这个属性可以给你提供能量。
 * 有些魔法师可能会给你负能量，即从你身上吸取能量。
 * 你被施加了一种诅咒，当你从魔法师 i 处吸收能量后，你将被立即传送到魔法师 (i + k) 处。
 * 这一过程将重复进行，直到你到达一个不存在 (i + k) 的魔法师为止。
 * 换句话说，你将选择一个起点，然后以 k 为间隔跳跃，直到到达魔法师序列的末端，在过程中吸收所有的能量。
 * 给定一个数组 energy 和一个整数k，返回你能获得的 最大 能量。
 * 提示：
 * 1、1 <= energy.length <= 10^5
 * 2、-1000 <= energy[i] <= 1000
 * 3、1 <= k <= energy.length - 1
 * 链接：https://leetcode.cn/problems/taking-maximum-energy-from-the-mystic-dungeon/
"""
from typing import List


class Solution:

    def maximumEnergy(self, energy: List[int], k: int) -> int:
        score = [0] * k
        for i, e in enumerate(energy):
            score[i % k] = max(0, score[i % k]) + e
        return max(score)


if __name__ == '__main__':
    # 3
    print(Solution().maximumEnergy([5, 2, -10, -5, 1], k=3))
    # -1
    print(Solution().maximumEnergy([-2, -3, -1], k=2))
    #
    # print(Solution().maximumEnergy())
