"""
 * 给你有一个 非负 整数 k 。有一个无限长度的台阶，最低 一层编号为 0 。
 * 虎老师有一个整数 jump ，一开始值为 0 。
 * 虎老师从台阶 1 开始，虎老师可以使用 任意 次操作，目标是到达第 k 级台阶。
 * 假设虎老师位于台阶 i ，一次 操作 中，虎老师可以：
 * 1、向下走一级到 i - 1 ，但该操作 不能 连续使用，如果在台阶第 0 级也不能使用。
 * 2、向上走到台阶 i + 2^jump 处，然后 jump 变为 jump + 1 。
 * 请你返回虎老师到达台阶 k 处的总方案数。
 * 注意 ，虎老师可能到达台阶 k 处后，通过一些操作重新回到台阶 k 处，这视为不同的方案。
 * 提示：0 <= k <= 10^9
 * 链接：https://leetcode.cn/problems/find-number-of-ways-to-reach-the-k-th-stair/description/
"""
from functools import cache


class Solution:

    def waysToReachStair(self, k: int) -> int:

        @cache
        def dfs(f, j, pre):
            if f - k > 1: return 0
            ret = 0
            if f == k:
                ret += 1
            if f > 0 and pre != 1:
                ret += dfs(f - 1, j, 1)
            ret += dfs(f + (1 << j), j + 1, 2)
            return ret

        return dfs(1, 0, -1)


if __name__ == '__main__':
    # 4
    print(Solution().waysToReachStair(2))
    # 4
    print(Solution().waysToReachStair(1))
    # 2
    print(Solution().waysToReachStair(0))
    # 0
    print(Solution().waysToReachStair(10**9))
    # 5985
    print(Solution().waysToReachStair(1048559))
