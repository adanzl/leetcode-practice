"""
 * 给你一个整数数组 rewardValues，长度为 n，代表奖励的值。
 * 最初，你的总奖励 x 为 0，所有下标都是 未标记 的。你可以执行以下操作 任意次 ：
 * 1、从区间 [0, n - 1] 中选择一个 未标记 的下标 i。
 * 2、如果 rewardValues[i] 大于 你当前的总奖励 x，则将 rewardValues[i] 加到 x 上（即 x = x + rewardValues[i]），并 标记 下标 i。
 * 以整数形式返回执行最优操作能够获得的 最大 总奖励。
 * 提示：
 * 1、1 <= rewardValues.length <= 5*10^4
 * 2、1 <= rewardValues[i] <= 5*10^4
 * 链接：https://leetcode.cn/problems/maximum-total-reward-using-operations-ii/
"""
from typing import List


class Solution:

    def maxTotalReward(self, rewardValues: List[int]) -> int:
        f = 1
        # 位优化
        for v in sorted(set(rewardValues)):
            f |= (f & ((1 << v) - 1)) << v
        return f.bit_length() - 1


if __name__ == '__main__':
    # 10
    print(Solution().maxTotalReward([10]))
    # 4
    print(Solution().maxTotalReward([1, 1, 3, 3]))
    # 11
    print(Solution().maxTotalReward([1, 6, 4, 3, 2]))
