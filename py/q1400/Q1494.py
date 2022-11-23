"""
 * 给你一个整数 n 表示某所大学里课程的数目，编号为 1 到 n ，数组 relations 中， relations[i] = [xi, yi]  表示一个先修课的关系，也就是课程 xi 必须在课程 yi 之前上。
 * 同时你还有一个整数 k 。
 * 在一个学期中，你 最多 可以同时上 k 门课，前提是这些课的先修课在之前的学期里已经上过了。
 * 请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。
 * 提示：
 * 1、1 <= n <= 15
 * 2、1 <= k <= n
 * 3、0 <= relations.length <= n * (n-1) / 2
 * 4、relations[i].length == 2
 * 5、1 <= xi, yi <= n
 * 6、xi != yi
 * 7、所有先修关系都是不同的，也就是说 relations[i] != relations[j] 。
 * 8、题目输入的图是个有向无环图。
 * 链接：https://leetcode.cn/problems/parallel-courses-ii/
"""
from functools import cache
from typing import List
from itertools import combinations


class Solution:

    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:

        @cache
        def dfs(state):
            if state == (1 << n) - 1: return 0
            nex = [i for i in range(n) if not state & (1 << i) and state & pre[i] == pre[i]]
            res = n + 1
            for sub in combinations(nex, min(k, len(nex))):  # 遍历组合
                res = min(res, 1 + dfs(state | sum([1 << i for i in sub])))
            return res

        pre = [0] * n
        for i, j in relations:
            pre[j - 1] |= 1 << (i - 1)
        return dfs(0)


if __name__ == '__main__':
    # 3
    print(Solution().minNumberOfSemesters(4, [[2, 1], [3, 1], [1, 4]], 2))
    # 4
    print(Solution().minNumberOfSemesters(5, [[2, 1], [3, 1], [4, 1], [1, 5]], 2))
    # 6
    print(Solution().minNumberOfSemesters(11, [], 2))
