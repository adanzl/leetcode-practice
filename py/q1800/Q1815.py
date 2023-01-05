"""
 * 有一个甜甜圈商店，每批次都烤 batchSize 个甜甜圈。这个店铺有个规则，就是在烤一批新的甜甜圈时，之前 所有 甜甜圈都必须已经全部销售完毕。给你一个整数 batchSize 和一个整数数组 groups ，数组中的每个整数都代表一批前来购买甜甜圈的顾客，其中 groups[i] 表示这一批顾客的人数。每一位顾客都恰好只要一个甜甜圈。
 * 当有一批顾客来到商店时，他们所有人都必须在下一批顾客来之前购买完甜甜圈。如果一批顾客中第一位顾客得到的甜甜圈不是上一组剩下的，那么这一组人都会很开心。
 * 你可以随意安排每批顾客到来的顺序。请你返回在此前提下，最多 有多少组人会感到开心。
 * 提示：
 * 1、1 <= batchSize <= 9
 * 2、1 <= groups.length <= 30
 * 3、1 <= groups[i] <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-number-of-groups-getting-fresh-donuts/
"""
from typing import List
from functools import cache
import math
import random


class Solution:

    def maxHappyGroups1(self, batchSize: int, groups: List[int]) -> int:

        # np hard问题，可以使用模拟退火，这次过了下一次就不确定，这玩意看脸

        def calc(arr):
            ret, sm = 1, arr[0]
            nonlocal ans
            for i in range(1, len(arr)):
                if sm % batchSize == 0:
                    ret += 1
                sm += arr[i]
            ans = max(ans, ret)
            return ret

        ans = 0
        T, t = 1e6, 1e-5  # 退火的温度上下界

        def simulate_anneal(groups):
            random.shuffle(groups)  # 洗牌
            tt = T
            while tt > t:
                i = random.randint(0, len(groups) - 1)
                j = random.randint(0, len(groups) - 1)
                before = calc(groups)
                groups[i], groups[j] = groups[j], groups[i]
                after = calc(groups)
                delta = after - before
                # 变坏了依然有几率保存结果 math.e ** (delta / i)
                if delta < 0 and math.e**(delta / tt) < random.random():
                    groups[i], groups[j] = groups[j], groups[i]
                tt *= 0.975

        if batchSize == 1: return len(groups)
        g, free = [], 0
        for num in groups:
            if num % batchSize == 0: free += 1
            else: g.append(num)
        for i in range(30):  # 多次退火尝试
            simulate_anneal(g)
        return ans + free

    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        # 基于batchSize的余数分组，枚举每种余数的选取情况
        n = len(groups)
        rm = [0] * 9
        for g in groups:
            rm[g % batchSize] += 1

        @cache
        def dfs(*args):
            if sum(args) == 0: return 0
            sm = sum([i * v for i, v in enumerate(args)])
            ret = 0
            for i in range(len(args)):
                if args[i] == 0: continue
                a = list(args)
                a[i] -= 1
                ret = max(ret, dfs(*a) + (1 if (sm - i) % batchSize == 0 else 0))
            return ret

        return dfs(*rm)


if __name__ == '__main__':
    # 11
    print(Solution().maxHappyGroups(9, [1, 3, 2, 5, 2, 2, 1, 6, 3, 2, 5, 2, 2, 1, 6, 3, 2, 5, 2, 2, 1, 6, 3, 2, 5, 2, 2, 1, 6, 6]))
    # 4
    print(Solution().maxHappyGroups(3, [1, 2, 3, 4, 5, 6]))
    # 4
    print(Solution().maxHappyGroups(4, [1, 3, 2, 5, 2, 2, 1, 6]))