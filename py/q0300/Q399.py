"""
 * 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，
 * 其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。
 * 每个 Ai 或 Bi 是一个表示单个变量的字符串。
 * 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。
 * 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。
 * 如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。
 * 注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。
 * 提示：
 * 1、1 <= equations.length <= 20
 * 2、equations[i].length == 2
 * 3、1 <= Ai.length, Bi.length <= 5
 * 4、values.length == equations.length
 * 5、0.0 < values[i] <= 20.0
 * 6、1 <= queries.length <= 20
 * 7、queries[i].length == 2
 * 8、1 <= Cj.length, Dj.length <= 5
 * 9、Ai, Bi, Cj, Dj 由小写英文字母与数字组成
 * 链接：https://leetcode.cn/problems/evaluate-division/
"""
from typing import List


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ans = []
        g = {}
        for (a, b), v in zip(equations, values):
            g.setdefault(a, {})[b] = v
            g.setdefault(b, {})[a] = 1.0 / v

        def dfs(g, a, b, visited):
            if a not in g or b not in g:
                return -1.0
            if b in g[a]:
                return g[a][b]
            visited.add(a)
            for c in g[a]:
                if c not in visited:
                    d = dfs(g, c, b, visited)
                    if d != -1.0:
                        return g[a][c] * d
            return -1.0

        for c, d in queries:
            ans.append(dfs(g, c, d, set()))
        return ans


if __name__ == '__main__':
    # [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    print(Solution().calcEquation([["a", "b"], ["b", "c"]], values=[2.0, 3.0], queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
    # [3.75000,0.40000,5.00000,0.20000]
    print(Solution().calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], values=[1.5, 2.5, 5.0], queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]))
    # [0.50000,2.00000,-1.00000,-1.00000]
    print(Solution().calcEquation([["a", "b"]], values=[0.5], queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]))
    # [-1.00000,0.50000,3.00000,1.00000,-1.00000]
    print(Solution().calcEquation([["a", "b"], ["ab", "c"], ["a", "bc"]], [2.0, 3.0, 4.0], [["a", "c"], ["b", "a"], ["ab", "c"], ["a", "a"], ["x", "x"]]))
