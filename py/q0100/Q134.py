"""
 * 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
 * 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
 * 给定两个整数数组 gas 和 cost ，如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。
 * 提示:
 * 1、gas.length == n
 * 2、cost.length == n
 * 3、1 <= n <= 10^5
 * 4、0 <= gas[i], cost[i] <= 10^4
 * 链接：https://leetcode.cn/problems/gas-station/
"""
from typing import List


class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        spare, minSpare, minIndex = 0, float('inf'), 0
        for i in range(n):
            spare += gas[i] - cost[i]
            if spare < minSpare:
                minSpare = spare
                minIndex = i

        return -1 if spare < 0 else (minIndex + 1) % n


if __name__ == '__main__':
    # 
    print(Solution().canCompleteCircuit([10, 30, 3, 50, 5], [30, 4, 50, 5, 2]))
    # 3
    print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    # -1
    print(Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]))