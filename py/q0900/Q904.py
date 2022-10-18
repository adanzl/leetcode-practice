"""
 * 你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果 种类 。
 * 你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：
 * 1、你只有 两个 篮子，并且每个篮子只能装 单一类型 的水果。每个篮子能够装的水果总量没有限制。
 * 2、你可以选择任意一棵树开始采摘，你必须从 每棵 树（包括开始采摘的树）上 恰好摘一个水果 。采摘的水果应当符合篮子中的水果类型。每采摘一次，你将会向右移动到下一棵树，并继续采摘。
 * 3、一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。
 * 给你一个整数数组 fruits ，返回你可以收集的水果的 最大 数目。
 * 提示：
 * 1、1 <= fruits.length <= 10^5
 * 2、0 <= fruits[i] < fruits.length
 * 链接：https://leetcode.cn/problems/fruit-into-baskets/
"""
from typing import List


class Solution:

    def totalFruit(self, fruits: List[int]) -> int:
        max = lambda a, b: a if a > b else b
        ans = 0
        idx1, idx2 = -1, -1
        v1, v2 = -1, -1
        i0 = -1
        for i, f in enumerate(fruits):
            if f == v1: idx1 = i
            elif f == v2: idx2 = i
            else:
                i0 = min(idx1, idx2)
                if idx1 < idx2:
                    idx1 = i
                    v1 = f
                else:
                    idx2 = i
                    v2 = f
            ans = max(ans, max(idx1, idx2) - i0)
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().totalFruit([1, 2, 1]))
    # 3
    print(Solution().totalFruit([0, 1, 2, 2]))
    # 4
    print(Solution().totalFruit([1, 2, 3, 2, 2]))
