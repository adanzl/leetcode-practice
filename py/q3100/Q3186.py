"""
 * 一个魔法师有许多不同的咒语。
 * 给你一个数组 power ，其中每个元素表示一个咒语的伤害值，可能会有多个咒语有相同的伤害值。
 * 已知魔法师使用伤害值为 power[i] 的咒语时，他们就 不能 使用伤害为 power[i] - 2 ，
 * power[i] - 1 ，power[i] + 1 或者 power[i] + 2 的咒语。
 * 每个咒语最多只能被使用 一次 。
 * 请你返回这个魔法师可以达到的伤害值之和的 最大值 。
 * 提示：
 * 1、1 <= power.length <= 10^5
 * 2、1 <= power[i] <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-total-damage-with-spell-casting/
"""
from typing import Counter, List


class Solution:

    def maximumTotalDamage(self, power: List[int]) -> int:
        ans, n = 0, len(power)
        cnt = sorted([[v, c] for v, c in Counter(power).items()])
        f = [0] * (len(cnt))
        for i, (v, c) in enumerate(cnt):
            f[i] = v * c
            if i >= 1:
                if v - cnt[i - 1][0] <= 2:
                    f[i] = max(f[i], f[i - 1])
                else:
                    f[i] = max(f[i], f[i - 1] + v * c)
            if i >= 2:
                if v - cnt[i - 2][0] <= 2:
                    f[i] = max(f[i], f[i - 2])
                else:
                    f[i] = max(f[i], f[i - 2] + v * c)
            if i >= 3:
                f[i] = max(f[i], f[i - 3] + v * c)
            ans = max(ans, f[i])
        return ans


if __name__ == '__main__':
    # 6
    print(Solution().maximumTotalDamage([1, 1, 3, 4]))
    # 13
    print(Solution().maximumTotalDamage([7, 1, 6, 6]))
    #
    # print(Solution().maximumTotalDamage())
