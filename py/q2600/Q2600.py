"""
 * 袋子中装有一些物品，每个物品上都标记着数字 1 、0 或 -1 。
 * 给你四个非负整数 numOnes 、numZeros 、numNegOnes 和 k 。
 * 袋子最初包含：
 * 1、numOnes 件标记为 1 的物品。
 * 2、numZeroes 件标记为 0 的物品。
 * 3、numNegOnes 件标记为 -1 的物品。
 * 现计划从这些物品中恰好选出 k 件物品。返回所有可行方案中，物品上所标记数字之和的最大值。
 * 提示：
 * 1、0 <= numOnes, numZeros, numNegOnes <= 50
 * 2、0 <= k <= numOnes + numZeros + numNegOnes
 * 链接：https://leetcode.cn/problems/k-items-with-the-maximum-sum/
"""

class Solution:

    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes: return k
        if k <= numOnes + numZeros: return numOnes
        return numOnes - (k - numOnes - numZeros)


if __name__ == '__main__':
    # 2
    print(Solution().kItemsWithMaximumSum(3, numZeros=2, numNegOnes=0, k=2))
    # 3
    print(Solution().kItemsWithMaximumSum(3, numZeros=2, numNegOnes=0, k=4))
    #
    # print(Solution().kItemsWithMaximumSum())