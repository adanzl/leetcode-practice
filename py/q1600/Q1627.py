"""
 * 有 n 座城市，编号从 1 到 n 。编号为 x 和 y 的两座城市直接连通的前提是： 
 * x 和 y 的公因数中，至少有一个 严格大于 某个阈值 threshold 。
 * 更正式地说，如果存在整数 z ，且满足以下所有条件，则编号 x 和 y 的城市之间有一条道路：
 * 1、x % z == 0
 * 2、y % z == 0
 * 3、z > threshold
 * 给你两个整数 n 和 threshold ，以及一个待查询数组，
 * 请你判断每个查询 queries[i] = [a_i, b_i] 指向的城市 ai 和 bi 是否连通（即，它们之间是否存在一条路径）。
 * 返回数组 answer ，其中answer.length == queries.length 。
 * 如果第 i 个查询中指向的城市 a_i 和 b_i 连通，则 answer[i] 为 true ；如果不连通，则 answer[i] 为 false 。
 * 提示：
 * 1、2 <= n <= 10^4
 * 2、0 <= threshold <= n
 * 3、1 <= queries.length <= 10^5
 * 4、queries[i].length == 2
 * 5、1 <= a_i, b_i <= cities
 * 6、a_i != b_i
 * 链接：https://leetcode.cn/problems/graph-connectivity-with-threshold/
"""

from math import isqrt
from typing import List

#
# @lc app=leetcode.cn id=1627 lang=python3
#
# [1627] 带阈值的图连通性
#

# @lc code=start


class Solution:

    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n + 1)]

        def find(x):
            r = x
            while parent[r] != r:
                r = parent[r]
            while parent[x] != r:
                parent[x], x = r, parent[x]
            return r

        for num in range(threshold + 1, n + 1):
            for v in range(1, isqrt(num) + 1):
                a, r = divmod(num, v)
                if r: continue
                if v > threshold:
                    r0, r1 = find(v), find(num)
                    parent[r1] = r0
                if a != v and a > threshold:
                    r0, r1 = find(a), find(num)
                    parent[r1] = r0
        return [find(x) == find(y) for x, y in queries]


# @lc code=end

if __name__ == '__main__':
    # [False, False, True]
    print(Solution().areConnected(10**4, threshold=2, queries=[[1, 4], [2, 5], [3, 6]]))
    # [false,false,true]
    print(Solution().areConnected(6, threshold=2, queries=[[1, 4], [2, 5], [3, 6]]))
    # [true,true,true,true,true]
    print(Solution().areConnected(6, threshold=0, queries=[[4, 5], [3, 4], [3, 2], [2, 6], [1, 3]]))
    # [false,false,false,false,false]
    print(Solution().areConnected(5, threshold=1, queries=[[4, 5], [4, 5], [3, 2], [2, 3], [3, 4]]))
