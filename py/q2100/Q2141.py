"""
 * 你有 n 台电脑。给你整数 n 和一个下标从 0 开始的整数数组 batteries ，其中第 i 个电池可以让一台电脑 运行 batteries[i] 分钟。
 * 你想使用这些电池让 全部 n 台电脑 同时 运行。
 * 一开始，你可以给每台电脑连接 至多一个电池 。然后在任意整数时刻，你都可以将一台电脑与它的电池断开连接，并连接另一个电池，你可以进行这个操作 任意次 。
 * 新连接的电池可以是一个全新的电池，也可以是别的电脑用过的电池。断开连接和连接新的电池不会花费任何时间。
 * 注意，你不能给电池充电。
 * 请你返回你可以让 n 台电脑同时运行的 最长 分钟数。
 * 提示：
 * 1、1 <= n <= batteries.length <= 10^5
 * 2、1 <= batteries[i] <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-running-time-of-n-computers/
"""
from typing import List

# @lc app=leetcode.cn id=2141 lang=python3


# @lc code=start
class Solution:
    '''
        当 n⋅x ≤ sum 成立时，必然可以让 n 台电脑同时运行 x 分钟
        记电池电量和为 sum，则理论上至多可以供电 x = sum // n 分钟。
        我们对电池电量从大到小排序，然后从电量最大的电池开始遍历：
            若该电池电量超过 x，则将其供给一台电脑，问题缩减为 n - 1 台电脑的子问题。
            若该电池电量不超过 x，则其余电池的电量均不超过 x，此时有 n*x = n*(sum//n) ≤ sum, 这些电池可以给 n 台电脑供电 x 分钟。
    '''

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        s = sum(batteries)
        for b in sorted(batteries, reverse=True):
            if b <= s // n:
                return s // n
            s -= b
            n -= 1
        return 0


# @lc code=end

if __name__ == '__main__':
    # 4
    print(Solution().maxRunTime(2, batteries=[3, 3, 3]))
    # 2
    print(Solution().maxRunTime(2, batteries=[1, 1, 1, 1]))
