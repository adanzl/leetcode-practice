"""
 * 给你两个二维整数数组 items1 和 items2 ，表示两个物品集合。每个数组 items 有以下特质：
 * 1、items[i] = [value_i, weight_i] 其中 value_i 表示第 i 件物品的 价值 ，weight_i 表示第 i 件物品的 重量 。
 * 2、items 中每件物品的价值都是 唯一的 。
 * 请你返回一个二维数组 ret，其中 ret[i] = [value_i, weight_i]， weight_i 是所有价值为 value_i 物品的 重量之和 。
 * 注意：ret 应该按价值 升序 排序后返回。
 * 提示：
 * 1、1 <= items1.length, items2.length <= 1000
 * 2、items1[i].length == items2[i].length == 2
 * 3、1 <= value_i, weight_i <= 1000
 * 4、items1 中每个 value_i 都是 唯一的 。
 * 5、items2 中每个 value_i 都是 唯一的 。
 * 链接：https://leetcode.cn/problems/merge-similar-items/
"""
from typing import Counter, List


class Solution:

    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        return sorted([[k, v] for k, v in (Counter({v: c for v, c in items1}) + Counter({v: c for v, c in items2})).items()])


if __name__ == '__main__':
    # [[1,6],[3,9],[4,5]]
    print(Solution().mergeSimilarItems([[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]]))
    # [[1,4],[2,4],[3,4]]
    print(Solution().mergeSimilarItems([[1, 1], [3, 2], [2, 3]], items2=[[2, 1], [3, 2], [1, 3]]))
    # [[1,7],[2,4],[7,1]]
    print(Solution().mergeSimilarItems([[1, 3], [2, 2]], items2=[[7, 1], [2, 2], [1, 4]]))
