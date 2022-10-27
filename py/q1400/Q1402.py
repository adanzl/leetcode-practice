"""
 * 一个厨师收集了他 n 道菜的满意程度 satisfaction ，这个厨师做出每道菜的时间都是 1 单位时间。
 * 一道菜的 「喜爱时间」系数定义为烹饪这道菜以及之前每道菜所花费的时间乘以这道菜的满意程度，也就是 time[i]*satisfaction[i] 。
 * 请你返回做完所有菜 「喜爱时间」总和的最大值为多少。
 * 你可以按 任意 顺序安排做菜的顺序，你也可以选择放弃做某些菜来获得更大的总和。
 * 提示：
 * 1、n == satisfaction.length
 * 2、1 <= n <= 500
 * 3、-1000 <= satisfaction[i] <= 1000
 * 链接：https://leetcode.cn/problems/reducing-dishes/
"""
from typing import List


class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        po, na = [], []
        for s in satisfaction:
            po.append(s) if s >= 0 else na.append(s)
        ps, ns = sum(po), 0
        ans = 0
        for i in range(len(po)):
            ans += (i + 1) * po[i]
        for i in range(len(na) - 1, -1, -1):
            score = ps + ns + na[i]
            if score <= 0: break
            ans += score
            ns += na[i]
        return ans


if __name__ == '__main__':
    # 14
    print(Solution().maxSatisfaction([-1, -8, 0, 5, -9]))
    # 20
    print(Solution().maxSatisfaction([4, 3, 2]))
    # 0
    print(Solution().maxSatisfaction([-1, -4, -5]))
