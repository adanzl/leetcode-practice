"""
 * 给你一个二维整数数组 items ，其中 items[i] = [price_i, beauty_i] 分别表示每一个物品的 价格 和 美丽值 。
 * 同时给你一个下标从 0 开始的整数数组 queries 。
 * 对于每个查询 queries[j] ，你想求出价格小于等于 queries[j] 的物品中，最大的美丽值 是多少。
 * 如果不存在符合条件的物品，那么查询的结果为 0 。
 * 请你返回一个长度与 queries 相同的数组 answer，其中 answer[j]是第 j 个查询的答案。
 * 提示：
 * 1、1 <= items.length, queries.length <= 10^5
 * 2、items[i].length == 2
 * 3、1 <= price_i, beauty_i, queries[j] <= 10^9
 * 链接：https://leetcode.cn/problems/most-beautiful-item-for-each-query
"""

from heapq import heappush
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=2070 lang=python3
# @lcpr version=20003
#
# [2070] 每一个查询的最大美丽值
#


# @lc code=start
class Solution:

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        items.sort(key=lambda x: x[0])
        ans = [0] * n
        h = []
        for v, i in sorted([[q, i] for i, q in enumerate(queries)]):
            while items and items[0][0]<=v:
                heappush(h, -items.pop(0)[1])
            if h:
                ans[i] = -h[0]
        return ans


# @lc code=end


if __name__ == '__main__':
    # [2,4,5,5,6,6]
    print(Solution().maximumBeauty([[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], queries=[1, 2, 3, 4, 5, 6]))
    # [4]
    print(Solution().maximumBeauty([[1, 2], [1, 2], [1, 3], [1, 4]], queries=[1]))
    # [0]
    print(Solution().maximumBeauty([[10, 1000]], queries=[5]))
