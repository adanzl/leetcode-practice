"""
 * 你打算做甜点，现在需要购买配料。目前共有 n 种冰激凌基料和 m 种配料可供选购。而制作甜点需要遵循以下几条规则：
 * 1、必须选择 一种 冰激凌基料。
 * 2、可以添加 一种或多种 配料，也可以不添加任何配料。
 * 3、每种类型的配料 最多两份 。
 * 给你以下三个输入：
 * 1、baseCosts ，一个长度为 n 的整数数组，其中每个 baseCosts[i] 表示第 i 种冰激凌基料的价格。
 * 2、toppingCosts，一个长度为 m 的整数数组，其中每个 toppingCosts[i] 表示 一份 第 i 种冰激凌配料的价格。
 * 3、target ，一个整数，表示你制作甜点的目标价格。
 * 你希望自己做的甜点总成本尽可能接近目标价格 target 。
 * 返回最接近 target 的甜点成本。如果有多种方案，返回 成本相对较低 的一种。
 * 提示：
 * n == baseCosts.length
 * m == toppingCosts.length
 * 1 <= n, m <= 10
 * 1 <= baseCosts[i], toppingCosts[i] <= 10^4
 * 1 <= target <= 10^4
 * 链接：https://leetcode.cn/problems/closest-dessert-cost/
"""
from bisect import bisect_left
from typing import List


class Solution:

    def closestCost(self, bc: List[int], tc: List[int], t: int) -> int:
        arr = [0]
        for i in range(len(tc)):
            for j in range(len(arr)):
                arr.append(arr[j] + tc[i])
        for i in range(len(tc)):
            for j in range(len(arr)):
                arr.append(arr[j] + tc[i])
        ans = sorted([n1 + n2 for n1 in bc for n2 in arr])
        idx = bisect_left(ans, t)
        if idx == len(ans): return ans[-1]
        if ans[idx] == t: return t
        if abs(ans[idx] - t) < abs(ans[idx - 1] - t):
            return ans[idx]
        else:
            return ans[idx - 1]



if __name__ == '__main__':
    # 10
    print(Solution().closestCost([1,7],  [3,4],  10))
    # 17
    print(Solution().closestCost([2,3],  [4,5,100],  18    ))
    # 8
    print(Solution().closestCost([3, 10], [2, 5], 9))
    # 10
    print(Solution().closestCost([10], [1], 1))
