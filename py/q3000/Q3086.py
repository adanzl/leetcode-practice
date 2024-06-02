"""
 * 给你一个下标从 0 开始的二进制数组 nums，其长度为 n ；另给你一个 正整数 k 以及一个 非负整数 maxChanges 。
 * 灵茶山艾府在玩一个游戏，游戏的目标是让灵茶山艾府使用 最少 数量的 行动 次数从 nums 中拾起 k 个 1 。
 * 游戏开始时，灵茶山艾府可以选择数组 [0, n - 1] 范围内的任何索引index 站立。
 * 如果 nums[index] == 1 ，灵茶山艾府就会拾起一个 1 ，并且 nums[index] 变成0（这 不算 作一次行动）。
 * 之后，灵茶山艾府可以执行 任意数量 的 行动（包括零次），在每次行动中灵茶山艾府必须 恰好 执行以下动作之一：
 * 1、选择任意一个下标 j != index 且满足 nums[j] == 0 ，然后将 nums[j] 设置为 1 。这个动作最多可以执行 maxChanges 次。
 * 2、选择任意两个相邻的下标 x 和 y（|x - y| == 1）且满足 nums[x] == 1, nums[y] == 0 ，
 *     然后交换它们的值（将 nums[y] = 1 和 nums[x] = 0）。
 *     如果 y == index，在这次行动后灵茶山艾府拾起一个 1 ，并且 nums[y] 变成 0 。
 * 返回灵茶山艾府拾起 恰好 k 个 1 所需的 最少 行动次数。
 * 提示：
 * 1、2 <= n <= 10^5
 * 2、0 <= nums[i] <= 1
 * 3、1 <= k <= 10^5
 * 4、0 <= maxChanges <= 10^5
 * 5、maxChanges + sum(nums) >= k
 * 链接：https://leetcode.cn/problems/minimum-moves-to-pick-k-ones/
"""
from itertools import accumulate
from math import inf
from typing import List


class Solution:

    def minimumMoves(self, nums: List[int], k: int, max_changes: int) -> int:
        pos = []
        c = 0  # nums 中连续的 1 长度
        for i, x in enumerate(nums):
            if x == 0:
                continue
            pos.append(i)  # 记录 1 的位置
            c = max(c, 1)
            if i > 0 and nums[i - 1] == 1:
                if i > 1 and nums[i - 2] == 1:
                    c = 3  # 有 3 个连续的 1
                else:
                    c = max(c, 2)  # 有 2 个连续的 1

        c = min(c, k)
        if max_changes >= k - c:
            # 其余 k-c 个 1 可以全部用两次操作得到
            return max(c - 1, 0) + (k - c) * 2

        n = len(pos)
        pre_sum = list(accumulate(pos, initial=0))

        ans = int(inf)
        # 除了 max_changes 个数可以用两次操作得到，其余的 1 只能一步步移动到 pos[i]
        size = k - max_changes
        for right in range(size, n + 1):
            # s1+s2 是 j 在 [left, right) 中的所有 pos[j] 到 pos[(left+right)/2] 的距离之和
            left = right - size
            i = left + size // 2
            s1 = pos[i] * (i - left) - (pre_sum[i] - pre_sum[left])
            s2 = pre_sum[right] - pre_sum[i] - pos[i] * (right - i)
            ans = min(ans, s1 + s2)
        return ans + max_changes * 2


if __name__ == '__main__':
    # 3
    print(Solution().minimumMoves([1, 1, 0, 0, 0, 1, 1, 0, 0, 1], 3, 1))
    # 4
    print(Solution().minimumMoves([0, 0, 0, 0], 2, 3))
    #
    # print(Solution().minimumMoves())
